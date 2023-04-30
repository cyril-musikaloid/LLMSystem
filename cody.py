import os
import openai

def getOpenAIKey():
     with open("openai.api.key") as file:
          return file.read()

API_KEY = getOpenAIKey()

prepromptFile = open("preprompt.txt")
prepromptStr = prepromptFile.read()
full_conv = prepromptStr

def truc():
    while True:
            query = input()
            if query.lower() == 'stop':
                break
            else:
                process_query(query)

def send_to_gpt(query):
    response = openai.Completion.create(engine="text-curie-001",
                                        prompt=query,
                                         temperature = 0.6,
                                         max_tokens = 350)
    
    return response.choices[0].text
    

def init_gpt():
    openai.api_key = API_KEY

    print(prepromptStr)
    response = send_to_gpt(prepromptStr)
    global full_conv
    full_conv = full_conv + response
    print(response)

def process_query(query):
    # Code for processing the command goes here

    query = "\n[USER]: "+ query
    global full_conv
    full_conv = full_conv + query
    response = send_to_gpt(full_conv)
    print(response)
    
    full_conv = full_conv + "\n" + response
         

init_gpt()
truc()