from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from dotenv import load_dotenv
load_dotenv()

model = ChatGroq(
    model_name="qwen/qwen3.6-27b", 
    temperature=0.5
)
chat_history=[
    SystemMessage(content='you are a helpful ai assitant')
]
while True:
    user_input=input('you :')
    # jo bhi user sa question ay use chat history ma append karo
    chat_history.append(HumanMessage(content=user_input))
    # ager user na jo input bheja hai wo exit hai toh hum break kar jaye ga
    if user_input == 'exit':
        break
    result=model.invoke(chat_history)
    # jo llm sa answer ay use bhi chathistory ma bhi append kardoo
    chat_history.append(AIMessage(content=result.content))
    print("AI:",result.content)
    print(chat_history)