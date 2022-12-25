import csv
import pandas as pd

with open('main.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "Area", "Name" ,'Quantity','Brand'])
    writer.writerow(['ID1','Minneapolis','shoes',2,'Air'])
    writer.writerow(['ID2','Chicago','shoes',1,'Air'])
    writer.writerow(['ID3','Central Department Store','shoes',5,'BonPied'])
    writer.writerow(['ID4','Quail Hollow','forks',3,'Pfitzcraft'])

df = pd.read_csv('main.csv')
listName = df['Name']
lengthName = len(listName)
uniqueName = listName.unique()
zero_input =  df.groupby('Name').agg({'Quantity': ['sum']}) / lengthName
with open('0_input_file_name.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(zero_input.to_string())
with open('1_input_file_name.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name" ,'Brand'])
    twoFile = df.groupby(['Name', 'Brand']).size().idxmax()
    writer.writerow(twoFile)


