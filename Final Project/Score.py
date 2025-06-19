import json
import pathlib

filename = str(pathlib.Path(__file__).parent.resolve()) + "\\Score.json"

def read():
    with open(filename, 'r') as file:
        return json.load(file)

def write(data):
    with open(filename, 'w') as file:
        return json.dump(data, file)

def save(nama,score):
    data = read()
    data[score] = nama
    write(data)
