# Q1. 
# for a in range(1,11):
#     print(a)

# Q2.
# a=int(input('Enter any integer: '))
# b=0
# for i in range(1,a):
#     b=b+i
# print(b)

# Q3.
# a=int(input('Enter any number: '))
# for i in range(1,11):
#     print (a,'x',i,'=',a*i)

# Q4.
# numbers = [12, 75, 150,  180, 145, 525, 50]
# for i in numbers:
#     if i>500:
#         break
#     elif i>150:
#         continue
#     elif i%5==0:
#         print(i)

# Q5.
# a= [12, 75, 150,  180, 145, 525, 50]
# for i in (a[::-1]):
#     print(i)

# Q6.
# a=int(input('Enter any number: '))
# for i in range (2,a+1):
#     for j in range (2,i):
#         if i%j==0:
#             print(f'{i} is not a prime number')
#             break
#     else:
#         print(f'{i} is a prime number')

# Q7.
# a=int(input('Enter any number: '))
# factorial=1
# for i in range (1,a+1):
#     factorial*=i
# print(factorial)

# Q8.
# n=int(input('Enter any number: '))
# even=0
# for i in range(1,n+1):
#     if i%2==0:
#         even=even+i
# print('The sum of even number till',n,'is',even)

# Q9.
# import random
# number=random.randint(1,10)
# numberguesses=1
# guess=int(input('Enter your guess: '))
# while (guess != number):
#     if guess > number:
#         print ('Close to',guess,', try again')
#     else:
#         print('Close to',guess,', try again')
#     numberguesses +=1
#     guess=int(input('Enter your guess: '))
# print('congratulations you got the right guess: ',guess)

# Q10.
# word=str(input('Enter your word: '))
# for i in (word[::-1]):
#     print(i)

# Q11.
# sentence=str(input('Enter you input: '))
# letters=0
# digits=0
# for i in sentence:
#     if i.isalpha():
#         letters+=1
#     elif i.isdigit():
#         digits+=1
# print('Total letters: ',letters)
# print('Total digits: ',digits)

# Q12.
# a=str(input('Enter your string: '))
# length=0
# for i in a:
#     length=length+1
# print('length of a string is: ',length)

# Q13.
# a=str(input('Enter your string: '))
# vowels='aeiouAEIOU'
# consonants='bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
# vowel_count=0
# consonant_count=0
# for i in a:
#     if i in vowels:
#         vowel_count+=1
#     elif i in consonants:
#         consonant_count+=1
# print('vowels count',vowel_count)
# print('consonants count',consonant_count)

# Q14.
# a=int(input('Enter numbers: '))
# numbers=[]
# for i in range(a):
#     b=int(input())
#     numbers.append(b)
# print(numbers)

# Q15.
# a=[1,2,3,4,5,6]
# for i in a:
#     b=a.copy()
# print(b)

# Q16.
# a=[29,13,9,6,70]
# maximum_value=a[0]
# for i in a:
#     if (i > maximum_value):
#         maximum_value = i
# print('maximum value:',maximum_value)

# Q17.
# numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# even=0
# odd=0
# for i in numbers:
#     if i%2==0:
#         even+=1
#     else:
#         odd+=1
# print(even)
# print(odd)

# Q18.
# numbers = [3, 5, 23,  6, 5, 1, 2, 9, 8]
# add=0
# for i in numbers:
#     add=add+i**2
# print('The sum of squares is',add)

# Q19.
# gadgets = ['Mobile','Laptop',100,'Camera',310.28,'Speakers', 27.00,'Television',1000,'Laptop Case','Camera Lens']
# # (a).
# strings=[]
# numbers=[]
# for i in gadgets:
#     if str(i).replace(".", "").isdigit():  
#         numbers.append(i)
#     else:
#         strings.append(i)

# print("list of strings:", strings)
# print("list of numbers:", numbers)
# # (b).
# strings=['Mobile', 'Laptop', 'Camera', 'Speakers', 'Television', 'Laptop Case', 'Camera Lens']
# for i in strings:
#     strings.sort()
# print(strings)
# # (c).
# strings=['Mobile', 'Laptop', 'Camera', 'Speakers', 'Television', 'Laptop Case', 'Camera Lens']
# for i in strings:
#     strings.sort(reverse=True)
# print(strings)
# # (d).
# numbers=[100, 310.28, 27.0, 1000]
# for i in numbers:
#     numbers.sort()
# print(numbers)
# # (e).
# numbers=[100, 310.28, 27.0, 1000]
# for i in numbers:
#     numbers.sort(reverse=True)
# print(numbers)