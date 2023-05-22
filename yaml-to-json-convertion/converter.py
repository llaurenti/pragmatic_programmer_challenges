import os, re
import shutil
import yaml
import json

path = input("Type directory that contain Y[A]ML files: ")

for file in os.listdir(path):
    source = path + file
    destination = path + re.sub('.yaml', '.json', file)
    print(destination)
    with open(source, 'r') as yaml_file:
        contents = yaml.safe_load(yaml_file)
        print(contents) 
    shutil.copy(source, destination)
    with open(destination, 'w') as json_file:
        json.dump(contents, json_file)
        print('jhonson', json_file)
        print('c', contents)
        #output = json.dumps(json.load(open(destination, 'w')), indent=2)
