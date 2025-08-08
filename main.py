import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_files import schema_write_file
from functions.run_python import schema_run_python_file
from functions.call_function import call_function


SYSTEM_PROMPT = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_write_file,
        schema_run_python_file,
    ]
)

def main():

    # sys.argv is a list, 0 is the program, the rest are the attributes with which the program is called
    try :
        user_prompt = sys.argv[1]
        verboseB = False
        if "--verbose" in sys.argv[2:]:
            verboseB = True


        print("Hello from agent-exp!")
        model_name = "gemini-2.0-flash-001"

        user_prompt = sys.argv[1]

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]

        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions],system_instruction=SYSTEM_PROMPT),
            )

        if response.function_calls:
            for call in response.function_calls:
                #print(f"Calling function: {call.name}({call.args})")

                output = call_function(call, verbose=verboseB)
                try:
                    func_response = output.parts[0].function_response.response
                    if verboseB:
                        print(f"-> {output.parts[0].function_response.response}")
                except Exception:
                    raise Exception("Fatal: No response from function call")
                    


        else:
            print(response.text)
        
        #check if --verbose option is passed as an additional argument after the first two items in the list
        if verboseB:

            prt_tokens = response.usage_metadata.prompt_token_count
            rsp_tokens = response.usage_metadata.candidates_token_count
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prt_tokens}")
            print(f"Response tokens: {rsp_tokens}")

    except IndexError:
        raise Exception("No Prompt provided")
        

if __name__ == "__main__":
    main()
