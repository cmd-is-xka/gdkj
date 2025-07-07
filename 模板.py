import sys
import os
sys.path.append(os.getcwd())
import pytest
#数据库存链接
from sqlconnect.sql_con import *
#接口请求方法
from reque.request_method import RunManin
#读取参数
from readyml.readyml import YamlHandler

#自定义测试名称Name,testname
#任务编号测试描述:*****************
#测试预期：*************
class Name:
    
    #第一步参数准备arrange
    def Arrange_testname(self,data):
        datavalue=data['datavalue']
        return
    
    #第二步act开始测试
    def Act_testname(self,data):
        
        return
    
    #第三步assert判断
    def Assert_testname(self,data):
        assert 1==2
        return

    #第四步测试后数据处理
    def Afterarrange_testname(self,data):
        return

#测试开始入口Test下面的test_
class TestAllTestName:
    #参数存放 格式    name: ''
    #test_name_name 定义名称要求大概描述测试代码内容
    stockdatafilename = "autotest/step2test/beferdatas/test.yml"
    testdata = YamlHandler().read_yaml(stockdatafilename)
    @pytest.mark.parametrize("data", [testdata])
    def test_name_name(self,data):
        testcase1 = Name()
        testcase1.Arrange_testname(data)
        testcase1.Act_testname(data)
        testcase1.Assert_testname(data)
        testcase1.Afterarrange_testname(data)
 
if __name__ == '__main__':
    #调试执行，推送注销
    pytest.main(["autotest/step2test/test_test.py::TestAllTestName", '-v', '-s'])