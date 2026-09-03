from langchain_groq import ChatGroq 
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

# Sahi model ID jo Groq cloud par available hai
model = ChatGroq(
    model_name="qwen/qwen3.6-27b", 
    temperature=0.5
)
st.header("Research Tool")
paper_input = st.selectbox("Select Research Paper Name", [
    "Select....",
    "Attention is all you need",
    "BERT:Pre-Training of Deep Bidirectional Transformers",
    "GPT-3,Language Models are few Learners",
    "Diffusion Models Beat GANs on Image Synthesis"
])

style_input = st.selectbox("Select Explanation Style", [
    "Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"
])

length_input = st.selectbox("Select Explanation Length", [
    "Short (1-2 Paragraphs)", "Medium (3-5 Paragraphs)", "Long (6-10 Paragraphs)"
])
template=load_prompt('template.json')
prompt=template.invoke({
    'paper_input':paper_input,
    'style_input':style_input,
    'length_input':length_input
})
# 4. Button click logic
if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)
