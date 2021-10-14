import streamlit as st
import requests


st.title('Chatbot Test')

URL = 'http://35.236.187.220:8080/webhooks/rest/webhook'

input = st.text_input('Type your message here', 'Hi')

response = requests.post(URL, json={"sender":"Andrew", "message":input})
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
      for idx,  button in enumerate(res['buttons']):
        options.append(button['title'])        
      option = st.radio('', options)
      #response = requests.post(URL, json={"sender":"Andrew", "message":res['buttons'][idx]['payload']})

  
