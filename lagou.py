# -*- coding: utf-8 -*-
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def get_json(url, page, lang_name):
    data = {
    'first':'True',
    'pn':page,
    'kd':lang_name
    }
    json = requests.post(url, data).json()
    return json

url = 'http://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'

json = get_json(url, 2, 'python')
list_con = json['content']['positionResult']['result']
for i in list_con:
    print i['companyShortName'], i['companyFullName'], i['salary'], i['city'], i['education'], i['positionName']