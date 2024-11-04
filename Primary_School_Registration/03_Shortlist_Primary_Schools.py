# Set up and run this Streamlit App
import streamlit as st
from logics.shortlist_school_handler import process_shortlist_criteria_function

# region <---------------- Password Check ---------------->

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# endregion <---------------- Password Check ---------------->

st.title("Shortlist Primary Schools")
st.write("We help you to shortlist Primary Schools that meet your needs here before actual registration.")

with st.form(key="form2", border=False):

    st.subheader("Tell us your criteria of your child's primary school")

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

    col1, col2, col3 = st.columns(3)
    
    with col1:
        nature = st.selectbox("Nature of School", ["", "CO-ED SCHOOL", "BOYS SCHOOL", "GIRLS SCHOOL"])

    with col2:
        mtl = st.selectbox("Mother Tongue Language", ["", "CHINESE", "CHINESE, MALAY, TAMIL"])

    with col3:
        location = st.selectbox("Location", ["", "NORTH", "SOUTH", "EAST", "WEST"])

    st.subheader("Your Question")

    st.markdown("""<style>.small-font {font-size:14px; color: green; font-style: italic}</style><p class='small-font'>Some of the commonly asked questions are:<br />- Which schools meet the above criteria?<br />- Which schools offer Hindi Language as a subject?<br />- Which schools offer Art as a subject?<br />- Which schools offer Artistic Gymnastics as a cca?<br />- Which schools possess barrier-free accessibility?</p>
    """, unsafe_allow_html=True)

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

    user_prompt_shortlist_0 = st.text_area(label="Enter your question here. Your question may take precedent over your above entries", value="Which schools meet the above criteria?", height=200)

    if nature == "" and mtl == "" and location == "":
        st.write("Your input: ", ":green[None]")
    else:
        st.write("Your input: ", nature, ",", mtl, ",", location, ",", user_prompt_shortlist_0)

    user_prompt_shortlist = user_prompt_shortlist_0.upper()

    if st.form_submit_button("Submit"):
        
        st.toast(f"User Input Submitted - {user_prompt_shortlist_0}")

        st.divider()

        df_schools_shortlisted_full_records, response_shortlist = process_shortlist_criteria_function(nature, mtl, location, user_prompt_shortlist)

        st.markdown(
        """
        <style>
            body {
                font-size:13px;
                overflow-wrap: break-word;
                text-wrap: balance;
            }
        </style>
        """,
            unsafe_allow_html=True,
        )

        st.markdown(df_schools_shortlisted_full_records)

        st.divider()

        st.write(response_shortlist)

        st.cache_data.clear()

