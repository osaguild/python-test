import json

# open file
file = open('./jsonformat/data/shop_format.json', 'r')

# get file data
data = json.load(file)

# print file data
print(data)