from langchain_core.messages import ChatPromptTemplate
Chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} expert')
    ('human','explain in simple areas , what is {topic}')

])
prompt=Chat_template.invoke({'domain':'cricket','topic':'umpire'})
print(prompt)
