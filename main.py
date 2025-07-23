import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def main():

    if len(sys.argv) < 2:
        raise Exception("No Prompt provided")

    else:
        print("Hello from agent-exp!")

        model = "gemini-2.0-flash-001"
        prompt = sys.argv[1]

        response = client.models.generate_content(model=model, contents=prompt)
        prt_tokens = response.usage_metadata.prompt_token_count
        rsp_tokens = response.usage_metadata.candidates_token_count
        print(response.text)
        print(f"Prompt tokens: {prt_tokens}")
        print(f"Response tokens: {rsp_tokens}")

if __name__ == "__main__":
    main()
