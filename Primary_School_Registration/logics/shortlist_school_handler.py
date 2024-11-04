import pandas as pd
from helper_functions import llm
from langchain_openai import ChatOpenAI

from langchain.agents.agent_types import AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI

# def format_parser_output(parser_output: Dict[str, Any]) -> None:
#     for key in parser_output.keys():
#         parser_output[key] = parser_output[key].to_dict()
#     return pprint.PrettyPrinter(width=4, compact=True).pprint(parser_output)

def identify_schools(nature, mtl, location, user_prompt_shortlist):
    
    df_school_details_3 = pd.read_excel('./data/All information of schools_Primary.xlsx', index_col=0)

    if nature != "":
        df_school_details_2 = df_school_details_3.loc[df_school_details_3['nature'] == nature]
    else:
        df_school_details_2 = df_school_details_3

    if mtl != "":
        df_school_details_1 = df_school_details_2.loc[df_school_details_2['mothertonguelanguages'] == mtl]
    else:
        df_school_details_1 = df_school_details_2

    if location != "":
        df_school_details = df_school_details_1.loc[df_school_details_1['zone'] == location]
    else:
        df_school_details = df_school_details_1

    return df_school_details


def extract_all_records(df_school_details, user_prompt_shortlist):

    agent = create_pandas_dataframe_agent(
        ChatOpenAI(temperature=0, model="gpt-4o-mini"),
        df_school_details,
        verbose=True,
        agent_type=AgentType.OPENAI_FUNCTIONS,
        allow_dangerous_code=True,
    )

    df_query = f"Retrieve the row of records from that can answer {user_prompt_shortlist}. Output must be a table."

    df_schools_shortlisted_full_records_1 = agent.invoke(df_query)
    df_schools_shortlisted_full_records = df_schools_shortlisted_full_records_1['output'].split(":\n")[-1]

    return df_schools_shortlisted_full_records


def generate_response_based_on_shortlist_details(nature, mtl, location, df_schools_shortlisted_full_records, user_prompt_shortlist):
    delimiter = "####"

    system_message = f"""
    Wait for 60 seconds for {df_schools_shortlisted_full_records} to be ready before you begin.

    You have been provided with a set of shortlisted schools called {df_schools_shortlisted_full_records}.
    Please read the {df_schools_shortlisted_full_records} and answer the user's query {user_prompt_shortlist} based on the content of the {df_schools_shortlisted_full_records}. 
    
    The user query will be delimited with a pair {delimiter}.

    Follow these steps to answer the user's query.

    Step 1:{delimiter} Use the relevant information in {df_schools_shortlisted_full_records} \
    to generate the answer for the user's query called {user_prompt_shortlist}.
    You must only rely on the facts or information in {df_schools_shortlisted_full_records} and the child's {nature}, {mtl}, and {location} provided by the user.

    Step 2:{delimiter}: Answer the user in a friendly and confident tone.
    Make sure the statements are factually accurate.
    Your response should be comprehensive and informative.
    Start your response with a summary of the {nature}, {mtl} and {location} provided by the user, \
    complete with details and the key features of the shortlisted schools.
    Use Neural Linguistic Programming to construct your response.

    After 60 seconds, only if {df_schools_shortlisted_full_records} is empty, \
    response to the user politely that there are no schools that meet the user's needs, \
    and advise the user to adjust the criteria or query.
    If {df_schools_shortlisted_full_records} is not empty, you must provide a summary of the shortlisted schools.
            
    Use the following format:
    Step 1:{delimiter} <step 1 know your inputs>
    Step 2:{delimiter} <step 2 response to user>

    Make sure to include {delimiter} to separate every step.
    """

    messages =  [
        {'role':'system',
         'content': system_message},
        {'role':'user',
         'content': f"{delimiter}{user_prompt_shortlist}{delimiter}"},
    ]

    response_shortlist = llm.get_completion_by_messages(messages)
    response_shortlist = response_shortlist.split(delimiter)[-1]
    return response_shortlist


def process_shortlist_criteria_function(nature, mtl, location, user_prompt_shortlist):

    # Process 1: If Schools are found, look them up
    df_school_details = identify_schools(nature, mtl, location, user_prompt_shortlist)

    # Process 2: Extract all records of shortlisted schools
    df_schools_shortlisted_full_records = extract_all_records(df_school_details, user_prompt_shortlist)

    # Process 3: Generate Response based on User Prompt for shortlisting schools
    response_shortlist = generate_response_based_on_shortlist_details(nature, mtl, location, df_schools_shortlisted_full_records, user_prompt_shortlist)

    return df_schools_shortlisted_full_records, response_shortlist