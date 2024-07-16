import streamlit as st
import requests
import os

st.header('Gastronomic Content Creator')  
text = st.text_input('Recipe name')

base_url = "https://api.dify.ai/v1"
path = "/completion-messages"
my_secret = os.environ['DIFY_APP_SECRET']

headers = {
  "Authorization": f"Bearer {my_secret}",
  "Content-Type": "application/json"
}

data = {
  "inputs": {
   "text": text,
 },

"response_mode": "blocking",
"user": "create food content"
}

url_completa = base_url + path
if st.button('Generate recipe'):
  response = requests.post(url_completa, json=data, headers=headers)

  if response.status_code == 200:
   st.success("Recipe Successfully Achieved")

   result = response.json()
  # print the response
   st.markdown("### Recipe generated:")
   st.markdown(result["answer"])
  else:
   st.error("Error generating recipe")
st.write("Thank you for using the application, see you later!")




