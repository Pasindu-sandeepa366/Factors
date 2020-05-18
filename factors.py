#!/usr/bin/python3
num = int(input("Enter number >> "))
count =1
for i in range (num):
    i=i+1
    x= num%int(i)
    if x == 0:
        print("[{0}] {1} is divided by {2} ".format(count,num,i))
        count = count +1
