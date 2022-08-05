


import streamlit as st
import os

def file_upload():
    data_file = st.file_uploader('Select an audio file')
    if data_file is not None:
        file_name = data_file.name.split('.')
        return file_name[0].title()

st.write('The predicted sound is `%s`' % file_upload())






