import streamlit as st
from PIL import Image


st.sidebar.title('creator')
st.sidebar.header('by : Justin Tio')
image10 = Image.open('foto.jpg')
st.sidebar.image(image10)

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
    image3 = Image.open('11.jpg')
    st.image(image3)
    st.title('hahaha dah coba yang lain sana !')
    
elif nama=='bukann yari' :
  st.title('pasti mba kunti')
  st.title('bwaaa')
  image = Image.open('abc.jpg')
  st.image(image)
  kaget = ['pilih', 'kaget', 'engga']
  kaget2 = st.selectbox('kaget ga ? ', kaget)
  if kaget2 == 'pilih' :
    st.title(' ')
  if kaget2 == 'kaget' :
    st.title('ututuu kasian bgt kaget')
  if kaget2 == 'engga' :
    st.title('bwaa lagi')
    image2 = Image.open('def.jpg')
    st.image(image2)
    st.title('ga kaget kan wkwk')
    st.title('udah deh kasian ntar gabisa bobo :D')
    st.title('mwahhh')
    image4 = Image.open('22.jpg')
    st.image(image4)
    
elif nama=='kesayangan juju' :
  sayang = ['pilih', 'sayang', 'no']
  sayang2 = st.selectbox('beneran sayang ? ', sayang)
  if sayang2 == 'no' :
    st.title('pundung setaun')
    image5 = Image.open('33.jpg')
    st.image(image5)
  if sayang2 == 'sayang' :
    st.title('cie sayang cie')
    tahun = st.slider("seberapa sayang emang? (harus 100 titik)", min_value=0, max_value=100)
    if tahun == 100 :
       st.title('hehehe gitudong')
       st.title('karena gatau disini mau diisi apa kita liat2 poto aja kaliyak')
       foto1 = Image.open('1.jpg')
       st.image(foto1)
       st.write('cis baru jadian yahahha, macam kopi susu lagi fak')
       st.title(' ')
      
       foto2 = Image.open('2.jpg')
       st.image(foto2)
       st.write('udah rada tampan dan putih ni aku')
       st.title(' ')
      
       foto3 = Image.open('3.jpg')
       st.image(foto3)
       st.write('cie mau sama bapack bapack')
       st.title(' ')
      
       foto4 = Image.open('4.jpg')
       st.image(foto4)
       st.write('tijel tp lucu')
       st.title(' ')
      
       foto5 = Image.open('5.jpg')
       st.image(foto5)
       st.write('ini juga lucu kamu')
       st.title(' ')      
      
       foto6 = Image.open('6.jpg')
       st.image(foto6)
       st.write('ikut ikut bajunya')
       st.title(' ')
      
       foto7 = Image.open('7.jpg')
       st.image(foto7)
       st.write('nih bocah dah bucin ae')
       st.title(' ')
      
       foto8 = Image.open('8.jpg')
       st.image(foto8)
       st.write('apa kamu')
       st.title(' ')
      
       foto9 = Image.open('9.jpg')
       st.image(foto9)
       st.write('nyosor wae sukanya')
       st.title(' ')
      
       foto10 = Image.open('10.jpg')
       st.image(foto10)
       st.write('eits bocil gemoy lewat')
       st.title(' ')      
     
       foto11 = Image.open('11.11.jpg')
       st.image(foto11)
       st.write('kucing')
       st.title(' ')
        
       foto12 = Image.open('12.jpg')
       st.image(foto12)
       st.write('bwa bocil lewat lagi')
       st.title(' ')    
        
       foto13 = Image.open('13.jpg')
       st.image(foto13)
       st.write('kita dah cakep maksimal ini')
       st.title(' ')   
        
       foto14 = Image.open('14.jpg')
       st.image(foto14)
       st.write('maksimal +++')
       st.title(' ')   
        
       foto15 = Image.open('15.jpg')
       st.image(foto15)
       st.write('dan ini tadi pagi')
       st.title('the end')
       st.title(' ')          
       st.title('udah capek sumpa')
    
    
elif nama=='arip' : 
   st.title('cih cingkuh sama arip')
    
