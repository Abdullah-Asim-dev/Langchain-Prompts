from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Groq ka active model specify karna behtar hota hai
model = ChatGroq(model_name="wen/qwen3.6-27b") 

# ERROR FIXED: Yahan se '=' ka sign hata diya hai
messages = [
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

# Model ko invoke karein
result = model.invoke(messages)

# AI ka response list mein append karein
messages.append(AIMessage(content=result.content))

# Print karein
print(messages)
