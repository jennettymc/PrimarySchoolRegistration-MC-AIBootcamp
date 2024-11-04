import streamlit as st
import pandas as pd
import json

# region <---------------- Password Check ---------------->

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# endregion <---------------- Password Check ---------------->


st.title("Methodology")

st.image("./images/Methodolody.png")
