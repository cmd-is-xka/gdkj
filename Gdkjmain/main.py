import pytest
import sys
import os
sys.path.append(os.getcwd())
from writeini.wirte_ini import *
import xml.etree.ElementTree as ET
import json




def run_tests_with_allure():
    writr_ini('Gdkj')
    allure_result_dir = "allure-results"
    allure_report_dir = "allure-report"
    report_txt_path = "allure_report_path.txt"
    # 清理旧的结果
    if not os.path.exists(allure_result_dir):
        os.makedirs(allure_result_dir)

    print("开始执行测试并生成中间结果...")
    pytest.main(["gdkjtestpro/test_login.py::TestAllTestName"])
    ret = pytest.main(["gdkjtestpro", '-v', '-s','--junitxml=junit/test-results-gdkj.xml', f"--alluredir={allure_result_dir}",'-k','not test_login'])


    if ret != 0:
        print("❌ pytest 执行失败，Allure 报告不会生成")
        return

    print("✅ pytest 执行完成，开始生成 Allure 报告...")

    # 生成 allure 报告（使用 os.system）
    gen_status = os.system(f"allure generate {allure_result_dir} -o {allure_report_dir} --clean")

    if gen_status == 0:
        abs_report_path = os.path.abspath(allure_report_dir)
        print(f"✅ Allure 报告生成成功，路径为：{abs_report_path}")

    else:
        print("❌ Allure 报告生成失败，请确认 allure 是否已安装并配置到环境变量")

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




#最后运行地方.
if __name__ == '__main__':
    run_tests_with_allure()