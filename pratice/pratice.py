# name = "naman"
# print(name ==  name[::-1])

# from collections import Counter
# print(Counter(name))

# nums = [1,2,3,4,5,5]
# nums.sort()
# print(nums)

# def second_max(nums):
#     nums = list(set(nums))
#     nums.sort()
#     return nums[-2]
# print(second_max(nums))


# sentenct = "hello world welcome to python programming"
# def countwordfreq(sentence):
#     words = sentence.split()
#     word_freq = Counter(words)
#     return word_freq
# print(countwordfreq(sentenct))

# groupdatabykey = [('a', 1), ('b', 2), ('a', 3), ('b', 4), ('c', 5)]
# def group_data_by_key(data):
#     grouped_data = {}
#     for key, value in data:
#         if key not in grouped_data:
#             grouped_data[key] = []
#         grouped_data[key].append(value)
#     return grouped_data
# print(group_data_by_key(groupdatabykey))


# def add(*args):
#     return sum(args)
# print(add(1,2,3,4,5,6))

# def keyvaluepair(**kwargs):
#     return kwargs
# print(keyvaluepair(a=1, b=2, c=3))


# class Animal:
#     def __init__(self,name, species):
#         self.name = name
#         self.species = species
#     def make_sound(self):
#         print("sounding")


# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name, species="Dog")
#         self.breed = breed
#     def make_sound(self):
#         print("Woof!")
# my_dog = Dog("Buddy", "Golden Retriever")
# print(my_dog.name)

# file = open("demo.txt","w")
# file.write("Hello you are creating first file!")
# file.close()
# file = open("demo.txt","r")
# file.seek(0)
# file = open("demo.txt","a")
# file.write("\nThis is second line.")
# file.close()
# file = open("demo.txt","r")
# content = file.read()
# print(content)


# class student:
#     def __init__(self,name,age,rollno):
#         self.name = name
#         self.age = age
#         self.rollno = rollno
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Roll No: {self.rollno}")

# student1 = student("naman", 20,101)
# student2 = student("rahul",32,102)
# student1.display()
# student2.display()

# class Bank:
#     def __init__(self, a_no,name,balance):
#         self.a_no = a_no
#         self.name = name
#         self.balance = balance
#     def deposit(self, amount):
#         if(amount < 0):
#             print("Amount be greater than 0")
#         else:
#             self.balance += amount
#             print(f"Deposited:{amount},New balance:{self.balance}")
#     def withdraw(self, amount):
#         if(amount > self.balance):
#             print("Insufficient balance")
#         else:
#             self.balance -= amount
#             print(f"Withdrawn:{amount},New balance:{self.balance}")
#     def display(self):
#         print(f"Account No: {self.a_no},Name:{self.name}, Balance:{self.balance}")
#     def edit(self,name):
#         self.name = name
#         print(f"Name update to {self.name}")

# data = []
# sbi = Bank(101,"naman",1000)
# sbi.deposit(500)
# sbi.withdraw(200)
# sbi.display()
# data.append(sbi.__dict__)
# file = open("bankdata.txt","w")
# file.write(str(data))
# file.close()
# file = open("bankdata.txt","r")
# content = file.read()
# print(content)


