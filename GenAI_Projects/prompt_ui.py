# from google import genai
import google.generativeai as genai
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt
import os

load_dotenv()

st.header('Research Tool')

paper_input = st.selectbox("Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"])

style_input = st.selectbox("Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')

if st.button('Summarize'):
    client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
    
    # Format the template with user inputs
    prompt = template.format(
        paper_input=paper_input,
        style_input=style_input,
        length_input=length_input
    )
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    
    st.write(response.text)