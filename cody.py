import os
import subprocess
import openai
from llama_cpp import Llama

API_KEY = "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"

prepromptFile = open("preprompt.txt")
prepromptStr = prepromptFile.read()
full_conv = prepromptStr


llm = Llama(model_path="c:/Users/Cyril/Documents/GPT/LLAMAModel/ggml-model-q4_0.bin")

def truc():
    while True:
            query = input()
            if query.lower() == 'stop':
                break
            else:
                process_query(query)

def send_to_gpt(query):
    #response = openai.Completion.create(engine="text-davinci-003",
    #                                    prompt=query,
    #                                     temperature = 0.6,
    #                                     max_tokens = 350)
    #
    response = llm(query, max_tokens=32, stop=["Q:", "\n"], echo=True)
    return response.choices[0].text
    

def init_gpt():
    #openai.api_key = API_KEY

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