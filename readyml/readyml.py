import os
import yaml


class YamlHandler:
    def read_yaml(self, filename):
        # 读取yaml文件数据
        with open(filename, 'r', encoding='utf-8',)as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, filename, data, encoding='utf-8'):
        # 在yaml文件里写入
        with open(filename, encoding=encoding, mode='w')as f:
            return yaml.dump(data, stream=f, allow_unicode=True)
