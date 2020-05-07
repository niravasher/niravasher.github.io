import os

#getting location of files
path_dir = input("Write path of directory where files are stored:")
os.chdir(path_dir)


#inputting files
name1 = input("Name of file 1:")
name2 = input("Name of file 2:")

f1 = open(name1)
f2 = open(name2)


#reading files line by line
lines1 = f1.readlines()
lines2 = f2.readlines()

n = len(lines1)
m = len(lines2)
p = m
if n>m:
    p=n


#traversing lines
for i in range(p):
    if i<n and i<m:
        if lines1[i] != lines2[i]: #highlighting only different lines
            if i<n:
                print("-", lines1[i])
            if i<m:
                print("+", lines2[i])
    else: #taking case of unequal number of lines
        if i < n:
            print("-", lines1[i])
        if i < m:
            print("+", lines2[i])
