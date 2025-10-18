import requests
import json



def talk(x):

    send = {'content':x}
    
    res = requests.post('http://localhost:5678/webhook/chat',
    json=send,
    )
    
    return res.json()



phrase = input('ask : ')
result = talk(phrase)

print(result)

