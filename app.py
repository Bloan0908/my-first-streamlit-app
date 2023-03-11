import streamlit as st
import scikit-learn
import plotly
a=st.number_input('Tham số a')
b=st.number_input('Tham số b')
st.title('GIẢI PHƯƠNG TRÌNH BẬC NHẤT')
st.balloons()
if st.button('Giải'):
  st.write('Phương trình có 1 nghiệm',-b/a)
