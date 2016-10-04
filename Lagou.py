#-*-coding:utf-8-*-
from __future__ import division
import requests
from pymongo import MongoClient
import json
import time
import math
import random

from filterbox import filterbox ,agents

requests = requests.session()
client = MongoClient("localhost", 27017)
db_position = client.Lagou["position"]
db_company = client.Lagou["company"]

def getjson(query_params,first = True,pn=1):
        requests.headers.update({'User-Agent':random.choice(agents)})
        url = "http://www.lagou.com/jobs/positionAjax.json?px=default"+query_params
        params = {"first":first,"pn":pn} 
        res = requests.post(url,params)
        return json.loads(res.text)

def get_total_pages(result):
    num = result['content']['positionResult']['totalCount']
    return int(math.ceil(num/15))

def save_to_mongodb(num,results):
    print "current page:" +str(num)
    for result in results:
        position={}
        company={}
        position['positionId'] = result['positionId']
        position['companyId'] = result['companyId']
        position['positionName'] = result['positionName']
        position['workYear'] = result['workYear']
        position['education'] = result['education']
        position['jobNature'] = result['jobNature']
        position['industryField'] = result['industryField']
        position['companyShortName'] = result['companyShortName']
        position['companyFullName'] = result['companyFullName']
        position['city'] = result['city']
        salary=result['salary'].split('-')
        try:
            salary_min = int(salary[0][:-1])*1000
            salary_max = int(salary[1][:-1])*1000
        except:
            salary_min=result['salary']
            salary_max=result['salary']
        position['salary_max'] = salary_max
        position['salary_min'] = salary_min
        position['positionAdvantage'] = result['positionAdvantage']
        position['district'] = result['district']
        position['createTime'] = result['createTime']
        position['approve'] = result['approve']
        position['publisherId'] = result['publisherId']
        position['explain'] = result['explain']
        position['plus'] = result['plus']
        position['deliver'] = result['deliver']
        position['gradeDescription'] = result['gradeDescription']
        position['businessZones'] = result['businessZones']

        company['companyId'] = result['companyId']
        company['companyFullName'] = result['companyFullName']
        company['companyShortName'] = result['companyShortName']
        company['financeStage'] = result['financeStage']
        company['companyLogo'] = result['companyLogo']
        company['industryField'] = result['industryField']
        company['city'] = result['city']
        company['district'] = result['district']
        company['companyLabelList'] = result['companyLabelList']
        company['businessZones'] = result['businessZones']
        try:
            db_position.insert(position)
        except:
            pass
        try:
            db_company.insert(company)
        except:
            pass


def process(query_params ='',box_index=0,last_param=''):
    params = filterbox[box_index]
    for  param in params.values()[0]:
        if params.keys()[0] in query_params:
            query_params=query_params.replace(last_param,'')
        add_param = "&"+params.keys()[0]+"="+param
        query_params = query_params+add_param
        print query_params
        try:
            result =getjson(query_params)
            count = get_total_pages(result) #返回页数
        except:
            count=0
        if count==0:
            query_params=query_params.replace(add_param,'')
            print query_params
        elif count<=330:
            first=False
            for pn in range(1,count+1):
                try:
                    results=getjson(query_params,first,pn)["content"]['positionResult']['result']
                    save_to_mongodb(pn,results)
                    time.sleep(random.randint(2,3))
                except:
                    pass
            query_params=query_params.replace(add_param,'')
            print query_params
        elif params.keys()[0]=="gx" and count>330:
            for pn in range(1,331):
                try:
                    results=getjson(query_params,first,pn)["content"]['positionResult']['result']
                    save_to_mongodb(pn,results)
                    time.sleep(random.randint(2,3))
                except:
                    pass
            query_params=query_params.replace(add_param,'')
            print query_params
        else:
            box_index=query_params.count('&')
            last_param = add_param
            process(query_params,box_index,last_param)


if __name__=='__main__':
    process()
