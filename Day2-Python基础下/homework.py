import json
from importlib.resources import contents

with open("heros.json", "r") as f, open("names.txt", "w",encoding="utf-8") as fp:
    hero_dic = json.loads(f.read())
    hero_dic = json.loads(hero_dic)
    # print(type(hero_dic))
    # print(hero_dic[2])
    for item in hero_dic['hero']:
        fp.write(f"{item['name']}-{item['title']}\n")
