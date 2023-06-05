#Import library
import streamlit as st
import openai
import os
#Get API key
with open("apikey.txt", "r") as f:
    openai.api_key = f.readline()

#Hàm gọi API và trả về kết quả summarize
def generate_summarizer(max_tokens, temperature, top_p, frequency_penalty, prompt, person_type):
    res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        max_tokens=100,
        temperature=0.7,
        top_p=0.5,
        frequency_penalty=0.5,
        messages=
       [
         {
          "role": "system",
          "content": "You are a helpful assistant for text summarization.",
         },
         {
          "role": "user",
          "content": f"Summarize this for a {person_type}: {prompt}",
         },
        ],
    )
    return res["choices"][0]["message"]["content"]    

#Application summerizer
st.title("GPT-3.5 Text Summarizer")
input_text = st.text_area("Enter the text you want to summarize: ", height=200)
col1, col2, col3 = st.columns(3)

with col1:
    token = st.slider("Token", min_value=0.0, max_value=200.0, value=50.0, step=1.0)
    temp = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.0, step=0.02)
    top_p = st.slider("Nucleus Sampling", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
    f_pen = st.slider("Frequency Penalty", min_value=-1.0, max_value=1.0, value=0.0, step=0.01)
    
with col2:
    option = st.selectbox(
        "How do you like to explained?",
        (
            "Second-Grader",
            "Professional Data Scientist",
            "Housewives",
            "Retired",
            "University Student",
        ),
    )

with col3:
    with st.expander("Current Parameter"):
        st.write("Current Token: ", token)
        st.write("Current Temperature: ", temp)
        st.write("Current Nucleus Sampling: ", top_p)
        st.write("Current Frequency Penalty: ", f_pen)

if st.button("Summarize"):
    st.write(generate_summarizer(token, temp, top_p, f_pen, input_text, option))