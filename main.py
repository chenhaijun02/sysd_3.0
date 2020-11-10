import pytest
import allure
import os
if __name__ == '__main__':
    pytest.main(["-s", "--alluredir=outputs/allure"])
    os.system("allure generate outputs/allure -o report --clean")