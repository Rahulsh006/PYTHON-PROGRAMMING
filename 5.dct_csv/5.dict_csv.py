salary = [{'Name':'Alice', 'Job':'Data Scientist', 'Salary':122000},
          {'Name':'Bob', 'Job':'Engineer', 'Salary':77000},
          {'Name':'Carl', 'Job':'Manager', 'Salary':119000}]

import pandas as pd
df = pd.DataFrame(salary)
df.to_csv('my_file.csv', index=False, header=True)

a=pd.read_csv("my_file.csv")
print(a)



'''import csv

field_names = ['No', 'Company', 'Car Model']

cars = [
{'No': 1, 'Company': 'Ferrari', 'Car Model': '488 GTB'},
{'No': 2, 'Company': 'Porsche', 'Car Model': '918 Spyder'},
{'No': 3, 'Company': 'Bugatti', 'Car Model': 'La Voiture Noire'},
{'No': 4, 'Company': 'Rolls Royce', 'Car Model': 'Phantom'},
{'No': 5, 'Company': 'BMW   ', 'Car Model': 'BMW X7'},
]

with open('Names.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(cars)
with open('Names.csv','r') as file_obj:
    read_obj = csv.reader(file_obj,delimiter='\t')
    [print((x[0]).replace(",","        ")) for x in read_obj if x!=[]]
'''