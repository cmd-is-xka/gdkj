import pytest
import sys
import os
sys.path.append(os.getcwd())
from writeini.wirte_ini import *
#最后运行地方.
if __name__ == '__main__':
    writr_ini('Gdkj')
    pytest.main(["gdkjtestpro/test_login.py::TestAllTestName", '-v', '-s','--alluredir=./result','--junitxml=junit/test-results-gdkj.xml'])
    # pytest.main(["gdkjtestpro", '-v', '-s','--junitxml=junit/test-results-gdkj.xml','-k','not test_login'])

