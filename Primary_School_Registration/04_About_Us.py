import streamlit as st

# region <---------------- Password Check ---------------->

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# endregion <---------------- Password Check ---------------->


st.title("About this App")

st.markdown("""
    
    :blue[**Project scope:**] This is a capstone project for GovTech's AIBootcamp Jul/Oct 2024. The scope of this project is to develop a web-based application that enables public to interact with publicly available information regarding Primary School Registration with Ministry of Education. The requirement of this capstone project is to build in at least two featured use cases.
    
    :blue[**Objectives:**] The application takes in users' specific information about their child and their considerations for choosing primary schools, consolidates information from multiple sources, and present relevant information to the users. This application is built in line with MOE's advocate that "Every school is a good school". By filtering out the factors that meet the parents' and their children's needs, the information help parents in logically selecting primary schools that are suitable for their child/children. It also provides an one-stop solution for all different nationalities, different entry levels and special condition(s) of the child/children, which is currently not available on any websites. As the current SchoolFinder function is also not able to read in multiple factors concurrently, our "Shortlist: Primary School" function makes use of LLM's capabilities to enable a more responsive approach.
            
    :blue[**Data sources:**] The information used in the application is taken from various MOE (on P1 Registration, Returning Singaporeans, International Students, Special Needs), and MOE's data on "School Directory and Information".
            
    :blue[**Features:**] There are two main features. The <u>first feature</u> is to answer questions about the procedures for registering to a Singapore's mainstream primary school.
            The <u>second feature</u> is to help parents in shortlisting some primary schools that can meet their specific needs.
            
    """, unsafe_allow_html=True)

