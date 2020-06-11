import json,csv


with open("csv_file.txt" , "r") as my_file:
    Csv_to_list = [{key:value for key, value in row.items()} 
        for row in csv.DictReader(my_file, skipinitialspace=True)]


with open("json_file.txt" , "w") as my_file:
    list_to_csv = json.dump(Csv_to_list, my_file, indent= 6)



