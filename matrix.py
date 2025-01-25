# matrix is indimensional list
# m = [[],[]]
# a is an empty list which we are going to convert into a 2d matrix

a = []
rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))
for i in range(rows):
    temp = [] #it will create a row first, once one row is ready we add it into the matrix
    for j in range(columns):
        v = int(input("Enter your values:"))
        temp.append(v)
    a.append(temp)
    
    #just like a, b is a matrix 
b = []
rows = int(input("Enter the number of rows:"))
columns = int(input("Enter the number of columns:"))
for i in range(rows):
    temp = []
    for j in range(columns):
        v = int(input("Enter your values:"))
        temp.append(v)
    b.append(temp)
    
    #first we need empty matrix to add values as per calculation 
c = [] 
for i in range(rows):
    t = []
    for j in range(columns):
        t.append(0)
    c.append(t)
print(c)


for i in range(len(a)):
    for j in range(len(a [0])):
        c[i][j]= a[i][j]+b[i][j]

for i in range(len(c)):
    for j in range(len(c [0])):
        print(c[i][j])
        
#
    