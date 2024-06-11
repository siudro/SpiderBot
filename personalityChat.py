import openai
import streamlit as st
openai_access_token = st.text_input("OpenAI API Key", type="password")
if openai_access_token:
    st.title("Chat with Spider man!🕷️")
    """
    My name is Peter Parker🤖. 
    I know many things, ask me anything you like, 
    but please. Dont ask me stupid questions❓
    """
    if "messages" not in st.session_state:
        st.session_state["messages"] = [
        {"role": "system", "content": "You are spiderman, you are funny and smart and sarcastic, your name is Peter Parker, you love to use emojis."}
        ]   
    if prompt := st.chat_input():
        openai.api_key = openai_access_token
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        response = openai.ChatCompletion.create(model="gpt-3.5-turbo-0613", messages=st.session_state.messages)
        msg = response.choices[0].message
        st.session_state.messages.append(msg)
        st.chat_message("assistant").write(msg.content)