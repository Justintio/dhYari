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
  lanjut = ['ga', 'lanjut']
  lanjut2 = st.selectbox('Lanjut ga ? ', lanjut) 
  if lanjut2 == 'ga' :
    st.title('yaudin')
  if lanjut2 == 'lanjut' :
    st.title('a')
    st.title('b')
    st.title('c')
    st.title('d')
    st.title('e')
    st.title('f')
    st.title('g')
    st.title('h')
    st.title('i lop u veri veri much')
    st.title('hahaha dah coba yang lain sana !')
elif nama=='bukann yari' :
  st.title('pasti mba kunti')
  image = Image.open('abc.jpg')
