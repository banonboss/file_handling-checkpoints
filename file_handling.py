# with open("text.txt","r") as file:
#     content = file.read()
#     print(content)

# with open("text.txt","w") as file:
#     file.write("\nI appended a new line.")

# with open("text.txt","a") as file:
#     file.write("\nI appended a new line.")

# with open("text.txt","x") as file:
#      file.write("\nI appended a new line.")

# with open("data.csv","r") as file:
#     c = file.read()
#     print(c)

#Add new row to the csv file
# with open("data.csv","a") as obj:
#     obj.write("\nOla,50,Ondo")
     
# import numpy as np
# data = np.genfromtxt("data.csv", dtype =str, delimiter=",", usecols=[1])
# print(data)
import numpy as np

with open("loan.csv","r") as f:
    data = f.read()



data = np.genfromtxt("loan.csv", delimiter=",", usecols=8, filling_values=0)

array = np.array(data)

#calculate the mean of the array
mean=np.mean(array)
print(mean)

median = np.median(array)
print(median)

max= np.max(array)
print(max)

var=np.var(array)
print(f"the var is:{var}")
