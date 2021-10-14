import streamlit as st
import requests


st.title('Chatbot Test')

URL = 'http://35.236.187.220:8080/webhooks/rest/webhook'

input = st.text_input('Type your message here')

response = requests.post(URL, json={"sender":"Andrew", "message":input})
st.subheader('Rasa Response')
if response is not None:
  json_response = response.json()
  for i in json_response:
    st.markdown(json_response[i]['text'])
    if json_response[i]['image'] is not None:
      st.image(json_response[i]['image'])
  st.write(json_response)
