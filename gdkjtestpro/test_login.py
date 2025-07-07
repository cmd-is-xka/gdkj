import requests
import json
import urllib3
urllib3.disable_warnings()
import sys
import os
sys.path.append(os.getcwd())
import pytest
#读取参数
from readyml.readyml import YamlHandler




class Name:
    def request_api(self,url, payload):
        try:
            headers = {'Content-Type': 'application/json'}
            response = requests.request("POST", url, headers=headers, data=payload)
            assert response.status_code == 200
            response = json.loads(response.text)
            userid = response['data']['userId']
            token = response['data']['token']
            assert userid == '1901529012060598273'
            result = {
                "userid":userid,
                "token":token
            }
            print(result)
            return result
            
        except Exception as e:
            return {
                "error": str(e),
                "is_valid": False,
                "message": f"请求过程中发生异常: {str(e)}"
            }
    def Assert_testname(self,data):
        mainurl = 'https://zhpro.gdcar.net'
        url = "%s/service/user/login"%(mainurl)

        payload = json.dumps({
        "openidMiniApp": "",
        "unionId": "",
        "phoneNumber": "13485760190",
        "userPassword": "1234567A"
        })
        headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuYmYiOjE3NDI4MDU3MDMsImV4cCI6MTc0MzQxMDUwMywiaWF0IjoxNzQyODA1NzAzfQ.9AuK9xQVI2-8sep0uSPKfnIP717vOWxCP96ZT1ALvyQ'
        }

        test_result = Name().request_api(url, payload)
        
        # 保存测试结果
        result_file_name = "userinfo.json"
        with open('gdkjtestpro/%s'%(result_file_name), 'w', encoding='utf-8') as f:
            json.dump(test_result, f, ensure_ascii=False, indent=4)


    
class TestAllTestName:
   datafilename = "gdkjtestpro/beferdatas/test.yml"
   testdata = YamlHandler().read_yaml(datafilename)
   @pytest.mark.parametrize("data", [testdata])
   def test_name_name(self,data):
      testcase1 = Name()
      testcase1.Assert_testname(data)


# if __name__ == '__main__':
#     #调试执行，推送注销
#     #pytest.main(["gdkjtestpro/test_login.py::TestAllTestName", '-v', '-s'])
