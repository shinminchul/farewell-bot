import requests

class QnAmaker:
    url = "https://westus.api.cognitive.microsoft.com/qnamaker/v2.0/knowledgebases/"
    def __init__(self, kb_id, subscription_key):
        self.kb_id=kb_id
        self.subscription_key=subscription_key
    
    def create(self, name, qnapairs, urls)
        pass
    
    def delete(self)
