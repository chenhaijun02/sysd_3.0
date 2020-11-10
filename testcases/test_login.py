import pytest
from common.handle_request import HandleRequest
from common.myconfig import conf
from common.handle_yml import HandleYaml
from common.contants import DATA_DIR
import os
import jsonpath
import  allure
from common.mylogger import log


class TestLogin():
    yamlpath = os.path.join(DATA_DIR, "login.yml")
    datas = HandleYaml(yamlpath).read_yaml()
    url = conf.get_str("env", "url") + datas[0]["url"]
    header = eval(conf.get_str("env", "header"))
    name=[i["name"] for i in datas[1:] ]
    @log
    @pytest.mark.parametrize("data", datas[1:],ids=name)
    @allure.feature("登录模块")
    def test_login(self, data):
        http = HandleRequest()
        res = http.send(method="post", json=data, url=self.url, headers=self.header)
        assert data["Message"] == res.json()["Message"]


if __name__ == '__main__':
    pytest.main(["-s"])
