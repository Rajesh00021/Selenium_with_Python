
# login= 31
# if (login < 10):
#     print("Login unsuccessful")
# elif(login==10):
#     print("Login successful")
# else:
#     print("Login again")
# a=10
# b=30
# if (a>b or a==b):
#     print("a is greater and equal than b")
# elif(a<b or a==b):
#     print("a is small and equal than b")
# else:
#     print("a is equal than b")
#
# i=1
# j=2
# while j<=20:
#     print(i + "x" +j +"=" +i*j)
#     j=j+2



# a=33
# # a=330
# # a=200
# b=200
# if b>a:
#     print("b is greater than a")
# elif a==b:
#     print("a is equal to b")
# else:
#     print("a is greater than b")

# while loop
# i=1
# while i<10:
# print(i)
# i=i+1

# for loop
# It is used to iterate the sequence
# s = [1,2,3,4,5,6,7,8,9,10]
# for i in s:
#  print(i,end=" ")
    # print(i)
# eg 2
# r = range(1,100)
# for i in r:
#     print(i)

#Fabunaci series
#
# a=0  # first index
# b=1   # second index
# print(a)
# print(b)
# for i in range(1,20):
#     c=a+b # third index
#     a=b
#     b=c
#     print(c)
#
#
# n = 12
# a = 0
# b = 1
# c = 0
# count = 1
# print("Fibonacci series is: ", end=" " )
# while(count <= n):
#   count += 1
#   print(a, end=" ")
#   a = b
#   b = c
#   c = a + b
# #
# Fabonacci series
# terms = int(input("Enter how many terms: "))
#
# first, second = 0, 1
# i = 0
#
# if terms <= 0:
#     print("Invalid input")
#
# elif terms == 1:
#     print("\nFibonacci series up to", terms, "terms:", end="  ")
#     print(first)
# else:
#     print("\nFibonacci series up to", terms, "terms:", end=" ")
#     while i < terms:
#         print(first, end=" ")
#         third = first + second
#         first = second
#         second = third
#         i += 1

# a=1
# for i in range(1,20):
#     print(i,end=" ")

# a=[10,20,30]
# for i in a:
#     print(i,end=" ")

# a = int(input("Enter First number: "))
# b= int(input("Enter Seccond number: "))
# if(a>b):
#     print("a is greater than b")
# elif (a==b):
#     print("a is equal to b")
# else:
#     print("b is greater than a")
#
#

# n= int(input("Enter any number between 0 to 5"))
# if n==0:
#     print("Zero")
# elif n==1:
#     print("One")
# elif n==2:
#     print("Two")
# elif n==3:
#     print("Three")
# elif n==4:
# #     print("Four")
# # elif n==5:
# #     print("Five")
#
# #
# from array import *
#
# a=array('i',[12,10,45,23,12,14])
# # a.append(100)
# a.extend([100,200,452])
# a.pop()
# a.remove(23)
# print(a)
# print(type(a))


# b=array('f',[12,21,25])
# print(b)
# print(type(b))
#
# x=[10,20,1,3]
# b=bytearray(x)
# b[1]=25
# print(type(b))
# for i in x: print(i)
# #
# st = array("u",("fhdjd"))
# print(type(st))

