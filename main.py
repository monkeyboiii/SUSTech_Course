import random
import requests
import re
import time
import json

info = {}  # inside json file
s = requests.Session()  # wrap all requests in a session for cookies


# load & login with sesion id (execution)
def login():
    global info
    with open('info.json', 'r') as f:
        info = json.load(f)
        url = info['login_url']
        r = s.get(url)
        data = {
            'username': info['username'],
            'password': info['password'],
            'execution': re.findall('on" value="(.+?)"',
                                    r.text)[0],  # ungreedy
            '_eventId': 'submit',
            'geolocation': ''
        }
        r = s.post(url, data)
        print(data['username'] + ' logged in!')


# reiterate until jwxt releases course selection panel
def courseCenter():
    url = info['enter_select_url']
    url_to_be_appended = info['url_to_be_appended']
    while True:
        r = s.get(url)
        key = re.findall('<a href="(.+?)" target="blank">进入选课</a>', r.text)
        if len(key) > 0:
            k = key[0]  # token to append
            panel = s.get(url_to_be_appended + k)
            if (click(panel)):
                return
        sleepTime = 0.2 + 0.05 * random.random()  # [200, 250) ms
        print('try after ' + str(sleepTime) + 's')
        time.sleep(sleepTime)


def click(panel):
    # xkOper = 选课操作
    # 公共选修课，本学期计划选课，方案外，跨年级
    # operlist = ["ggxxkxkOper"，"bxqjhxkOper", "fawxkOper", "knjxkOper"]
    operlist = ["ggxxkxkOper", "bxqjhxkOper"]
    url = info['course_url_to_be_appended']
    total = len(info['course'])
    for courseid in info['course']:
        urllist = [
            url + i + "?jx0404id=" + courseid + "&xkzy=&trjf="
            for i in operlist
        ]
        for urls in urllist:
            r = s.get(urls)
            result = str(r.text)
            print(result, end=' ')
            sleepTime = 0.2 + 0.05 * random.random()  # [200, 250) ms
            if result.find("true") >= 1:
                total = total - 1
                if total <= 0: return true
    return False


if __name__ == "__main__":
    login()
    courseCenter()