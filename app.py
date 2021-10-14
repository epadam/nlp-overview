import streamlit as st
import requests


st.title('Chatbot Test')

URL = 'http://35.236.187.220:8080/webhooks/rest/webhook'

input = st.text_input('Type your message here', 'Hi')

def call_rasa(msg):
  response = requests.post(URL, json={"sender":"Andrew", "message":msg})
  return repsonse

response = call_rasa(input)

st.subheader('Rasa Response')
if response is not None:
  json_response = response.json()
  st.write(json_response)
  for res in json_response:
    st.markdown(res['text'])
    if 'image' in res:
      st.image(res['image'])
    if 'buttons' in res:
      options =[]
      for button in res['buttons']:
        options.append(button['title'])        
      option = st.radio('', options)
      #input = res['buttons'][options.index(option)]['payload']
      #response = call_rasa(input)


  
