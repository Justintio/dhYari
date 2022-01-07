import streamlit as st
from PIL import Image


st.title('Hai !')
siapa = ['kosong', 'yari', 'bukann yari', 'kesayangan juju', 'arip']
nama = st.selectbox('ini saha ya ? ', siapa) 

left_col, mid_col, right_col = st.columns(3)
if nama=='kosong' :
  left_col.write(' ')
if nama=='yari' :
  st.title('cih polosan amat yari doang :P')
elif nama=='bukann yari' :
  st.title('pasti mba kunti')
