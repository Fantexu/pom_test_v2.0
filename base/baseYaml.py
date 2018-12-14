import yaml
from selenium.webdriver.common.by import By


def get_yaml(yaml_path):
    with open(yaml_path, 'rb') as file:
        return yaml.load(file.read())


def set_yaml(yaml_path, data):
    with open(yaml_path, 'wb') as file:
        yaml.dump(data, file)


def get_tuple(yaml_path):
    data = get_yaml(yaml_path)
    for i in data:
        data[i] = eval(data[i])
    return data


def get_testdata(yaml_path, *args):
    text = get_yaml(yaml_path)
    data = list()
    for i in text:
        for j in i.values():
            data.append(tuple([j[x] for x in args]))
    return data


if __name__ == '__main__':
    path = '../data/loginData.yaml'
    # print(get_testdata(path))
    # text = get_yaml(path)
    # # print(text)
    # data = list()
    # for i in text:
    #     for j in i.values():
    #         a = j['phone']
    #         b = j['password']
    #         data.append((a, b))
    # print(data)
    # demo(1, 3, 45, 78)
    get_testdata(path, 'phone', 'password', 'code')