import streamlit as st

# Titel van de app
st.title("Mijn Eerste Streamlit App")

# Voeg wat tekst toe aan de app
st.write("Dit is een eenvoudige Streamlit-app.")

# Voeg een invoerveld toe voor tekst
user_input = st.text_input("Voer wat tekst in:")

# Voeg een knop toe om een actie uit te voeren
if st.button("Klik om tekst te tonen"):
    st.write(f"Je hebt ingevoerd: {user_input}")

# # Voeg een grafiek toe
# import matplotlib.pyplot as plt
# import numpy as np

# data = np.random.randn(100)
# st.line_chart(data)

# Voeg een interactief element toe
selected_option = st.selectbox("Kies een optie:", ["Optie 1", "Optie 2", "Optie 3"])
st.write(f"Je hebt {selected_option} gekozen.")

# Voeg een bestandsuploadveld toe
uploaded_file = st.file_uploader("Upload een bestand", type=["txt", "csv"])
if uploaded_file is not None:
    st.write(f"Je hebt een bestand met de naam {uploaded_file.name} geüpload.")

# Voeg een sidebar toe
st.sidebar.header("Zijbalk")
st.sidebar.write("Dit is de zijbalk van de app.")

# Voeg een interactieve plot toe
import pandas as pd
import altair as alt

df = pd.DataFrame({
    'x': [1, 2, 3, 4, 5, 6],
    'y': [10, 20, 30, 40, 50, 60]
})

st.write("Een eenvoudige interactieve plot:")
c = alt.Chart(df).mark_circle().encode(
    x='x',
    y='y'
).interactive()
st.altair_chart(c, use_container_width=True)

# # Voeg een kaart toe
# import folium

# st.write("Een eenvoudige kaart:")
# m = folium.Map(location=[52.5200, 13.4050], zoom_start=10)
# st.write(m)

