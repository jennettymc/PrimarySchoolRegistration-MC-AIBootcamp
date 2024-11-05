from helper_functions import llm
#from langchain_community.document_loaders import SeleniumURLLoader
from langchain_community.document_loaders import UnstructuredURLLoader
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service as ChromeService
#from webdriver_manager.chrome import ChromeDriverManager

#options = webdriver.ChromeOptions()
#driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

def load_url_based_on_user_prompt_function(sped):
    if "Yes" in sped:
        urls = [
            "https://www.moe.gov.sg/special-educational-needs",
            "https://www.moe.gov.sg/special-educational-needs/sped-schools",
            "https://www.moe.gov.sg/special-educational-needs/apply",
            "https://www.moe.gov.sg/special-educational-needs/understand",
            "https://www.moe.gov.sg/-/media/files/special-education/special-education-sped-schools-admission-timelines.pdf",
        ]
    else:
        urls = [
            "https://www.moe.gov.sg/returning-singaporeans",
            "https://www.moe.gov.sg/returning-singaporeans/primary",
            "https://www.moe.gov.sg/returning-singaporeans/assured-school-placement",
            "https://www.moe.gov.sg/-/media/files/returning-singaporeans/returning-singaporean-information-sheet.pdf",
            "https://www.moe.gov.sg/international-students/studying-in-singapore",
            "https://www.moe.gov.sg/international-students/admission",
            "https://www.moe.gov.sg/international-students/aeis",
            "https://www.moe.gov.sg/international-students/s-aeis",
            "https://www.moe.gov.sg/primary/p1-registration/international-students",
            "https://www.moe.gov.sg/primary/p1-registration/international-students/indicate-interest",
            "https://www.moe.gov.sg/-/media/files/primary/p1-registration/2024-p1-ioi-formsg-user-guide.pdf",
            "https://www.moe.gov.sg/primary/p1-registration/international-students/receive-offer-letter",
            "https://www.moe.gov.sg/primary",
            "https://www.moe.gov.sg/primary/p1-registration",
            "https://www.moe.gov.sg/primary/p1-registration/how-to-choose-a-school",
            "https://www.moe.gov.sg/primary/p1-registration/distance",
            "https://www.moe.gov.sg/primary/p1-registration/home-address",
            "https://www.moe.gov.sg/primary/p1-registration/registration-phases-key-dates",
            "https://www.moe.gov.sg/primary/p1-registration/registration-phases-key-dates?pt=1",
            "https://www.moe.gov.sg/primary/p1-registration/registration-phases-key-dates?pt=2A",
            "https://www.moe.gov.sg/primary/p1-registration/registration-phases-key-dates?pt=2B",
            "https://www.moe.gov.sg/primary/p1-registration/registration-phases-key-dates?pt=2C",
            "https://www.moe.gov.sg/primary/p1-registration/registration-phases-key-dates?pt=2C%20Supplementary",
            "https://www.moe.gov.sg/primary/p1-registration/cap-on-pr-intake",
            "https://www.moe.gov.sg/primary/p1-registration/understand-balloting",
            "https://www.moe.gov.sg/primary/p1-registration/past-vacancies-and-balloting-data",
            "https://www.moe.gov.sg/primary/p1-registration/how-to-register",
            "https://www.moe.gov.sg/primary/p1-registration/vacancies-and-balloting",
            "https://www.moe.gov.sg/primary/p1-registration/results",
            "https://www.moe.gov.sg/primary/p1-registration/report-to-school",
            "https://www.moe.gov.sg/primary/p1-registration/student-care-centres",
            "https://www.moe.gov.sg/primary/p1-registration/transition-to-primary",
            "https://www.moe.gov.sg/faq?categoryid=76037F9F568F46A7AA80EFDCE9AB23CD",
        ]

    #loader = SeleniumURLLoader(urls=urls)

    loader = UnstructuredURLLoader(urls=urls)

    articles = loader.load()

    return articles

def generate_response_based_on_user_prompt_function(nationality, level, age, sped, articles, user_prompt):
    delimiter = "####"

    system_message = f"""
    Follow these steps to answer the user's queries.

    You have been provided with a set of articles.
    Please read the articles and answer the following question based on the content of the articles. 
        
    The user query will be delimited with a pair {delimiter}.
        
    Step 1:{delimiter} If the user is asking about registration process for a primary school in Singapore, \
    understand the nationality, level, age and sped provided by the user in variable names as listed below.
    {nationality},
    {level},
    {age},
    {sped}

    After that, also understand {user_prompt} and identify relevant information in following data by the name of articles.
    If the {user_prompt} is empty, assume that the user's question is "how to register for a primary school?".

    All available information about primary school registration is shown in the data below:
    {articles}

    Step 2:{delimiter} Use the relevant information on primary school registration \
    generate the answer for the user's query.
    You must only rely on the facts or information in the articles and the child's {nationality}, {level}, {age}, and {sped} entered by the user.

    The following sequence to prepare your answer should be taken.

    First, check the {sped} entry provided by the user.
    If {sped} starts with a "Yes", you must refer to articles related to "special educational needs".
    This condition takes precedent over any other conditions.
        
    Second, please highlight to the user if the child's {age} is 2 years above the standard age for the {level} that their child is registering for, \
    or below the standard age for the {level} that their child is registering for, \
    according to the conditions stated below.    
    {age} is more than 8 and less than 6 if {level} is"Primary 1", \
    {age} is more than 9 and less than 7 if {level} is "Primary 2", \
    {age} is more than 10 and less than 8 if {level} is "Primary 3", \
    {age} is more than 11 and less than 9 if {level} is "Primary 4", \
    {age} is more than 12 and less than 10 if {level} is "Primary 5", \
    {age} is more than 13 and less than 11 if {level} is "Primary 6".

    Third, if {level} is "Primary 6", inform user that new students are generally not admitted at "Primary 6".
            
    Fourth, check the {nationality} entry provided by the user.
    If {nationality} is stated as "Singapore Citizen or Permanent Resident returning from overseas", you must refer to articles related to "returning-singaporeans" and "p1-registration".
    If {nationality} is stated as "Non-Singapore Citizen or Non-Singapore Permanent Resident", you must refer to articles related to "international-students" and "p1-registration".

    Fifth, if {level} is not "Primary 1", please do not take reference from "P1 registration process".
    If {level} is "Primary 1" and {sped} starts with "No", please quote the relevant Phase of "P1 registration process" where applicable.

    Sixth, if your recommendation is for user to find a school, \
    do recommend user to refer to the SchoolFinder tool which is available on the Ministry of Education's website.

    Your response should be as detail as possible and \
    include information that is useful for user to better understand the registration process.

    Step 3:{delimiter}: Answer the user in a friendly tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative to help the \
    the users to understand the registration steps.
    Start your response with a summary of the child's nationality, level, age, and sped entered by the user, \
    complete with details including the steps involved in registering for a school, how to apply for a primary school, \
    where to apply, timeline of application, the different phases of registration and the documents to be submitted.
    Use Neural Linguistic Programming to construct your response.

    After 60 seconds, if you are not able to find the information related to the user's query from the provided articles, \
    please response to the user politely that you are sorry that you do not have the relevant information to provide an answer, \
    provide the name of the official authorities and advise the user to contact the official authorities. 
            
    Use the following format:
    Step 1:{delimiter} <step 1 know your inputs>
    Step 2:{delimiter} <step 2 reasoning>
    Step 3:{delimiter} <step 3 response to user>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_prompt}{delimiter}"},
    ]

    response_to_user = llm.get_completion_by_messages(messages)
    response_to_user = response_to_user.split(delimiter)[-1]
    return response_to_user


def process_user_message_function(nationality, level, age, sped, user_prompt):
    delimiter = "```"

    # Process 1: Download URL based on sped selection
    articles = load_url_based_on_user_prompt_function(sped)

    # Process 2: Generate Response based on User Prompt for Primary School Registration
    reply = generate_response_based_on_user_prompt_function(nationality, level, age, sped, articles, user_prompt)

    return reply
