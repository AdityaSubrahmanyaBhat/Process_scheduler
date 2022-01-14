import requests
from streamlit_lottie import st_lottie
import streamlit as st
import time

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

