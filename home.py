import streamlit as st
import pandas

#Set webpage layout to wide
st.set_page_config(layout="wide")

content = """The Best Company"""
st.header(content)

content2="""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
    tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut
    aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit
    in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
    officia deserunt mollit anim id est laborum.
"""
st.write(content2)

content3 = """Our Team"""
st.subheader(content3)

#col, enpty_col, col1, enty_col1, col3 = st.columns([1.5, 0.4, 1.5, 0.4, 1.5])
col, col1, col3 = st.columns(3)

df = pandas.read_csv("data.csv")

with col:
    for index, row in df[:4].iterrows():
        #st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.subheader(f'{row["first name"].capitalize()} {row["last name"].capitalize()}')
        st.text(row["role"])
        st.image("images/" + row["image"])

with col1:
    for index, row in df[4:8].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.text(row["role"])
        st.image("images/" + row["image"])

with col3:
    for index, row in df[8:].iterrows():
        st.subheader(row["first name"].capitalize() + " " + row["last name"].capitalize())
        st.text(row["role"])
        st.image("images/" + row["image"])

