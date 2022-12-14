import streamlit as st
import data

# https://docs.streamlit.io/library/api-reference?highlight=beta_page_config#streamlit.set_page_config

# st.set_page_config(page_title='your_title', layout = 'wide', initial_sidebar_state = 'auto') #page_icon = favicon, 
st.set_page_config(layout = 'wide')

st.title("Analysis Background")

# st.write(st.session_state['test'])