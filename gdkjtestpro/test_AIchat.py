import requests
import json
import time
import urllib3
urllib3.disable_warnings()
import sys
import os
sys.path.append(os.getcwd())
import pytest
#读取参数
from readyml.readyml import YamlHandler


class Name:
   def read_json(self,filename):
      with open(filename, "r", encoding="utf-8")as f:
         userinfo = json.load(f)
      token = userinfo['token']
      return token
   
   def Assert_testname(self,data):

      token = Name().read_json('gdkjtestpro/userinfo.json')
      url = "https://zhpro.gdcar.net/ai/text/chatNew"

      payload = json.dumps({"message": "hello"})
      headers = {
      'Content-Type': 'application/json',
      'Authorization': '%s'%(token)}
      start_time = time.time()
      response = requests.request("POST", url, headers=headers, data=payload)

      assert response.status_code ==200

      end_time = time.time()
      response_time = end_time - start_time

      print('接口响应时间：',response_time)

      result = json.loads(response.text)


      content = result['data']['content']
      print(content)
      return
   

class TestAllTestName:
   datafilename = "gdkjtestpro/beferdatas/test.yml"
   testdata = YamlHandler().read_yaml(datafilename)
   @pytest.mark.parametrize("data", [testdata])
   def test_name_name(self,data):
      testcase1 = Name()
      testcase1.Assert_testname(data)


if __name__ == '__main__':
    #调试执行，推送注销
    pytest.main(["gdkjtestpro/test_AIchat.py::TestAllTestName", '-v', '-s'])