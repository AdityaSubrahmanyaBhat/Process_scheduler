import streamlit as st
import pandas as pd
import input

def main():
    st.set_page_config(page_title='Process Scheduler',  initial_sidebar_state = 'auto')
    input.input_form()

if __name__=='__main__':
    main()