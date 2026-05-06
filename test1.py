import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="My Streamlit Page",
    page_icon=":robot:",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremely.com/help',
        'Report a bug': "https://www.extremely.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Welcome to My First Streamlit App!")

st.header("A Simple Web Page Example")

st.write("This is a paragraph of text. You can use Markdown for **bold** text, *italic* text, and even `code`.")

st.subheader("Interactive Elements")

name = st.text_input("What's your name?")
if name:
    st.write(f"Hello, {name}!")

age = st.slider("How old are you?", 0, 100, 25)
st.write(f"You are {age} years old.")

option = st.selectbox(
    'Which number do you like best?',
    (1, 2, 3))

st.write('You selected:', option)

# Fix for StreamlitDuplicateElementId error
show_secret = st.checkbox('Show a secret message')
if show_secret:
    st.success("You found the secret!")

st.button('Click me')
if st.button('Click me'):
    st.info('Button clicked!')

st.subheader("Displaying Data")

data = {'Column A': [1, 2, 3, 4],
        'Column B': ['Apple', 'Banana', 'Cherry', 'Date']}
df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("About This App")
st.markdown("This app demonstrates basic Streamlit features. To run this locally, save the code as `app.py` and execute `streamlit run app.py` in your terminal.")
