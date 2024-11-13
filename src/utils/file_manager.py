import csv
import json

class FileManager():

    def __init__(self):
        pass
    
    def read_csv(file_name):
        with open(file_name, mode="r") as file:
            reader = csv.reader(file)
            return [row for row in reader]

    def export_csv(data, file_name="CSV desde File Manager"):
        with open(file_name, mode="w", newline=" ") as file:
            writer = csv.writer(file)
            for row in data:
                writer.writerow(row)

    def read_json(file_name):
        with open(file_name, mode="r") as file:
            return  json.load(file)
        
    def export_json(data, file_name):
        with open(file_name, mode="w") as file:
            json.dump(data,file, indent=4)
