# df dependencies
import os
import dialogflow
from google.api_core.exceptions import InvalidArgument


GOOGLE_AUTHENTICATION_FILE_NAME = "df.json"
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'test.json'

DIALOGFLOW_PROJECT_ID = 'bwu-ppsb'
DIALOGFLOW_LANGUAGE_CODE = 'en'
SESSION_ID = 'random'

# initialiazing chatbot
session_client = dialogflow.SessionsClient()
session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

def get_chatbot_reply(query):
    text_to_be_analyzed = query
     
    text_input = dialogflow.types.TextInput(text=text_to_be_analyzed, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(session=session, query_input=query_input)
        return str(response.query_result.fulfillment_text)
    except InvalidArgument:
        return "Please give an input"

if __name__ == "__main__":
    query = input()
    print(get_chatbot_reply(query))