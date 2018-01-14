import requests

class QnAmaker:
    def __init__(self, kb_id, subscription_key):
        self.url = 'https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/' + kb_id
        self.headers = {'Content-Type':'application/json; charset=utf-8', 'Ocp-Apim-Subscription-Key' : subscription_key}
    
    def getAnswer(self, message):
        generateanswer=self.url+"/generateAnswer"
        r = requests.post(generateanswer, headers=self.headers, json={'question': message})
        return r.json()