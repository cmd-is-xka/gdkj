from enum import verify
from pymysql import NULL
import requests
import json
import time
from sympy import false
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
      url = "https://zhpro.gdcar.net/ai/task/submitTask"

      payload = json.dumps([{
         "width": 1080,
         "height": 1920,
         "x": 0,
         "y": 0,
         "beauty_white_img_index": NULL,
         "beauty_enlarge_eye_img_index": NULL,
         "beauty_thinface_img_index": NULL,
         "beauty_smooth_img_index": NULL,
         "gen_srt": True,
         "videoid": "842c0866-c9c4-4501-b214-82dd0a50f57f",
         "source_video": "bd2_1.mp4",
         "background_name": "0ffae4fadf3141119322f3294f006ce5.png",
         "backgroundid": "1",
         "ref_audio": "缓慢慈祥讲知识_女.wav",
         "audioid": "audio10",
         "text": "123458",
         "videonmae": "",
         "fn_name": "wrapper_4",
         "tts_method": "CosyVoice",
         "no_change_background": False
       }])
      headers = {
      'Content-Type': 'application/json',
      'Authorization': '%s'%(token)}
      start_time = time.time()
      response = requests.request("POST", url, headers=headers, data=payload,verify=False)

      assert response.status_code ==200

      end_time = time.time()
      response_time = end_time - start_time

      print('接口响应时间：',response_time)

      result = json.loads(response.text)
      code = result['code']
      print(code)
      assert code ==0
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
    pytest.main(["gdkjtestpro/test_digitalHuman.py::TestAllTestName", '-v', '-s'])