# Set up and run this Streamlit App
import streamlit as st

# region <---------------- Password Check ---------------->

from helper_functions.utility import check_password  

# Check if the password is correct.  
if not check_password():  
    st.stop()

# endregion <---------------- Password Check ---------------->

st.markdown("""
## 👨‍🎓 Welcome!
#### This application is about primary school registration in Singapore.

In Singapore, children ages three through six can attend either a public or private kindergarten or a childcare center. ECDA regulates programmes for children younger than 6 years old.
            
Whereas Ministry Of Education (MOE) regulates the educational programmes for age of 6 and beyond. The educational system of Singapore includes six years of primary school, followed by four to six years of secondary school, and one to three years of post-secondary school prior to university education. The curriculum for primary schools is common for all students in years one to four. For years five and six, students can take individual courses at the foundation or standard level. In year six, primary school students are to take the Primary School Leaving Examination (PSLE) which is the primary determinant of the stream they will join in secondary school. 

Primary school education is compulsory for all Singapore Citizens (SC) born after 1 January 1996 and living in Singapore, unless an exemption is granted. The starting age for Primary 1 (P1) is usually the year a child turns six years old, or the year they turn five if they were born on January 1. However, the cut-off date may vary slightly from year to year. 

Primary 1 (P1) registration is a process to register your child for mainstream primary schools in the following year. You can register your child in the P1 Registration Exercise if your child is born between "2 January of 6 years before the intended year of admission" and "1 January of 5 years before the intended year of admission". For example, you can register your child in the 2024 P1 Registration Exercise if your child is born between 2 January 2018 and 1 January 2019 (both dates inclusive).

The P1 registration process is also applicable to Permanent Residents (PR) and international students. For entry at Level P2 and above, a different process will be taken.

The admission timelines and application process of Special Education Schools are different from mainstream primary schools.

**In this application, you are able to:**
1. Clarify your doubts about the registration process to a mainstream primary school of Singapore, either entering at P1 or beyond P1, or for Singaporeans/PRs oridinarily residing in Singapore, returning Singaporeans/PRs or foreigners.
2. Shortlist primary schools that can meet your criteria.

Please begin your journey by clicking on the icons in the sidebar under the heading of "Featured Functions".
            
""", unsafe_allow_html=True)

