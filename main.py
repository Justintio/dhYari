import streamlit as st
from PIL import Image

left_col, mid_col, right_col = st.columns(3)
st.title('Hai !')
siapa = ['yari', 'bukann yari', 'kesayangan juju', 'arip']
nama = st.selectbox('ini saha ya ? ', siapa) 
if nama=='yari' :
  st.mid_col('cih polosan amat yari doang :P')
elif nama=='bukann yari' :
  st.mid_col('pasti mba kunti')
