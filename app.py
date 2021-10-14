import streamlit as st
import requests


st.title('Chatbot Test')

URL = 'http://35.236.187.220:8080/webhooks/rest/webhook'

input = st.text_input('input')

response = requests.post(URL, data={'sender':'Andrew', 'message':'Hello'})
if response is not NONE:
  json_response = response.json()
  st.write('Response')
  st.text(json_response['text'])
