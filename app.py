import streamlit as st
import sklearn #thu vien sklearn luu day du la scikit-learn
import plotly
a=st.number_input('Tham số a')
b=st.number_input('Tham số b')
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
st.balloons()
if st.button('Giải'):
  if (a==0 && b==0): st.write('Phuong trinh co vo so nghiem')
  if (a==0 && b><0): st.write('Phuong trinh vo nghiem')
  else: st.write('Phương trình có 1 nghiệm',-b/a)
