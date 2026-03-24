import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ternary

st.title("Ternäres Diagramm aus Excel")

# Datei Upload
uploaded_file = st.file_uploader("Excel-Datei hochladen", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)

    st.write("Daten Vorschau:")
    st.dataframe(df)

    # Spalten auswählen
    col1 = st.selectbox("Spalte A", df.columns)
    col2 = st.selectbox("Spalte B", df.columns)
    col3 = st.selectbox("Spalte C", df.columns)

    if st.button("Diagramm erstellen"):

        a = df[col1]
        b = df[col2]
        c = df[col3]

        total = a + b + c
        a = a / total
        b = b / total
        c = c / total

        points = list(zip(a, b, c))

        scale = 1
        figure, tax = ternary.figure(scale=scale)

        tax.scatter(points, marker='o', color='blue')

        tax.left_axis_label(col1)
        tax.right_axis_label(col2)
        tax.bottom_axis_label(col3)

        tax.gridlines(multiple=0.1)
        tax.ticks(axis='lbr', multiple=0.1)
        tax.clear_matplotlib_ticks()

        st.pyplot(figure)
