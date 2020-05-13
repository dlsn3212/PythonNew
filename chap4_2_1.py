dict_a = {
    "name" : "어벤져스 엔드게임",
    "type" : "히어로 무비",
    "cast" : ["아이언맨","타노스","토르","닥터스트레인지","헐크"],
    "director" : ["안소니 루소","조 루소"],
    "relase" : 2018
}

print(dict_a["director"][0])

dict_a["type"] = "로맨스"
dict_a["cameo"] = "스탠리"

print(dict_a)

del dict_a["relase"]
print(dict_a)

# print(dict_a["relase"])

print("")
print("")
key = "cast"