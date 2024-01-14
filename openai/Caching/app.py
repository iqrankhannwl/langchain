import os
from langchain.globals import set_llm_cache
from langchain_openai import ChatOpenAI
from langchain.cache import InMemoryCache
from langchain.cache import SQLiteCache
from decouple import config

print(os.chroot())

OPENAI_API_KEY=config("OPEN_API_KEY")

def in_memory_cache(query):
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    set_llm_cache(InMemoryCache())
    res = llm.invoke(query)
    return res


# # We can do the same thing with a SQLite cache
def sqlite_cache(query):
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY)
    set_llm_cache(SQLiteCache(database_path=".langchain.db"))
    res = llm.invoke(query)
    return res

result = sqlite_cache("how the best man the whol world?")
print(result)

