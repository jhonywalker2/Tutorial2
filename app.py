import streamlit as st 
from PIL import Image

st.title("Esta es mi primera app en la nube")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales")

st.write("Yo, wasgood")
image = Image.open("Eminem.jpg")
st.image(image, caption="interfaces multimodales")

texto = st.text_input("Escribe algo" , "Este es mi texto") 
st.write("El texto escrito es", texto)

st.subheader("Ahora usamos 2 columnas")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Esta es la primera columna")
    st.write("Las interfaces multimodales mejoran la experiencia de usuario")
    resp = st.checkbox("estoy de acuerdo")
    if resp:
      st.write("Correcto!!")
with col2:
    st.subheader("Esta es la segunda columna")
    modo = st.radio("Que Modalidad es la principal interfaz", ("Visual", "auditiva", "tactil"))
    if modo == "visual":
        st.write("la vista es fundamental para tu interfaz") 
    if modo == "auditiva":
        st.write("La audicion es fundamental para tu interfaz")
    if modo == "tactil":
        st.write("El tacto es fundamental para tu interfaz")
    
