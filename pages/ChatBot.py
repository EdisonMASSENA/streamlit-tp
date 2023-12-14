import streamlit as st
import time
from TextProcessor import *

ai = TextProcessor()

with st.chat_message("assistant"):
    st.write("Hello 👋")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    
    response = ""
    if '/trad' in prompt:
        req = prompt.replace('/trad', '')
        response = ai.translate(req)
    elif '/sum' in prompt:
        req = prompt.replace('/sum', '')
        response = ai.summary(req)
    elif '/img' in prompt:
        req = prompt.replace('/img', '')
        response = ai.imagine(req)
    elif '/code' in prompt:
        req = prompt.replace('/code', '')
        response = ai.code(req)
    elif '/actu' in prompt:
        req = prompt.replace('/actu', '')
        response = ai.actu(req)
    elif '/json' in prompt:
        req = prompt.replace('/json', '')
        response = ai.json_format(req)

    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = response


        if '/img' in prompt:            
            st.session_state.messages.append({"role": "assistant", "content": st.image(response)})
        else:
            # Simulate stream of response with milliseconds delay
            for chunk in assistant_response:
                full_response += chunk + " "
                time.sleep(0.05)
                # Add a blinking cursor to simulate typing
                message_placeholder.markdown(full_response + "▌")
            message_placeholder.markdown(response)
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
