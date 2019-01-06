#1. Write a program which will find factors of given number and find whether the
#factor is even or odd.

def factor_even_or_odd(num):
    for each in range(1,num+1):
        if each%2!=0:
            print("it is odd number : ",each)
        else:
            print("it is even number : ",each)
factor_even_or_odd(40)



#2. Write a code which accepts a sequence of words as input and prints the words in a
#sequence after sorting them alphabetically. 
def sortwords(word):
    #sortwords = input("Enter the sentence : ")
    a = word.split()
    a.sort()
    for each in a:
        print(each)
sortwords(input("What is your sentence : "))

#3. Write a program, which will find all the numbers between 1000 and 3000 (both
#included) such that each digit of a number is an even number. The numbers
#obtained should be printed in a comma separated sequence on a single line
num = list(range(1000,3001))
sq1=[]
def evennumber(num):
    for each in num:
        if each%2==0:
            sq1.append(each)
evennumber(list(range(1000,3001)))
print(sq1)

#4.Write a program that accepts a sentence and calculate the number of letters and
#digits.
a="Raghavender1984"

word=0
digit=0
def letter(a):
    global word
    global digit
    for each in a:
        if each.isalpha():
            word=word+1
        else:
            digit=digit+1
#letter(input("The letter with digit : "))
letter("Hello123")
print(word)




word = 0
digit =0
for each in a:
        if each.isalpha():
            word = word+1
        else:
            each.isdigit()
            digit = digit+1
print(word)
print(digit)

#5. Design a code which will find the given number is Palindrome number or not.
def isplaindrom(n):
    num = n
    d =0
    rev=0
    while n>0:
        d = n%10
        print("d is ",d)
        n = int(n/10)
        print("n is ",n)
        rev = rev*10+d
        print("rev is ",rev)
    if num==rev :
        return True
        #print (n, " is plaindorme")
    else:
        return False
        #print (n, " is not plaindorme")
        
x = int(input("Enter No : "))
if isplaindrom(x):
    print(x, " is plaindrom")
else:
    print(x, " is not plaindrom")