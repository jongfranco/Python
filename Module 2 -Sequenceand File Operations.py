#1. What is the output of the following code?
#nums = set([1,1,2,3,3,3,4,4])
#print(len(nums))
#Hint: Set consists unique element.

nums = set([1,1,2,3,3,3,4,4])
print(len(nums))
# Answer is 4 because it will ignore repeated values or string or integer

#2.What will be the output?
# d ={"john":40, "peter":45}
#print(list(d.keys()))
#Hint:d.keys()isthefunctionwhichwillshowkeys

d ={"john":40, "peter":45}
print(list(d.keys()))

#Answer will be ["John","peter"] becuase these are keywords and this will show only keys

#3.A website requires a user to input username and password to register. Write a program
#to check the validity of password given by user. Following are the criteria for checking
#password:

#1. At least 1 letter between [a-z]
#2. At least 1 number between [0-9]
#1. At least 1 letter between [A-Z]
#3. At least 1 character from [$#@]
#4. Minimum length of transaction password: 6
#5. Maximum length of transaction password: 12

#Hint: In case of input data being supplied to the question, it should be assumed to be a
#console input.

import re
def checkpassword(e):
    for i in e:
        if (len(e)<6 or len(e)>12):
            print("Not a Valid passowrd")
            break
        elif not re.search('[a-z]',e):
            print("Not a Valid passowrd")
            break
        elif not re.search('[A-Z]',e):
            print("Not a Valid passowrd")
            break
        elif not re.search('[0-9]',e):
            print("Not a Valid passowrd")
            break
        elif not re.search('[$#@]',e):
            print("Not a Valid passowrd")
            break
        else:
            print("Valid Password")
            break
checkpassword("Raghu#12@3$")

#4. Write a for loop that prints all elements of a list and their position in the list.
#a = [4,7,3,2,5,9]
#Hint: Use Loop to iterate through list elements.

a = [4,7,3,2,5,9]
def looppostion(d):
    for i in d:
        print(i)
        print("Position of value ",i,"in list ",d.index(i))
        
looppostion(a)
    


#5. Please write a program which accepts a string from console and print the
# characters that have even indexes.
# Example: If the following string is given as input to the program:
# H1e2l3l4o5w6o7r8l9d
# Then, the output of the program should be:
# Helloworld

class combinewword():
    def __init__(self,a):
        self.a = a
    def printletter(self):
        word = []
        for each in self.a:
            if each.isalpha():
                word.append(each)
        print(''.join(word))
        
s = combinewword("H1e2l3l4o5w6o7r8l9d")
s.printletter()


#6. Please write a program which accepts a string from console and print it in reverse
#order.
# Example: If the following string is given as input to the program:
# rise to vote sir
# Then, the output of the program should be:
# ris etov ot esir
class reversewword():
    def __init__(self,a):
        self.a = a
    def reverseletter(self):
        words=[]
        for i in self.a:
           words.append(i)
        words.reverse()
        print(''.join(words))

s = reversewword("rise to vote sir")
s.reverseletter()



#7. Please write a program which count and print the numbers of each character in a
#string input by console.
# Example: If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
#a,2
#c,2
#b,2
#e,1
#d,1
#g,1
#f,1

#Version 1
class countwword():
    def __init__(self,a):
        self.a = a
    def counts(self):
        words=[]
        for i in self.a:
           words.append(i)
        for i in words:
            print(i,",",words.count(i))
s = countwword("abcdefgabc")
s.counts()

#Version 2
from collections import Counter
S ='abcdefgabc'
S = S.lower()
d = Counter(S)
for item, i in d.items():
      print('%s occured %d times' % (item, i))

#8. With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a
#program to make a list whose elements are intersection of the above given lists.

a = set([1,3,6,78,35,55])
b = set([12,24,35,24,88,120,155])
a &= b
li = list(a)
print(li)

#9. With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this
#list after removing all duplicate values with original order reserved.

b = [12,24,35,24,88,120,155,88,120,155]
def removedupliacate(a):
    c =[]
    for each in a:
        if each not in c:
            c.append(each)
    print(c)

b = [12,24,35,24,88,120,155,88,120,155]
removedupliacate(b)

from collections import OrderedDict
list(OrderedDict.fromkeys(b))

#10.By using list comprehension, please write a program to print the list after removing
#the value 24 in [12,24,35,24,88,120,155].
def removeelement(a):
    b = int(input("Enter the value which you have remove : "))
    #print(type(b))
    c = []
    for i in a:
        if i!=b:
            c.append(i)
    print(c)

x = [12,24,35,24,88,120,155]        
removeelement(x)

li = [12,24,35,24,88,120,155]
li = [x for x in li if x!=24]
print(li)


#11.By using list comprehension, please write a program to print the list after removing
#the 0th,4th,5th numbers in [12,24,35,70,88,120,155]

x = [12,24,35,70,88,120,155]      
x = [y for(i,y) in enumerate(x) if i not in (0,4,5)]
print (x)

#12.By using list comprehension, please write a program to print the list after removing
#delete numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

z = [12,24,35,70,88,120,155]      
z = [x for x in z if x%5!=0 and x%7!=0]
print (z)

#13.Please write a program to randomly generate a list with 5 numbers, which are
#divisible by 5 and 7 , between 1 and 1000 inclusive.

import random
z = random.sample([x for x in range(1,1001) if x%5==0 and x%7==0],5)
print (z)



#14.Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by
#console (n>0).
#Example:
#If the following n is given as input to the program:
#5
#Then, the output of the program should be:
#3.55

n=int(input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print(sum)
