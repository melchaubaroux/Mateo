
import json
import requests

from config import *


def text_to_text (text): 

    payload_text_to_text["text"]+=text
    
    response = requests.post(url=url_text_to_text,json=payload_text_to_text,headers=header)
    result = json.loads(response.text)
    # model = list(result.keys())[0]
    return(result['openai']['generated_text'])
   


def text_to_speech (text): 


    payload_text_to_speech["text"]+=text

    response = requests.post(url=url_text_to_speech,json=payload_text_to_speech,headers=header)
    result = json.loads(response.text)
    # model = list(result.keys())[0]
    return(result['openai']['audio'])
    






