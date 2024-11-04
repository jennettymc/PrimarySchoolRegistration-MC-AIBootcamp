# Set up and run this Streamlit App
import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="wide",
    page_title="Primary School Registration - Main Page"
)
# endregion <--------- Streamlit App Configuration --------->

# region <---------------- Password Check ---------------->

from Primary_School_Registration.helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# endregion <---------------- Password Check ---------------->

st.markdown(
"""
    <style>
        [data-testid="stImage"] {
            justify-content: center;
        }
    </style>
""",
    unsafe_allow_html=True,
)

st.image("./Primary_School_Registration/images/Header_3a.png", use_column_width="auto")

with st.expander("Disclaimer"):
    st.markdown("""
        
    **IMPORTANT NOTICE:** This web application is a prototype developed for **educational purposes only**. The information provided here is **NOT intended for real-world usage** and should not be relied upon for making any decisions, especially those related to financial, legal, or healthcare matters.

    **Furthermore, please be aware that the LLM may generate inaccurate or incorrect information. You assume full responsibility for how you use any generated output.**

    Always consult with qualified professionals for accurate and personalized advice.
                    
    """, unsafe_allow_html=True)


pages = {
    "Welcome":[
        st.Page("./Primary_School_Registration/01_Home.py", title="🏠 Home"),
    ],
    "Featured Functions":[
        st.Page("./Primary_School_Registration/02_Ask_About_Registration_Procedures.py", title="1️⃣ Ask: Primary School Registration"),
        st.Page("./Primary_School_Registration/03_Shortlist_Primary_Schools.py", title="2️⃣ Shortlist: Primary Schools"),
    ],
    "About this Application":[
        st.Page("./Primary_School_Registration/04_About_Us.py", title="🖼️ About Us"),
        st.Page("./Primary_School_Registration/05_Methodology.py", title="🛠️ Methodology"),
    ],
}

st.markdown(
"""
    <style>
        [data-testid="stSidebar"] {
            background: #dceec8;
        }
    </style>
""",
    unsafe_allow_html=True,
)


pg = st.navigation(pages)
pg.run()


