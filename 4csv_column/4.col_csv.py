import csv

try:
    a = int(input("enter the column no to read : "))
    with open('temp.csv','r') as file_obj:

        read_obj = csv.reader(file_obj,delimiter='\t')
        d = next(read_obj)
        l = len(d)
        if a>l:
            print(" colomn count error ")
        else:
            print("coloumn ",d[a-1],"content : ")
            [print(x[a-1],end=", ") for x in read_obj]

except Exception:
    print(Exception)