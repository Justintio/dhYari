import streamlit as st
from PIL import Image

st.title('Hai !')
siapa = ['yari', 'bukann yari', 'kesayangan juju', 'arip']
nama = st.selectbox('ini saha ya ? ', siapa) 
if nama=='yari' :
  st.write('cih polosan amat yari doang :P')
elif nama=='bukann yari' :
  st.write('pasti mba kunti')
