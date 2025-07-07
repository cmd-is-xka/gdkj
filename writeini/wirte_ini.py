import configparser
def writr_ini(name):
    conf = configparser.ConfigParser()
    conf.read("pytest.ini",encoding="utf-8")
    key = conf.get("pytest","junit_suite_name")
    conf.set("pytest",'junit_suite_name',name)
    conf.write(open("pytest.ini","w",encoding="utf-8"))