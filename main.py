from requests import Session, Request
import random
import time
import json
import re


config = {}  # configurations inside config.json file
s = Session()  # wrap requests in session for cookies


# load & login
def login():
    global config
    with open('config.json', 'r') as f:
        config = json.load(f)
        url = config['login_url']
        
        r = s.get(url)  # cas page        
        data = {
            'username': config['username'],
            'password': config['password'],
            'execution': re.findall('on" value="(.+?)"', r.text)[0],  # ungreedy, a really long random string
            '_eventId': 'submit',
            'geolocation': ''
        }
        r = s.post(url=url, data=data)
        
        if r.status_code == 200:
            print(data['username'] + ' logged in!')
            return True
        else:
            print('not logged in')
            return False


def tisCourseCenter():
    global config
    
    forms = config['course_forms']
    tasks = len(forms)
    succees = [False * tasks]
    task = 0
    
    while tasks > 0:
        if not succees[task] and tisClick(forms[task]):
            tasks = tasks - 1
        else:
            task = (task + 1) % tasks
        time.sleep(0.1 + random.random() / 5)
            
    
def tisClick(data):
    url='https://tis.sustech.edu.cn/Xsxk/addGouwuche'
    r = s.post(url=url,data=data,headers={"content-type": "application/x-www-form-urlencoded"})
    print(r.text)
    result = json.loads(r.text)
    if result['jg'] == '-1':
        return False
    else:
        return True
    

if __name__ == "__main__":
    if login():
        tisCourseCenter()