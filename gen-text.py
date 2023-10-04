import streamlit as st
import openai

# Set your OpenAI API key 
openai.api_key =st.secrets["openai_key"]


st.title("Text-to-Text Generator")

    # Input text box for user to enter a prompt
prompt = st.text_area("Enter a prompt:")
def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=12 
    )
    return response.choices[0].text


    # Button to generate text
if st.button("Generate"):
    if prompt:
        generated_text = generate_text(prompt)
        st.write("Generated Text:")
        st.write(generated_text)
    else:
        st.warning("Please enter a prompt.")




