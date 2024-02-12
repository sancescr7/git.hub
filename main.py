#a = 2112
#print(a, type(a)) 
#b = 8.54
#print(b, type(b))
#c = '2112'
#print(c, type(c))
#d = True
#print(d, type(d))
#salary = int (input('maas daxil edin: '))
#print(salary, type(salary))
#print(salary, '$')

#a = 5
#b = 2
#a*b

#birinci_reqem = int(input('ilk reqemi yazin: '))
#ikinci_reqem = int(input('novbeti reqemi yazin: '))

#print(birinci_reqem // ikinci_reqem)
#print(birinci_reqem / ikinci_reqem)
#print(birinci_reqem % ikinci_reqem)

#a = int(input())
#a += 10 # a = a +10
#print(10!=5)

#a = int(input())

#print(a//10,a%10)

#a = int(input())
#b = a//100
#c = %





# a = int(input())

# if 1 <= a <= 3:
#     print("Initial")
# elif 4 <= a <= 6:
#     print("Average")

# elif 7 <= a <= 9:
#     print("Sufficient" )

# elif 10 <= a <= 12:
#     print("High")

# else:
#     print("1,12 uygun olaraq mueyyenlesdirildi")

# a = abs(int(input()))

# b = a//100 
# c = a//10
# d = c%10
# s = a%10
# print(b)
# print(d)
# print(s)

# a,b = map(int , input().split())
# if a < b:
#     print(a,b)
# elif b < a:
#     print(b,a)


# n,m = map(int , input().split()) 
# if (n+m)%2==1:
#     print('0')
# else:
#     print('1')


# a,b,c = map(int , input().split())
# if a%c==0:
#     otaq_oglan = a//c
# else:
#     otaq_oglan = a//c + 1

# if b%c==0:
#     qizdarin_otagi = b//c
# else:
#     qizdarin_otagi = b//c +1
# print(otaq_oglan + qizdarin_otagi)

# a = int(input())
# if 0 < a:
#     print("Positive")
# elif a==0:
#     print("Zero")
# else:
#     print("Negative")

# a = int(input())
# if 0 < 3:
#     print("ODD")
# else:
#     print("EVEN")

# y = int(input())
# if 3 > 0:
#     print("0")
# else:
#     print("y==0")

# a = int(input()) 
# b = int(input())

# if a % b == 0 and b % a == 0:
#     print("0")
# elif a == 0:
#     print("a,b==0")

# y = int(input())
# if 2 < 4:
#     print("y==2")
# elif 8100 > 20:
#     print("y==8100")
# else:
#     print("y==0")

# a = abs(int(input()))
# import math as m
# print(abs(-65))

# print(pow(2,7))  # -> 128
# print(round(5.6)) # -> 6
# print(round(5.87326732, 2)) # -> 5.87

# print(min(5, 2, 1, 121, -12, 0))
# print(max(5, 2, 1, 121, -12, 0))

# print(m.pi)
# print(m.e)

# print(m.floor(13.99))

# a= int(input())

# b = a%10
# c = a//10
# print(f"{c}{c}{b}{b}") 

# a = int(input())

# b = a//1000 # 1
# c = a//100
# d = c%10 # 2

# v = a//10
# f = v%10 #  3
# s = a%10 # 4
# print(f"{s}{f}{d}{b}")

#12345

# a = int(input())
# b = a//10000 # 1
# c = a//100
# v = c%10 # 3
# s = a%10 # 5
# print(f"{b}{v}{s}")
#123
# a = int(input())
# b = a%10 # 3
# c = a//10 # 12
# print(f"{b}{c}")

# a = int(input())
# if a % 2 == 1:
#     print(a-1)
# elif a % 2 == 0:
#     print(a-2)

# a = int(input())
# if a >= 0:
#     print(a**3+2*a**2+4*a-6)
# elif a < 0:
#     print(a**3-7*a)

# a = int(input())
# if a > 0:
#     print("Water")
# elif a <= 0:
#     print("Ice")

#15689

# a = int(input())
# b = a//10000 # 1
# c = b//1000
# s = c%10 # 5
# f = a//100
# t = f%10 # 6
# g = a//10
# h = g%10 #8
# n = a%10 # 9
# if b<s<t<<h<n:
#     print("YES")
# else:
#     print("NO")

# 2345

# a = int(input())
# b = a//1000
# c = a//100
# s = c%10
# n = a//10
# m = n%10
# e = a%10
# if b<s<m<e:
#     print("YES")
# else:
#     print("NO")
# 27
# a = int(input())
# b = a//10
# c = b%10 # 2
# d = a%10 # 7
# print(f"{d}")

# 567  # 374
# a = int(input())
# b = a//100
# c = b//10
# m = c%10 # 5
# v = a//10
# n = v%10 # 6
# x = a%10 # 7
# if m<n<x:
#     print("YES")
# else:
#     print("NO")



# n = int(input("input: "))

# for i in range(n):
#     print(i)
#     i +=2

# n = int(input('input. '))

# while n > 1:
#     if n % 2 == 0:
#         print('cut eded')
#         n += 1
#         break
#     else:
#         print('tek eded')
#         break

# n = 'salam'
# # print(len(n))
# for i in range(len(n)):
#     print(n[i])

# n = int(input())

# for i in range(0, n):
#     for j in range(0, i+1):
#         print("* ",end="")
#     print()

# l,k = map(int,input().split())
# saygac = 0

# while l > 1:
#     l = l / k
#     saygac += 1
# print(saygac)

# n = int(input('Input: '))

# while n > 1:
#     if n % 2 == 0:
#         print('Cut eded')
#         n += 1
#     else:
#         print('Tek eded')
#         break


# for i in range(1, n+1):
#     if i % 3 == 0:
#         print('3-e bolunen eded')
#     else:
#         print('Sehv')

# n = 'salam'
# print(n[5])
# print(len(n))
# for i in range(len(n)):
#     print(n[i])

# for count, i in enumerate(n, start=1):
#     print(count, i)
# for i in n:
#     print(i)
# n = int(input())

# for i in range(0, n):
#     for j in range(0, i+1):
#         print("* ",end="")
#     print()

# Task 1

# l,k = map(int, input().split())
# saygac = 0

# while l / k > 1:
#     l = l / k
#     saygac += 1 

# print(saygac)

# 198

# a = int(input())
# b = a//100 # 1
# c = a//10
# v = c%10 # 9
# n = a%10 # 8
# print(f"{b}{n}")
#  321
# a = int(input())
# b = a%10 # 1
# while input > 9:
#     c = a//10 # 32
#     n= a%10 # 2
# print()

# n = int(input())
# n = abs(n)
# while n > 99:
#     a = n%10
#     n = n//10
# if a > 9:
#     a = n%10
# print(a)

# a = int(input())
# n = 1
# while n**2 <= a:
#     print(n**2,end=" ")
#     n+=1

# 2345
# n = abs(int(input()))
# a = n%10 #5
# while n > 9:
#     n = n // 10
# print(n+a)

# n = int(input())
# l = list(map(int,input().split()))
# for i in range (n):
#     l[i]

# bosh_list = []

# students = ['Murad', 32, 7.95, ['Cefer', 'Faina', 'Yusif'], True, 'Anar', 'Fatime']
# print(bosh_list)
# print(students[3][2][2])
# inside_list = students[3]
# inside_list.pop(0)
# print(inside_list)
# print(students)
# print(len(students))
# print(students[::-1])
# print(students)
# students.append(['Ramin', 'Jamil'])
# students.append('Ramin')
# students.append('Jamil')
# students.insert(0, 'Lale')
# print(students)  #['Lale', 'Murad', 32, 7.95, ['Cefer', 'Faina', 'Yusif'], True, 'Anar', 'Fatime', 'Ramin']
# students.pop(0)
# print(students)
# students.remove(32)


# n = int(input())
# l = list(map(int,input().split()))
# for i in range (n):
#     l[i]

# n = int(input())
# for i in range(0, n):
#     for j in range(0, i+1):
#         print("* ",end="")
#     print()


# a = int(input())
# l = list(map(int, input().split()))
# print(l[-1],end =" ")

# for i in range(a - 1):
#     print(l[i],end =" ")


# a = int(input())
# if a > 1:
#     l = list(map(int, input().split()))
#     b = min(l)
#     c = max(l)
#     print(b,c, end = " ")
# else:
#     print("Ooops!")

# a = int(input())
# b = list(map(int,input().split()))
# saygac = 0
# for i in range(a):
#     if b[i]!= max (b):
#         saygac=saygac + b[i] 
# print(saygac)

# 4
# 92846
# 96841
# 33582
# 25998
# list = []
# a = int(input())
# for i in range(a):
#     c = int(input())
#     list.append(c)
# print(*list[::-1])

# a = int(input())
# l = list(map(int, input().split()))
# for i in range(a):
#     if l[i]%2 == 1:
#         print(l[i], end = " ")

# new_matrix = [[14,56,41], ['murad','anar',True],[7.5,46,'cefer']]
# print(new_matrix)
# print(new_matrix[1])

# for i in range(len(new_matrix)):
#     for k in range





# new_matrix = [[14, 56, 41], ['Murad', 'Anar', True], [7.5, 46, 'Cefer']]
# print(new_matrix)
# print(new_matrix[1][2][0])


# for i in range(len(new_matrix)):
#     for k in range(len(new_matrix[i])):
#         print(new_matrix[i][k], end=' ')
#     print()

# for i in new_matrix:
#     for k in i:
#         print(k, end=' ')
#     print()


# row = int(input('Enter row: ')) # setr
# col = int(input('Enter column: ')) # sutun

# new_matrix = [list(map(int, input().split())) for i in range(row) ]


# for row in new_matrix:
#     for k in row:
#         print(k+1, end=' ')
#     print()








# new_matrix = [[14, 56, 41], ['Murad', 'Anar', True], [7.5, 46, 'Cefer']]
# print(new_matrix)
# print(new_matrix[1][2][0])


# for i in range(len(new_matrix)):
#     for k in range(len(new_matrix[i])):
    #     print(new_matrix[i][k], end=' ')
    # print()

# for i in new_matrix:
#     for k in i:
#         print(k, end=' ')
#     print()


# row = int(input('Enter row: ')) # setr
# col = int(input('Enter column: ')) # sutun

# new_matrix = [list(map(int, input().split())) for i in range(row) ]


# for row in new_matrix:
#     for k in row:
#         print(k+1, end=' ')
#     print()

# n = int(input())
# for i in range(n):
#     for j in range(n):
#         print("* ",end=" ")
#     print()

# a = int(input())
# b = 0
# c = 0
# new_matrix = [list(map(int, input().split())) for i in range(a)]
# for i in range(len(new_matrix)):
#     for j in range(len(new_matrix[i])):
#         if new_matrix[i][j] < 0  and new_matrix[i][j] % 2 == 0:
#             b = b + 1
#             c = c + new_matrix[i][j]
# print(b , c)
            

            


# a = int(input())
# c = 0
# new_matrix = [list(map(int, input().split())) for i in range(a)]
# for i in range(len(new_matrix)):
#     for j in range(len(new_matrix[i])):
#         if new_matrix[i][j]>0:
#             c = c + new_matrix[i][j]
# print(c)

# a = input()
# print("Hello,", a)

# a,b = map(int,input().split())
# print(a**2 + b**2)

# 15689 #12321
# a = int(input())
# c = a//10000
# b = a%10
# v = a//10
# l = v%10
# g = a//1000
# f = g%10
# j = a//100
# d = j%10 
# if c < f < d < l < b:
#     print("YES")
# else:
#     print("NO")

# a = int(input())
# if a == 3 or a == 4 or a == 5:
#     print("Spring")
# elif a == 6 or a == 7 or a == 8:
#     print("Summer")
# elif a == 9 or a == 10 or a == 11:
#     print("Autumn")
# elif a == 12 or a == 1 or a == 2:
#     print("Winter")


# n = int(input())
# for i in range(n):
#     a = int(input())
#     if a % 2 == 0:
#         print(a,'is even')
#     else:
#         print(a, 'is odd')




# a = int(input())
# for i in range(1 , a+1):
#     if a%i == 0:
#         if i%2 != 0:
#             print(i)


# n = int(input())
# saygac = 0
# while n > 1:
#     if n %2 == 0:
#         n = n//2
#         saygac+=1
#     else:
#         n = n+1
#         saygac+=1
# print(saygac)

   
# a = 'Codelandia Academy'
# print(a[4:12])
# new = (a.strip())

# a = str(input())
# b = len(a)
# print(a)
# print(b)

# a = str(input())
# b = str(input())
# x = a.lower()
# c = x.count(b)
# print(c)

# a = str(input())
# b = a.count('2')
# c = a.count('5')
# if b>c:
#     print('2')
# elif c>b:
#     print('5')
# else:
#     print("=")

# 539013
# a = str(input())
# a = a.replace('3',"")
# a = a.replace('9',"")
# print(a)

# a = str(input())
# b = str(input())
# c = len(a)
# v = len(b)
# if a > b:
#     print('no')
# else:
#     print('go')

# a = str(input())
# b = a.split()
# c = len(b)
# print(c)

# text = input()

# plus = text.count("+")
# minus = text.count("-")
# vur = text.count("*")
# count = plus+ minus + vur
# if(text[0] == "-") or (text[0] == "+"):
#     print(-1)
# else:
#     print(count)


# a = input()
# if a == a[::-1]:
#     print("Yes")
# else:
#     print("No")

# a, sign, b = input().split()
# a = int(a)
# b = int(b)
# if sign == "+":
#     print(a + b)
# elif sign =="*":
#     print(a*b)
# elif sign == "/":
#     print(a//b)
# else:
#     print(a-b)

# a = input()
# if a.count(' ') !=0:
#     print(a.index(' '), a.rfind(' '))
# else:print(-1)

# s = input()
# s = s.replace('a','0')
# s = s.replace('b','a')
# s = s.replace('0','b')
# print(s)

# a,b,c = map(float,input().split())
# def cefer(x,y,z):
#     return  min(max(x,y), max(y,z), x+y+z)
# print(cefer(a,b,c))

# a = int(input())
# def cefer(x):
#     return 1+x+x**2
# print(cefer(a))

# a,b,c = map(int,input().split())
# def cefer(x,y,z):
#     return x*y*z + x + y**2 + z**3
# print(cefer(a,b,c))

# a = input()
# def cefer(vorqaqas):
#     saygac = 1
#     for i in vorqaqas:
#         if i != '0':
#             saygac = saygac * int(i)
#     print(saygac)    

# cefer(a)    

# a = int(input())
# def cefer():
#     if a >=1:
#         c = list(map(int,input().split()))
#         balaca_halley = min(c)
#         print(balaca_halley)
# cefer()


# a = int(input())
# l = list(map(int,input().split()))
# def cefer():
#     for i in range(a):
#         if l[i]%3==0:
#             print(l[i]//3, end=' ')
#         else:
#             print(l[i],end=' ')
# cefer()
# import sys
# a = int(input())
# def cefer(a):
#     if a == 0:
#         return 0
#     elif a > 0:
#         return cefer(a-1)+a
# sys.setrecursionlimit(1000)
# print(cefer(a))


# a = abs(int(input()))

# def cefer(b):
#     if b == 0:
#         return 0
#     else:
#         return b % 10 + cefer(b//10)
 
    

# print(cefer(a))

# n = int(input())
# def faktorial(eded):
#     if eded>1:
#         return eded * faktorial(eded-1)
#     else:
#         return 1
# print(faktorial(n))    


# a , b = map(int , input().split())
# def cefer(x , y):

# movie={
#     'name': 'cefer',
#     'surname': 'azizov',
#     'age': 15
# }
# info = dict(name ='cefer', surname = 'azizov', age = 15)
# print(new_dict)
# print(info)
# print(type(new_dict))



# movie={
#     'name': 'cobra kai',
#     'director': 'azizov',
#     'imdb': 9.8,
#     'release': 2019
# }

# print(movie.get('imdb'))
# print(movie.keys())
# print(movie.values())
# print(movie.items())

# for i in movie:
#     print(i)

# for i in movie:
#     print(movie[i])

# for i in movie.keys():
#     print(i)

# for i in movie.values():
#     print(i)

# for key, value in movie.items():
#     print(key,':',value)
#     print(f'{key}-{value}')



# movie={
#     'cobra kai': {
#         "director": 'katrin l. goodson, bob wilson',
#          "rating": 9.4,
#          "year": 2018,
#         'actors' :{
#             'caracter 1':{
#                 'name':'xolo mariduena',
#                 'age': 22,

#             },
#             'caracter 2':{
#                 'name':'mary mouser',
#                 'age': 27,
#             },
#              'caracter 3':{
#                 'name':'william zabka',
#                  'age': 58,
#             },
#             'caracter 4':{
#                 'name': 'ralph macchio',
#                 'age': 62,
#             },
#             'caracter 5':{
#                 'name':'tanner buchanan',
#                 'age': 25,
#             },
#             'caracter 6':{
#                 'name':'jacob bertrand',
#                 'age': 23,
#             },
#             'caracter 7':{
#                 'name':'peyton list',
#                 'age': 25,
#             },
#             'caracter 8':{
#                 'name':'martin kove',
#                 'age': 77,
#             },
#             'caracter 9':{
#                 'name':'Gianni DeCenzo',
#                 'age': 22 ,
#             },
#             'caracter 10':{
#                 'name': 'griffin santopietro',
#                 'age': 17,
#             },
#             'caracter 11':{
#                 'name':'vanessa rubio',
#                 'age': 40,
#             },
#             'caracter 12':{
#                 'name':'courtney henggler',
#                 'age': 45,

#             },
#             'caracter 13':{
#                 'name':'anallisa cochrane',
#                 'age': 27,
#             },
        

        
#         },

#     },
#             'the conjuring':{
#         "director": 'james wan : patric wilson  ',
#          "rating": 7.4,
#          "year": 2013,
#         'actors':{
#              'caracter 1':{
#                  'name':'vera farmiga',
#                  'age': 50,
#              },
#              'caracter 2':{
#                  'name':'sterling jerins',
#                  'age': 16,
#              },
#              'caracter 3':{
#                  'name': 'lili taylor',
#                  'age': 56,
#              },
#              'caracter 4':{
#                  'name':'patrick wilson',
#                  'age': 50,
#              },

             
#          },
# },





# },
# for i in movie:
#     for j in movie[i]['actors']:
#         print(j,movie[i]['actors']['caracter 1'])
#         break
# print(movie)
# for i in movie:
#     for j in movie[i]['actors']['caracter1']:
#         print(j, movie[i]['actors']['caracter1']['name'])
#         break


# a , b = map(int , input().split())
# def cefer(x , y):
    
# a = int(input())
# def cefer(x):
#     if x < 10:
#         return 1
#     else:
#         return cefer(x//10)+1
# print(cefer(a))    






# b = input()
# a = 'AIOUYE'
# count = 0
# for i in b:
#     if i in a:
#         count += 1
# print(count)

# n = input()
# j = n.count(max(n))
# print(j)

# a = input()
# b = input()
# c = input()


























































































































































































































































































































































