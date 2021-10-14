import streamlit as st
import requests

if 'input' not in st.session_state:
	st.session_state.input = 'Hi'

if 'option' not in st.session_state:
	st.session_state.option = 0


st.title('Chatbot Test')

URL = 'http://35.236.187.220:8080/webhooks/rest/webhook'


input = st.text_input('Type your message here', st.session_state.input)

#if st.session_state.input is None:
#	st.session_state.input = input

response = requests.post(URL, json={"sender":"Andrew", "message":input})

st.session_state.input = None

st.write(st.session_state.option)

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
      option = st.radio('', options , key='option')
      st.session_state.input = res['buttons'][options.index(option)]['payload']

     



  
