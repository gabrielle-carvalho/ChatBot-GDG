# To run this code you need to install the following dependencies:
# pip install google-genai

from dotenv import load_dotenv  # This is the new import you need

load_dotenv()

import os
from google import genai
from google.genai import types
import base64 #tava no codigo gerado pelo ai studio

# os.environ['GOOGLE_API_KEY'] = "chave"

def generate(entrada):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.5-pro-preview-06-05"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=entrada),
            ],
        ),
    ]
    tools = [
        types.Tool(google_search=types.GoogleSearch()),
    ]
    generate_content_config = types.GenerateContentConfig(
        tools=tools,
        response_mime_type="text/plain",
    )

    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        print(chunk.text, end="")

if __name__ == "__main__":
    generate()


# def generate():
#     client = genai.Client(
#         api_key=os.environ.get("GEMINI_API_KEY"),
#     )
#     # TAREFA 1: escolher o modelo apropriado e ajustar entrada do usuário e retorno da função

#if __name__ == "__main__":
#    # Teste para ter certeza que funciona
#    test_response = generate(entrada="Olá, como está o tempo hoje em Cuiabá?")
#    print(f"Test response: {test_response}")