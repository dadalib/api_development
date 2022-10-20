
import requests
import json
import certifi


response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow',verify = False) 
data =response.json()['items']

for question in data:
    # print("type",type(question))
    if question['answer_count']==0:
        print(question['title'])
        print(question['link'])
    else:
        print('skipped')

