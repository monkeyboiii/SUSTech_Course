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
        
        r = s.post(url=url, data=data, headers={
            # trivial
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "content-type": "application/x-www-form-urlencoded",
            "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "same-origin",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "referer": "https://cas.sustech.edu.cn/cas/login?service=https%3A%2F%2Ftis.sustech.edu.cn%2FcasLogin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
        })
        
        if r.status_code == 200:
            print(data['username'] + ' logged in!')
            return True
        else:
            print('not logged in')
            return False


def tisCourseCenter():
    print(tisClick())
    
def tisClick():
    url='https://tis.sustech.edu.cn/Xsxk/addGouwuche'
    data = 'p_pylx=1&p_sfgldjr=0&p_sfredis=0&p_sfsyxkgwc=0&p_xktjz=rwtjzyx&p_chaxunxh=&p_gjz=%E6%95%B0%E6%8D%AE%E6%8C%96%E6%8E%98&p_skjs=&p_xn=2020-2021&p_xq=2&p_xnxq=2020-20212&p_dqxn=2020-2021&p_dqxq=2&p_dqxnxq=2020-20212&p_xkfsdm=kzyxk&p_xiaoqu=&p_kkyx=&p_xkxs=&p_id=B3B8FB81A1A810EDE053CA0412AC70A7&p_sfhlctkc=0&p_sfhllrlkc=0&p_kxsj_xqj=&p_kxsj_ksjc=&p_kxsj_jsjc=&p_kcdm_js=&p_kcdm_cxrw=&p_kc_gjz=&p_xzcxtjz_nj=&p_xzcxtjz_yx=&p_xzcxtjz_zy=&p_xzcxtjz_zyfx=&p_xzcxtjz_bj=&p_sfxsgwckb=1&p_skyy=&p_chaxunxkfsdm=&pageNum=1&pageSize=13'
    r = s.post(url=url,data=data,headers={
        "content-type": "application/x-www-form-urlencoded",
        
        # trivial
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control": "max-age=0",
        "sec-ch-ua": "\"Google Chrome\";v=\"87\", \" Not;A Brand\";v=\"99\", \"Chromium\";v=\"87\"",
        "sec-ch-ua-mobile": "?0",
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    })

    print(r.text)
    
    result = json.loads(r.text)
    if result['jg'] == '-1':
        return False
    else:
        return True
    

if __name__ == "__main__":
    if login():
        tisCourseCenter()