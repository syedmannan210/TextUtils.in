import json
import numpy
from difflib import get_close_matches
import nltk
import random
import time

#Load the knowledge base from JSON file
def load_knowledgebase(filepath :str)-> dict:
    with open(filepath,'r') as file:
        data:dict=json.load(file)
        return data

#Save data to knowledge base:
def save_knowledgebase(filepath:str,data:dict):
    with open(filepath,'w') as file:
        json.dump(data,file,indent=2)

#to find the best matches
def find_bestmatches(userquestion:str,questions:list[str])->str | None:
    matches:list=get_close_matches(userquestion,questions,n=1,cutoff=0.6)
    return matches[0] if matches else  None

#Get answer to questions from user:
def getanswer_toquestions(question:str,knowledgebase:dict)->str | None:
    for q in knowledgebase["questions"]:
        if q["question"]==question:
            return q["answer"]

from nltk.corpus import wordnet

# Function to handle greetings
def handle_greetings(userinput: str) -> str | None:
    # Define a set of greeting words
    GREETING_KEYWORDS = ("hello", "hi", "greetings", "hey")

    # Tokenize the user's input
    words = nltk.word_tokenize(userinput)

    # If any of the words in the user's input is a greeting, return a greeting response
    for word in words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(["Hello!", "Hi there!", "Hey!", "Hello, how can I help you?"])

    return None

#Conv. Ending Function:

def conv_end(userinput:str)->str|None:
    ending_words=("okay","ok","bye","thats fine","see you around!","thanks","appreciated")
    endwords=nltk.word_tokenize(userinput)
    for endword in endwords:
        if endword.lower() in ending_words:
            time.sleep(0.05)
            return ("Thanks! for your time Sir!, If you need any other help. I'm here to assist you.")



#Main Function
def chatbot():
    print("Phoenix the chatbot!".center(150).upper())
    time.sleep(1)
    knowledgebase:dict=load_knowledgebase("knowledgebase.json")
    while True:
        userinput=input("You: ")
        greeting_response = handle_greetings(userinput)
        if greeting_response:
            print(f"Phoenix: {greeting_response}")
            continue
        if userinput.lower()=="skip":
            break
        ending_response=conv_end(userinput)
        if ending_response:
            print(f"Phoenix: {ending_response}")
            continue
        else:
            bestmatch:str = find_bestmatches(userinput,[q["question"] for q in knowledgebase["questions"]])
        if bestmatch:
            answer:str= getanswer_toquestions(bestmatch,knowledgebase)
            print(f"Phoenix: {answer}")
        else:
            print("Phoenix: Sorry I dont know the answer the of this question! Can you please teach me?")
            new_answer=input("Type The answer Or 'skip' to Skip: ")
            if new_answer.lower()!="skip":
                knowledgebase["questions"].append({"question":userinput,"answer":new_answer})
                save_knowledgebase("knowledgebase.json",knowledgebase)
                print(f"Thanks for teaching me a new response!")

if __name__=="__main__":
    chatbot()
