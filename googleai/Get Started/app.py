from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

from decouple import config
GOOGLEAI_API_KEY = config("GOOGLE_API_KEY")


def generate_(query):
    llm = ChatGoogleGenerativeAI(google_api_key=GOOGLEAI_API_KEY, model="gemini-pro")
    response = llm.invoke(query)
    return response.content

result = generate_("Who is Hacker in the world?")
# print(result)

def generate_with_human_msg(query, img_url):
    llm = ChatGoogleGenerativeAI(google_api_key=GOOGLEAI_API_KEY, model="gemini-pro-vision")
    message = HumanMessage(
       content=[
        {
            "type": "text",
            "text": query,
        },
        {"type": "image_url", "image_url": img_url},
    ]
    )
    response = llm.invoke([message])
    return response

result = generate_with_human_msg("What's in this image?", "/home/learning/Pictures/Screenshots/Screenshot from 2024-01-07 12-45-24.png")
print(result.content)