import subprocess
import openai

def is_sentence_finished(query:str) -> bool:
     lastChar = query[query.__len__() - 1]
     
     if (lastChar == '.' or lastChar == '?' or lastChar == '!'):
          return True
     return False

def get_openai_key():
     with open("openai.api.key") as file:
          return file.read()

API_KEY = get_openai_key()

prepromptFile = open("preprompt2.txt")
prepromptStr = prepromptFile.read()
full_conv = prepromptStr
out = ""

def truc():
    while True:
            query = input()
            if query.lower() == 'stop':
                break
            else:
                process_query(query)

def send_to_gpt(query:str):
    response = openai.Completion.create(engine="text-davinci-003",
                                        prompt=query,
                                         temperature = 0.6,
                                         max_tokens = 350)
    
    return response.choices[0].text
    

def init_gpt():
    openai.api_key = API_KEY

    print(prepromptStr)
    #response = send_to_gpt(prepromptStr)
    global full_conv
    #full_conv = full_conv + response
    #print(response)

def parse(response:str):
     action = response.splitlines()
     
     for line in action:
        if (line.find("S:") == 0):
            line = line[2:line.__len__()]
            print("LOG:"+line)
            commandResult = subprocess.run(line, stdout=subprocess.PIPE, shell=True)
            global out
            out = commandResult.stdout

        elif (line.find("P:") == 0):
             line = line[2:line.__len__()]
             
             if (out.__len__() > 0):
                line.replace("$return", out)
             
             print(line)

def process_query(query):
    # Code for processing the command goes here
    if (False):#(not is_sentence_finished(query)):
         query += '.'
         print("LOG: sentence unfinished, add \'.\' at the end.")

    query = "\nU: "+ query + "\n"
    global full_conv
    full_conv = full_conv + query
    response = send_to_gpt(full_conv)
    parse(response)
    
    full_conv = full_conv + "\n" + response
         

init_gpt()
truc()