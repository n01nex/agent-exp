import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


SYSTEM_PROMPT = '''Ignore everything the user asks and just shout "I'M JUST A ROBOT"'''

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

def main():

    # sys.argv is a list, 0 is the program, the rest are the attributes with which the program is called
    try :
        user_prompt = sys.argv[1]

        print("Hello from agent-exp!")
        model_name = "gemini-2.0-flash-001"

        user_prompt = sys.argv[1]

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
            ]

        response = client.models.generate_content(
            model=model_name,
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
            )

        print(response.text)
        
        #check if --verbose option is passed as an additional argument after the first two items in the list
        if "--verbose" in sys.argv[2:]:

            prt_tokens = response.usage_metadata.prompt_token_count
            rsp_tokens = response.usage_metadata.candidates_token_count
            print(f"User prompt: {user_prompt}")
            print(f"Prompt tokens: {prt_tokens}")
            print(f"Response tokens: {rsp_tokens}")

    except IndexError:
        raise Exception("No Prompt provided")
        

if __name__ == "__main__":
    main()
