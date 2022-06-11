import csv

with open("python.csv","w")as file_obj:

    file_obj_csv = csv.writer(file_obj)
    file_obj_csv.writerow(["name","class","marks"])
    file_obj_csv.writerow(["simran","7th","88"]),(["harry","4th","90"])

with open("python1.csv","w",newline = "")as file_obj:
    file_obj_csv = csv.DictWriter(file_obj,["name","class","marks"])
    file_obj_csv.writeheader()
    file_obj_csv.writerows([{"name":"A","class":7,"marks":76},{"name":"B","class":4,"marks":89}])



import pandas

my_input = [["name","class","marks"],["simran",7,87],["sofia",9,78]]
my_final_input = pandas.DataFrame(my_input)
print(my_final_input)

my_final_input.to_csv("mydata.csv",index = None)
