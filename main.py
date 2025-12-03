#  class 2 lucter 
# if / elif/ else

# marks=int(input("enter your marks: "))

# if(marks>=90):
#     grade="A"
# elif(marks>=80 and marks<90):
#     grade= "B"
# elif(marks>=70 and marks<80):
#     grade= "C"
# elif(marks>=60 and marks<70):
#     grade= "D"


# print("grade of student->", grade)

#  
# age= int(input("enter your age: "))

# if(age>= 18):
#     if(age>=70):
#         print("can't dive")
#     else: 
#         print("can drive")
# else: 
#     print("can drive")

#  pratices odd or even

# num= int(input("enter your munber: "))

# if(num % 2==0):
#     print("EVEN")
# else:
#     print("ODD")
# grestest number 4
# A = int(input(" enter fast number: "))
# B = int(input("enter second number:"))
# C= int(input(" enter third number:"))
# D = int(input(" enter forth number:"))

# if (A>= B and A>= D and A>= C):
#     print(" fast number is largest")
# elif(B>=C and B>=D):
#     print("second is largest")
# elif(C>=D ):
#     print("third is largest")
# else:
#     print(" forth is largest") 


# # multipul of 7
# x= int(input("enter a number: "))

# if( x % 7 ==0):
#     print("multipul of 7")
# else:
#     print("not multipul of 7")


#class 03 lecture

# marks=[94,54,78,98,77]
# print(marks)
# print(type(marks))
# print(marks[3])
# print(marks[0])
# print(len(marks))

# #string-is-immutable (unchangeable)
# #list is mutable(changeabke)

# student=["tanvir",90,"physis"]
# #print(student(3))  #not possible

# #list slicing
# print(marks[0:5])
# print(marks[:3])
# print(marks[1:])

#list methods

# list=[3,1,3,2,4,5,]
# list.append(8)
# print(list.append(9)) #none result but add 9 next print result
# print(list)
# list.sort()
# print(list)
# list.sort(reverse=True)
# print(list)
# list.reverse()  # last to fast
# print(list)
# list.insert(5,6) #add exta 6 in fifth position
# print(list)
# list.remove(1) #fast number 1
# print(list)
# list.pop(3)
# print(list)

#tuples
# immutable (cannot change )
list =[4,2,4,5,6,8,5,4]
tup= (2,3,4,3,5,6,7,4)
print(type(tup))
tup1 =(1)# type= int 
tup2= (1,)# type tup
tup3=("hello")#type str
tup=( "hello",)#type tup (single word must use ,)

# tuple methods
tup=( 1,3,2,2,3,4,)
print(tup.index(3)) # fast place of 3
print(tup.count(2))# total 2 count

#practice question
#Question 1
movies=[]
mov1=input("enter you 1st movie name :")
mov2=input("enter you 2ed movie name :")
mov3=input("enter you 3rd movie name :")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies) 

#Questin 2 
