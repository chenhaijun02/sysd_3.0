import yaml
import os
from common.contants import DATA_DIR

class HandleYaml():
    def __init__(self, path):
        self.path = path

    def read_yaml(self):
        with open(self.path, "r", encoding="utf-8") as f:
            data = yaml.load(f)
        return data
if __name__ == '__main__':
    yamlpath = os.path.join(DATA_DIR, "login.yml")
    data = HandleYaml(yamlpath).read_yaml()
    print(data)
    # for i in data[1:-1]:
    #     name =i["name"]
    #     print(name)
    name = [i["name"] for i in data[1:-1]]
    print(name)