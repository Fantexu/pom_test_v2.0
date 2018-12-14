import os


def get_txt(file):
    with open(file, 'r', encoding='utf-8') as f:
        text = f.readlines()
        data = list()
        for i in text:
            data.append(tuple(i.strip().split(',')))
        return data
