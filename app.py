import streamlit as st 
from PIL import Image

st.title("Esta es mi primera app en la nube")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")

st.write("Yo, wasgood")
image=Image.open("Gus.jpg")
st.image(image, caption="interfaces multimodales")
