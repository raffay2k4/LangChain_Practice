import chainlit as cl
import prompts
from langchain_cohere import ChatCohere
from langchain_core.runnables import Runnable
from langchain_core.messages import AIMessage, HumanMessage

chat_history=[]

llm=ChatCohere(
    model="command-r-plus",
    temperature=0.7
)

joke_chain = (
    prompts.joke_prompt
    | llm
)

haider_chain = (
    prompts.haider_prompt
    | llm
)

dmart_chain=(
    prompts.dmart_prompt
    | llm
)

async def run_chatbot(user_input: dict, chain: Runnable):
    
    response = cl.Message(content="")

    for token in chain.stream(user_input):
        await response.stream_token(token.content)
    
    await response.send()

    chat_history.extend(
        [
            HumanMessage(content=user_input["input"]),
            AIMessage(content=response.content)
        ]
    )
   