import requests
import json
from pprint import pprint 
from requests.api import request
from requests.adapters import HTTPAdapter
from datetime import datetime

#使用方法 导入from autotest.reque.request_method import RunManin
#使用方法 result = RunManin().run_main('post',url,data,headers)
#使用方法 result = RunManin().run_main('get',url,data)
#使用方法 result = RunManin().run_main('put',url,data,headers)
#使用方法 result = RunManin().run_main('delete',url)

class RunManin():
    def send_get(self,url,data):
        result = requests.get(url, data,timeout=100)
        r_code = result.status_code
        results = json.loads(result.content)
        print(r_code)
        assert r_code == 200,f'状态码非200!'
        return results
    def send_delete(self,url):
        result = requests.delete(url)
        r_code = result.status_code
        results = json.loads(result.content)
        print(r_code)
        assert r_code == 200,f'状态码非200!'
        return results
    def send_post(self,url,data,headers):
        if headers == None:
            headers = {}
        else:
            headers = headers
        if data == None:
            data = {}
        else:
            data = data
        #result = requests.post(url,data.encode("utf-8"),headers=headers,timeout=20000)
        result = requests.post(url,data,headers=headers,timeout=600000)
        request_time = result.elapsed.total_seconds()
        r_code = result.status_code
        results = json.loads(result.content)
        print(r_code)
        assert r_code == 200,f'状态码非200!'
        return results
    def send_put(self,url,data,headers):
        if headers == None:
            headers = {}
        else:
            headers = headers
        if data == None:
            data = {}
        else:
            #如果有中文使用
            #data = data.encode("utf-8")
            data = data
        result = requests.put(url,data,headers=headers,timeout=13)
        r_code = result.status_code
        results = json.loads(result.content)
        print(r_code)
        assert r_code == 200,f'状态码非200!'
        return results
    def run_main(self,method,url=None,data=None,headers=None):
        result = None
        
        if method == 'get':
            result = self.send_get(url,data)
            return result
        if method == 'post':
            result = self.send_post(url,data,headers)
            return result
        if method == 'put':
            result = self.send_put(url,data,headers)
            return result
        if method == 'delete':
            result = self.send_delete(url)
        else:
            print("method值错误！")
