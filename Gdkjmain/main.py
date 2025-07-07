import pytest
import sys
import os
sys.path.append(os.getcwd())
from writeini.wirte_ini import *
import xml.etree.ElementTree as ET
import json

#最后运行地方.
if __name__ == '__main__':
    writr_ini('Gdkj')
    pytest.main(["gdkjtestpro/test_login.py::TestAllTestName"])
    pytest.main(["gdkjtestpro", '-v', '-s','--junitxml=junit/test-results-gdkj.xml','-k','not test_login'])

    # 读取 XML 文件
    tree = ET.parse('junit/test-results-gdkj.xml')
    root = tree.getroot()

    # 提取 testsuite 元素
    testsuite = root.find('testsuite')

    # 获取所需的属性值
    errors = testsuite.get('errors')
    failures = testsuite.get('failures')
    skipped = testsuite.get('skipped')
    tests = testsuite.get('tests')

    content = {
        '测试结果':'详情如下',
        '错误':errors,
        '失败':failures,
        '跳过':skipped,
        '总数':tests
    }
    
    result_file_name = "result.json"
    with open('Gdkjmain/%s'%(result_file_name), 'w', encoding='utf-8') as f:
        json.dump(content, f, ensure_ascii=False, indent=4)