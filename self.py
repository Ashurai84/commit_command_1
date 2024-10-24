# # name=input("My name is :")
# # Age=int(input("my age is :"))
# # marks=float(input("I get max:"))
# # print("welcome =", name)
# # print("Your age =", Age)
# # print("congratulations you got =", marks)


# # first=int(input("Enter first = "))
# # second=int(input("Enter second = "))

# # print("sum = ", first + second)





# #Print the sum of side of square
# side =  float(input("enter area of square:",  ))
# print('area = ',side*side) 

# #strings
# str1 = "n tbhis is the string .\nmy name uis"
# print(len(str1))


# #INDEXING

# str ="Apna college"
# ch= str[0]
# print(ch)

# #Slicing
# str ="Ashutosh"
# print(str[-8:-3])#Negative slicing
# print(str[2:7])


# #Sring functions
# str ="my name is ashutosh" #Returns true str if str ends with subsitute
# print(str.endswith("osh"))
# print(str.capitalize())#Capitalize the starting word of sentence
# print(str.replace("name","namm"))#used to change the word from sentence 


# #Conditional statement
# light = input("what is the color of light :")

# print(light)

# if(light =="red"):
#   print("stop")
# elif(light =="yellow"):
#   print("start")
# elif( light =="green"):
#   print("gooo!!!")
# else:
#   print("light is broken ")


# #Nesting
# whether= input("What is today whether: ")

# friends= True

# if whether =="sunny":
#   print("go for a walk and go to gym")
# else:
#   print("play with friends ")
# if whether == "rainy":
#   print("read books")
# else:
#   print("eat maggies")

# #WAP to find the greatest o]f 4 numbers input by user
# a=int(input("Enter your first digit: "))
# b=int(input("Enter your  second digit: "))
# c=int(input("Enter your third digit: "))
# d=int(input("Enter your  forth digit: "))

# if(a>b and a>=c):
#   print("First number is big ",a)
# elif(b>c and b>=d):
#   print("second is bigger",b)
# elif(c>d and c>=a):
#   print("third is biiger",c)
# else:
#   print("fourth is biiger",d)

#  #wap  to take in the ,  and display the grade as per following rules:

# marks=int(input("Enter your   marks :"))
# if(marks >=90 ):
#   grade ="A"
# elif(marks >=80 ):
#   grade ="B"
# elif(marks >=70):
#   grade="C"
# else:
#   grade="D"
# print("Your marks is -> ",grade)

#LISTS AND TUPLES 

# #overview of lists
# a=[1,2,3,4,5,"hello"]
# print(a[5])


# # Tuplessss

# tup=(1,2,3,4,3,4,4)
# tup=tup.count(4) # it count how many numbers are there in tuple
# print(tup)


# A=(2,1,3,1,2,3,)
# print(A.index(3)) # find the index number 




#  #DEFING OBJECTS

# class person:
#     def __inti__(self,name,age):
#         self.name=name
#         self.age=age
# p1=person("Ashutosh",18)
# p2=person("VRUTII",18)

# print(p1.name)
# print(p1.age)



# print(p2.name)
# print(p2.age)



# DICTIONARY $ SETSS


dict={
    "name":  " ashutosh ",
    "topics":  "Dictionary",
    "subjects":  ["python","java","css"],

}

null_dict ={} #null orempty dictonary 
null_dict["name"] = "ashutosh" # we can write in empty also or null
print(null_dict) 
#for changes
dict["name"] = " ashu " #overwrite
dict[" surname"] = "Rai"
print(dict)













 