import os
import openai
import json
def clean_artifact_list(artifacts):
    """
    Cleans a list of artifact strings by removing the leading numbers and trailing punctuation,
    while preserving internal hyphens.
    
    Parameters:
    artifacts (list): A list of strings representing artifacts, each with a leading number and possible trailing punctuation.
    
    Returns:
    list: A cleaned list of artifact strings without leading numbers and trailing punctuation.
    """
    cleaned_artifacts = []
    for artifact in artifacts:
        # Remove the leading number
        cleaned_artifact = ' '.join(artifact.split()[1:])  # Remove the number and keep the rest
        # Remove any trailing punctuation
        cleaned_artifact = cleaned_artifact.strip('.,;:!?')
        cleaned_artifacts.append(cleaned_artifact)

    return cleaned_artifacts

def extract_room_and_artifacts(description):
    """
    Extracts and returns the room description and a list of artifacts from the given string,
    keeping the original format of the artifacts (without adding numbers).
    
    Parameters:
    description (str): A string containing the room description and a list of artifacts.
    
    Returns:
    tuple: A tuple where the first element is a string of the room description and the second element
           is a list of artifacts as they appear in the input string.
    """
    # Split the description into room description and artifacts
    parts = description.split('Artifacts:')

    # The room description is the first part
    room_desc = parts[0].strip()

    # The artifacts list is the second part, remove any leading/trailing whitespace or newlines
    artifacts = parts[1].strip().split('\n') if len(parts) > 1 else []

    # Return a tuple of the room description and the artifacts list
    return room_desc, artifacts

# Adjusted function to extract the character after "Answer: " and then trim the string from "Answer"
# def extract_and_trim_from_answer(s):
#     # Find the index of "Answer: " in the string
#     answer_keyword = "Answer: "
#     answer_index = s.find(answer_keyword)

#     # Extracting the character after "Answer: " if found
#     if answer_index != -1 and answer_index + len(answer_keyword) < len(s):
#         extracted_char = s[answer_index + len(answer_keyword)].strip()
#     else:
#         extracted_char = None

#     # Trimming the string from "Answer"
#     s = s[:answer_index].strip() if answer_index != -1 else s

#     return extracted_char, s

def getArtifactDesc(artifact):
    openai.api_type = "azure"
    openai.api_key = os.environ['OPENAI_API_KEY']
    openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
    openai.api_version = '2023-03-15-preview'
    prompt = "write me a short description of an abandoned house's" + artifact
    try:
        response = openai.ChatCompletion.create(
            engine='gpt-4',
            messages=[
                {"role": "system", "content": "You generate a 30 word description for an escape house artifact."},
                {"role": "user", "content": prompt},
            ]
        )

        # print the response
        x = (response['choices'][0]['message']['content'])
        return x

    #error checks
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")

    except openai.error.AuthenticationError as e:
        # Handle Authentication error here, e.g. invalid API key
        print(f"OpenAI API returned an Authentication Error: {e}")

    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")

    except openai.error.InvalidRequestError as e:
        # Handle connection error here
        print(f"Invalid Request Error: {e}")

    except openai.error.RateLimitError as e:
        # Handle rate limit error
        print(f"OpenAI API request exceeded rate limit: {e}")

    except openai.error.ServiceUnavailableError as e:
        # Handle Service Unavailable error
        print(f"Service Unavailable: {e}")

    except openai.error.Timeout as e:
        # Handle request timeout
        print(f"Request timed out: {e}")

    except:
        # Handles all other exceptions
        print("An exception has occured.")


def getRoomDesc(room, numberartifacts):
    openai.api_type = "azure"
    openai.api_key = os.environ['OPENAI_API_KEY']
    openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
    openai.api_version = '2023-03-15-preview'
    prompt = "write me a short description of an abandoned house's" + room + " foyer noting " + str(numberartifacts) + " specific thing(s) that is going to be used to hide clues and tools for the same game and return a list of comma seperated artifact names. Use hyphens for a artifact that needs multiple words and always use numbers to index each artifact. Start with /'Artifacts:/', no quotes. Each artifact on a new line. Still print the room desc 1st and dont start with /'Room Description/'"
    try:
        response = openai.ChatCompletion.create(
            engine='gpt-4',
            messages=[
                {"role": "system", "content": "You generate a description for an escape house."},
                {"role": "user", "content": prompt},
            ]
        )

        # print the response
        x = (response['choices'][0]['message']['content'])
        y,z = extract_room_and_artifacts(x)
        return y, clean_artifact_list(z)

    #error checks
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")

    except openai.error.AuthenticationError as e:
        # Handle Authentication error here, e.g. invalid API key
        print(f"OpenAI API returned an Authentication Error: {e}")

    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")

    except openai.error.InvalidRequestError as e:
        # Handle connection error here
        print(f"Invalid Request Error: {e}")

    except openai.error.RateLimitError as e:
        # Handle rate limit error
        print(f"OpenAI API request exceeded rate limit: {e}")

    except openai.error.ServiceUnavailableError as e:
        # Handle Service Unavailable error
        print(f"Service Unavailable: {e}")

    except openai.error.Timeout as e:
        # Handle request timeout
        print(f"Request timed out: {e}")

    except:
        # Handles all other exceptions
        print("An exception has occured.")
    

# def getQuestion(topic, difficulty, age):
#     openai.api_type = "azure"
#     openai.api_key = os.environ['OPENAI_API_KEY']
#     openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
#     openai.api_version = '2023-03-15-preview'
#     if(len(topic) == 0):
#         topic = "random trivia"
#     prompt = "Give me a question about " + topic + " that is " + difficulty + " and is appropriate for ages " + age + " and up."
#     try:
#         response = openai.ChatCompletion.create(
#             engine='gpt-4',
#             messages=[
#                 {"role": "system", "content": "You generate multiple choice (A-D) questions for a topic and also give the right letter for the correct answer. Dont use the word correct. Just say Answer: A, B, C, or D."},
#                 {"role": "user", "content": prompt},
#             ]
#         )

#         # print the response
#         x = (response['choices'][0]['message']['content'])
#         return extract_and_trim_from_answer(x)

#     #error checks
#     except openai.error.APIError as e:
#         # Handle API error here, e.g. retry or log
#         print(f"OpenAI API returned an API Error: {e}")

#     except openai.error.AuthenticationError as e:
#         # Handle Authentication error here, e.g. invalid API key
#         print(f"OpenAI API returned an Authentication Error: {e}")

#     except openai.error.APIConnectionError as e:
#         # Handle connection error here
#         print(f"Failed to connect to OpenAI API: {e}")

#     except openai.error.InvalidRequestError as e:
#         # Handle connection error here
#         print(f"Invalid Request Error: {e}")

#     except openai.error.RateLimitError as e:
#         # Handle rate limit error
#         print(f"OpenAI API request exceeded rate limit: {e}")

#     except openai.error.ServiceUnavailableError as e:
#         # Handle Service Unavailable error
#         print(f"Service Unavailable: {e}")

#     except openai.error.Timeout as e:
#         # Handle request timeout
#         print(f"Request timed out: {e}")

#     except:
#         # Handles all other exceptions
#         print("An exception has occured.")

def extract_and_remove_from_answer(s):
    # Find the index of "Answer: " in the string
    answer_keyword = "Answer: "
    answer_index = s.find(answer_keyword)

    extracted_char = None

    # Extracting the character after "Answer: " if found
    if answer_index != -1 and answer_index + len(answer_keyword) < len(s):
        extracted_char = s[answer_index + len(answer_keyword)].strip()

    # Trimming the string from "Answer"
    trimmed_string = s[:answer_index].strip() if answer_index != -1 else s

    return (trimmed_string, extracted_char)


def getQuestions(topic, difficulty, age):
    openai.api_type = "azure"
    openai.api_key = os.environ['OPENAI_API_KEY']
    openai.api_base = 'https://api.umgpt.umich.edu/azure-openai-api/ptu'
    openai.api_version = '2023-03-15-preview'
    
    if len(topic) == 0:
        topic = "random trivia"
    
    prompt = f"Give me {50} different questions about {topic} that are {difficulty} and are appropriate for ages {age} and up. Use a tilde as delimiters after each correct answer before the new question starts."
    
    questions = []  # Store 50 questions and answers
    
    try:
        response = openai.ChatCompletion.create(
            engine='gpt-4',
            messages=[
                {"role": "system", "content": "You generate multiple choice (A-D) questions for a topic and also give the right letter for the correct answer. Dont use the word correct. Just say Answer: A, B, C, or D."},
                {"role": "user", "content": prompt},
            ]
        )
        # print(response['choices'])
        parts = response['choices'][0]['message']['content'].split('~')
        questions = []
        for part in parts:
            trimmed_string, extracted_char = extract_and_remove_from_answer(part)
            questions.append((trimmed_string, extracted_char))
        
        return questions
    
    except openai.error.APIError as e:
        # Handle API error here, e.g. retry or log
        print(f"OpenAI API returned an API Error: {e}")
        return None
    
    except openai.error.AuthenticationError as e:
        # Handle Authentication error here, e.g. invalid API key
        print(f"OpenAI API returned an Authentication Error: {e}")
        return None
    
    except openai.error.APIConnectionError as e:
        # Handle connection error here
        print(f"Failed to connect to OpenAI API: {e}")
        return None
    
    except openai.error.InvalidRequestError as e:
        # Handle connection error here
        print(f"Invalid Request Error: {e}")
        return None
    
    except openai.error.RateLimitError as e:
        # Handle rate limit error
        print(f"OpenAI API request exceeded rate limit: {e}")
        return None
    
    except openai.error.ServiceUnavailableError as e:
        # Handle Service Unavailable error
        print(f"Service Unavailable: {e}")
        return None
    
    except openai.error.Timeout as e:
        # Handle request timeout
        print(f"Request timed out: {e}")
        return None
    
    except Exception as e:
        # Handles all other exceptions
        print(f"An exception has occurred: {e}")
        return None
