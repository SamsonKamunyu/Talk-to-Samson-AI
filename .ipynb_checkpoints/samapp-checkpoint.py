import streamlit as st
from model.chat_engine import get_response


st.set_page_config(page_title="Talk to Samson")

st.title("Talk to Samson")
st.markdown("Ask me anything. I'll do my best to give Samson-style advice.")

# st.write("This is a personal AI therapist clone powered by LLMs and voice AI.")

# Conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if user_input := st.chat_input("Hey! What’s on your mind?"):
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.chat_message("user"):
        st.markdown(user_input)

    response = get_response(user_input)
    st.session_state.messages.append({"role": "assistant", "content": response})

    with st.chat_message("assistant"):
        st.markdown(response)