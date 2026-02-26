import streamlit as st 
from PIL import Image

st.title("Esta es mi primera app en la nube")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")

st.write("Yo, wasgood")
image = Image.open("Eminem.jpg")
st.image(image, caption="interfaces multimodales")

texto = st.text_input("Escribe algo" , "Este es mi texto") 
st.write("El texto escrito es", texto)
