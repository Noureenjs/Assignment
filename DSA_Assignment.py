#!/usr/bin/env python
# coding: utf-8

# # 1. Complete the following code to find the area of an equilateral triangle. Output should be as displayed
#     

# In[1]:


import math
side = float(input("Enter the side of the equilateral triangle: "))
area = ((math.sqrt(3))/4)*pow(side,2)
print("Area =" , area)


# # 2. Write a program to count the number of each characters in a string

# In[2]:


string = "perimeter"
count=0
for i in string:
  count+=1
print(count)


# # 3. Write a program to find the area and perimeter of a rectangle using functions

# In[3]:


def area_rectangle(l,b):
  return (l*b)

length = int(input("enter length:-"))
breadth = int(input("enter breadth:-"))

print(area_rectangle(length, breadth))


# # 4. Write a program to print the fibonacci series till a specified number
# 

# In[4]:


count =int(input("enter the count:-"))
n1 , n2 = 0 ,1
for i in range (count):
  print(n1)
  nth = n1+n2
  n1 =n2
  n2 =nth


# # 5. Complete the following code to find the minimum of 3 number using cinditional statements. Output should be as displayed
# 

# In[5]:


a,b,c = input("Enter three numbers followed by  : ").split()

print("First number :",a)
print("Second number :",b)
print("Third number :",c)
a =int(a)
b=int(b)
c=int(c)
if a == b == c:
    print("Entered numbers are equal!!!")
elif b > a < c:
    print(a," is smallest")
elif c > b < a:
    print(b," is smallest")
elif a > c < b:
    print(c," is smallest")


# # 6. Write a program to print star pyramind. The number of rows should be taken as input from the user
# 

# In[6]:


rows = int(input("enter the num of rows:"))
for i in range(rows):
  for j in range(rows -i-1):
    print(end =" ")
  for j in range (i+1):
    print("*" , end =" ")
  print()


# # 7. Complete the following code to convert hour into seconds. Output should be as displayed

# In[7]:


def to_seconds(t):
    t =t*3600
    return t
time_in_hours = int(input(" enter the time in hours :-"))
print(time_in_hours ," Hour is equal to" ,to_seconds(time_in_hours) ," Seconds")


# # 8. Write a program to print multiplication table as below

# In[12]:


for i in range (1,11):
  multiply = 1*6
  print( i ,"x" ,"6" ," =" , multiply)


# # 9. Write a program to take your 5 favorite food as list and print each as 'I like Biriyani'
# 

# In[14]:


a,b,c = input("Enter your favourite food list followed by  : ").split()
print("I like" , a)
print("I like" ,b)
print("i like", c)


# # 10. Find error(s) in the following code(if any) and rewrite code.

# In[15]:


x=int(input("Enter value of x:"))
for y in range(0,10):
     if x==y:
        print("They are equal")
     else:
        print( "They are unequal")


# In[ ]:




