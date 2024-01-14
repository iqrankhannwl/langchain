from decouple import config
from langchain_openai import OpenAI, ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
OPEN_API_KEY = config("OPEN_API_KEY")


# LLMs Models
def llm_model(query):
    llm = OpenAI(openai_api_key=OPEN_API_KEY)
    response = llm.invoke(query)
    return response
# Chat Model
def chat_model(query):
    chat = ChatOpenAI(openai_api_key=OPEN_API_KEY)
    response = chat.invoke(query)
    return response

# Chat model with human and system message
def chat_model_message(sys_message:str=None, human_message:str=None) -> str:
    chat = ChatOpenAI(openai_api_key=OPEN_API_KEY)
    message = [
        SystemMessage(content=sys_message),
        HumanMessage(content=human_message)
    ]
    response = chat.invoke(message)
    return response.content

result = chat_model_message("You'r helpful assitent", "who the rechist man in the world?")
print(result)