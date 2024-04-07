import streamlit as st
from dataclasses import dataclass
import requests
import urllib
@dataclass
class Message:
    actor: str
    payload: str


USER = "user"
ASSISTANT = "ai"
MESSAGES = "messages"
if MESSAGES not in st.session_state:
    st.session_state[MESSAGES] = [Message(actor=ASSISTANT, payload="Hi!How can I help you?")]

msg: Message
for msg in st.session_state[MESSAGES]:
    st.chat_message(msg.actor).write(msg.payload)

prompt: str = st.chat_input("Enter a prompt here")

if prompt:
    st.session_state[MESSAGES].append(Message(actor=USER, payload=prompt))
    st.chat_message(USER).write(prompt)
    target_url = "https://blab-backend.onrender.com"
    #message = requests.post(target_url, json={'message': prompt})
    #response: str = f"{message.text.split('<|assistant|>')[-1]}"
    st.session_state[MESSAGES].append(Message(actor=ASSISTANT, payload=prompt))
    st.chat_message(ASSISTANT).write('putsala')
