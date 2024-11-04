# Set up and run this Streamlit App
import streamlit as st
from logics.user_query_handler import process_user_message_function

# region <---------------- Password Check ---------------->

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# endregion <---------------- Password Check ---------------->


st.title("Primary School Registration")
st.write("Ask any questions you have about the procedures for registering a primary school in Singapore.") 

with st.form(key="form1", border=False):

    st.subheader("Help us to understand your situation")

    st.markdown(
    """
    <style>
        div[data-baseweb="select"] > div {
            background-color: #dceec8;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        
        nationality = st.selectbox("1: What is the nationality of your child?", ["","Singapore Citizen or Permanent Resident currently ordinarily residing in Singapore", "Singapore Citizen or Permanent Resident returning from overseas", "Non-Singapore Citizen or Non-Singapore Permanent Resident"])

        sped = st.selectbox("4: Does your child need to be enrolled into a Special Education School funded by Singapore Government?", 
            ["", 
            "No, or none of the options below", 
            "Yes, diagnosed to have 'Autism spectrum disorder (ASD) with no intellectual impairment'", 
            "Yes, diagnosed to have 'Autism spectrum disorder (ASD) with intellectual impairment'", 
            "Yes, diagnosed to have 'Mild intellectual disability (MID)'",
            "Yes, diagnosed to have 'Moderate to severe intellectual disability (MSID)'",
            "Yes, diagnosed to have 'Multiple disabilities (MD)'",
            "Yes, diagnosed to have 'Sensory impairment'"
            ]
    )

    with col2:
    
        level = st.selectbox("2: Which level is your child enrolling for?", ["", "Primary 1", "Primary 2", "Primary 3", "Primary 4", "Primary 5", "Primary 6"])

        age = st.selectbox("3: What will be the age of your child in the intended year of admission?", ["", "6", "7", "8", "9", "10", "11", "12", "13", "14"])


    st.subheader("Your Question")

    st.markdown("""<style>.small-font {font-size:14px; color: green; font-style: italic}</style><p class='small-font'>Some of the commonly asked questions are:<br />- How to register for a primary school in Singapore based on the above entries?<br />- Could you list down the different phases of P1 Registration Process?<br />- How to register my second child for the same primary school that my first child is currently studying in?<br />- How to register my child for the primary school that my child has attended MOE Kindergarten located in the school?<br />- How to register my child for the primary school that I graduated from?<br />- We are a Singaporean family returning to Singapore. How to register my child for a primary school?<br />- How distance affects priority admission?<br />- How long do we need to stay at the address used for my child's registration?</p>
    """, unsafe_allow_html=True)
    
    # st.caption(":green[Some of the commonly asked questions are:]")
    # st.caption(":green[> How to register for a primary school in Singapore based on the above entries?]")
    # st.caption(":green[> Could you list down the different phases of P1 Registration Process?]")
    # st.caption(":green[> How to register my second child for the same primary school that my first child is currently studying in?]")
    # st.caption(":green[> How to register my child for the primary school that my child has that my child has attended MOE Kindergarten located in the school?]")
    # st.caption(":green[> How to register my child for the primary school that I graduated from?]")
    # st.caption(":green[> We are a Singaporean family returning to Singapore. How to register my child for a primary school?]")
    # st.caption(":green[> How distance affects priority admission?]")
    # st.caption(":green[> How long do we need to stay at the address used for my child's registration?]")


    st.markdown(
    """
    <style>
        .stTextArea [data-baseweb=base-input] {
            background-color: #dceec8;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )

    user_prompt = st.text_area(label="Enter your question here. Your question may take precedent over your above entries", value="How to register for a primary school in Singapore based on the above entries?", height=200)

    # user_prompt = st.text_area(label="Enter your question here. Your question may take precedent over your above entries", height=200)

    if nationality == "" and level == "" and age == "" and sped == "":
        st.write("Your input: ", ":green[None]")
    else:
        st.write("Your input: ", nationality, ",", level, ",", age, ",", sped, ",", user_prompt)
    
    if st.form_submit_button("Submit"):

        st.toast(f"User Input Submitted - {user_prompt}")

        st.divider()

        response = process_user_message_function(nationality, level, age, sped, user_prompt)

        st.write(response)
        
    
