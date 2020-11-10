import pytest
from common.handle_request import HandleRequest
from common.myconfig import conf
from common.handle_yml import HandleYaml
from common.contants import DATA_DIR
import os
import jsonpath

def pytest_collection_modifyitems(items):
    """
    测试用例收集完成时，将收集到的item的name和nodeid的中文显示在控制台上
    :return:
    """
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


@pytest.fixture()
def test_login(self):
    yamlpath = os.path.join(DATA_DIR, "login.yml")
    data = HandleYaml(yamlpath).read_yaml()
    url = conf.get_str("env", "url")
    header = eval(conf.get_str("env", "header"))
    http = HandleRequest()
    res = http.send(method="post", json=data, url=url, headers=header)
    token = jsonpath.jsonpath(res.json, "$..token")
    yield token
