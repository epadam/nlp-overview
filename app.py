import streamlit as st
import requests


st.title('Chatbot Test')

URL = 'http://35.236.187.220:8080/webhooks/rest/webhook'

input = st.text_input('Type your message here')

response = requests.post(URL, json={"sender":"Andrew", "message":input})
st.subheader('Rasa Response')
if response is not None:
  json_response = response.json()
  st.markdown(json_response[0]['text'])
  st.write(json_response)
