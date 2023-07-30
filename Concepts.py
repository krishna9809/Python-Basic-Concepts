# print("krishna") 
# print("krishna sharma") 

# # output
# # krishna
# # krishna sharma

# #Variables

# employee_name = "sam"
# print(employee_name)
# employee_name = "matt"
# print(employee_name)

# #output 
# # sam
# # matt

# #data type 
# a = 100
# print(type(a))
# b = 3.34
# print(type(b))
# c = True
# print(type(c))
# d = "sam"
# print(type(d))
# e = 2+5j
# print(type(e))

# #output ==>
# # <class 'int'>
# # <class 'float'>
# # <class 'bool'>
# # <class 'str'>
# # <class 'complex'>

# # operators
# a = 10
# b = 20
# #arithmatic operators
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)

# # output ==>
# # 30
# # -10
# # 200
# # 0.5

# #relational operators
# print(a>b)
# print(a<b)
# print(a==b)
# print(a!=b)

# #output ==>
# # False
# # True
# # False
# # True

# #logical operators
# a = True
# b = False
# print(a and b)
# print(a or b)

# #output ==>
# # False
# # True

# #string

# s1 = 'hello'
# print(s1)
# s1 = "hello"
# print(s1)
# s1 = '''this is multi
# line string'''
# print(s1)
# print(s1[0])
# print(s1[0:3])

# #output ==>
# # hello
# # hello
# # this is multi
# # line string
# # t
# # thi

# #functions in string

# str = "My Name, Is, Krishna"

# print(len(str))
# print(str.upper())
# print(str.lower())
# print(str.replace('Is','Great'))
# print(str.count('Name'))
# print(str.find('Krishna'))
# print(str.split(','))

# #output ==>
# # 20
# # MY NAME, IS, KRISHNA
# # my name, is, krishna
# # My Name, Great, Krishna
# # 1
# # 13
# # ['My Name', ' Is', ' Krishna']

# # Tuples in Python

# tp1 = (1,'a',True)
# print(tp1)
# print(tp1[0])
# print(tp1[1:3])
# print(tp1[-1])

# #output ==>
# # (1, 'a', True)
# # 1
# # ('a', True)
# # True
# # tp1[2] = 'h throw an ==> error assingnment operator does not work on tuple

# #operation on tuple

# tup1 = (1,2,3,3,4)
# print(len(tup1))

# tup2 = (5,5,6,7,7)
# print(tup1 + tup2)

# print(tup1*3)
# print(tup1*3 + tup2) 

# #output ==>
# # 5
# # (1, 2, 3, 3, 4, 5, 5, 6, 7, 7)
# # (1, 2, 3, 3, 4, 1, 2, 3, 3, 4, 1, 2, 3, 3, 4)
# # (1, 2, 3, 3, 4, 1, 2, 3, 3, 4, 1, 2, 3, 3, 4, 5, 5, 6, 7, 7)

# #functions of tuple

# print(min(tup1))
# print(max(tup2))
# print(tup1.count(3))
# print(tup1.index(2))

# #output ==>
# # 1
# # 7
# # 2
# # 1

# #List in pyhton

# l1 = [1,'a',True]
# print(type(l1))
# print(l1)
# print(l1[1])
# print(l1[-1])
# print(l1[1:3])
# print(len(l1))

# #output
# # <class 'list'>
# # [1, 'a', True]
# # a
# # True
# # ['a', True]
# # 3

# #modifying list

# l1.append("aa")
# print(l1)

# l1.pop()
# print(l1)

# l2 = [1,5,3,4]
# l2.reverse()
# print(l2)

# l2.insert(2,'d')
# print(l2)

# l3 = ["apple","mango","banana"]
# l3.sort()
# print(l3)

# print(l2+l3)
# print(l3*3)

# #output ==>
# # [1, 'a', True, 'aa']
# # [1, 'a', True]
# # [4, 3, 5, 1]
# # [4, 3, 'd', 5, 1]
# # ['apple', 'banana', 'mango']
# # [4, 3, 'd', 5, 1, 'apple', 'banana', 'mango']
# # ['apple', 'banana', 'mango', 'apple', 'banana', 'mango', 'apple', 'banana', 'mango']

# # Dictionary 

# fruit = {"apple":10,"orange":20}
# #type
# print(type(fruit))
# print(fruit)
# #printing keys
# print(fruit.keys())
# # printing values
# print(fruit.values())
# print(fruit.items())
# #insert new 
# fruit["mango"] = 50
# print(fruit)
# fruit["apple"] = 100
# print(fruit)

# #output ==>
# # <class 'dict'>
# # {'apple': 10, 'orange': 20}
# # dict_keys(['apple', 'orange'])
# # dict_values([10, 20])
# # dict_items([('apple', 10), ('orange', 20)])
# # {'apple': 10, 'orange': 20, 'mango': 50}
# # {'apple': 100, 'orange': 20, 'mango': 50}

# # functions of dictionary

# #update funnction
# fruit1 = {"apple":10,"mango":20}
# fruit2 = {"orange":30,"banana":40}
# fruit1.update(fruit2)
# print(fruit1)
# #pop function
# fruit3 = {"apple":10,"banana":40}
# fruit3.pop("apple")
# print(fruit3)

# #output ==>
# # {'apple': 10, 'mango': 20, 'orange': 30, 'banana': 40}
# # {'banana': 40}


# #Set

# s1 = {1,"a",True}
# print(type(s1))

# #output == >
# # <class 'set'>

# #operation in set

# #add element
# s1.add("hello world")
# print(s1)

# #update multiple element
# s1.update([2,3,4,5,"aaa"])
# print(s1)

# #remove element
# s1.remove(1)
# print(s1)

# #functions in set

# #union
# s2 = {1,2,3,4}
# s3 = {"a","b"}

# s4 = s2.union(s3)
# print(s4)

# #intersection
# s2 = {1,2,3,4}
# s3 = {2,4}

# s4 = s2.intersection(s3)
# print(s4)

# #output ==>
# # {'a', 1, 'hello world'}
# # {1, 2, 3, 4, 5, 'aaa', 'hello world', 'a'}
# # {2, 3, 4, 5, 'aaa', 'hello world', 'a'}
# # {1, 2, 3, 4, 'a', 'b'}
# # {2, 4}

# # if Statements in python
# a = 10;
# b = 20;

# if a < b:
#     print("a is less then b")

# #output ==>
# # a is less then b

# # if-else 
# a = 30

# if a < b:
#     print("a is less then b")
# else:
#     print("a is greater then b")

# #output ==>
# # a is greater then b

# #elif statement use when we have multiple conditions

# # ques => Find the largest from three numbers
# a = 10
# b = 40
# c = 30


# if (a>b and a<c):
#     print("a is larger from all")
# elif ( b>a and b>c):
#     print("b is larger from all")
# else:
#     print("c i s larger from all")

# #output ==>
# # b is larger from all

# # if statement in tuple

# t1  = (1,2,4,'a',True)

# if 2 in t1:
#     print("yes! 2 is in the tuple t1")

# # if statement in list

# l1 = [1,2,3,4]

# if l1[1] == 2:
#     l1[1] = l1[1] + 100

# print(l1)

# # if with dictionary

# d1 = {"apple":1,"banana":2,"gauva":3}

# if d1["banana"] == 2:
#     d1["banana"] = d1["banana"] + 100

# print(d1)

# #output ==>
# # yes! 2 is in the tuple t1
# # [1, 102, 3, 4]
# # {'apple': 1, 'banana': 102, 'gauva': 3}
 

# #looping in python
# # ==> looping is a statement are used to repeat a task multiple times

# # while
# i= 0
# while i<=10:
#     print(i)
#     i = i+1

# #output ==>
# # 0
# # 1
# # 2
# # 3
# # 4
# # 5
# # 6
# # 7
# # 8
# # 9
# # 10

# i = 1
# n = 2

# while i<=10:
#     print(n, "x", i ,"=", i*n)
#     i = i + 1

# #output ==>
# # 2 x 1 = 2
# # 2 x 2 = 4
# # 2 x 3 = 6
# # 2 x 4 = 8
# # 2 x 5 = 10
# # 2 x 6 = 12
# # 2 x 7 = 14
# # 2 x 8 = 16
# # 2 x 9 = 18
# # 2 x 10 = 20

# #while loop in list

# l2 = [1,2,3,4,5]
# i = 0
# while i <= len(l1):
#     l2[i] = l2[i] + 100
#     i = i+1
# print(l2)

# #output ==>
# # [101, 102, 103, 104, 105]


# # for loop = > it is use to iterate over a sequence(tuple, list, dictionary)

# l3 = ["apple","banana","watermelon"]

# for i in l3:
#     print(i)

# #output ==>
# # apple
# # banana
# # watermelon

# #nested for loop
# l4 = ["blue","red","black"]
# l5 = ["book","table","mobile"]

# for i in l4:
#     for j in l5:
#         print(i,j)

# #output ==>
# # blue book
# # blue table
# # blue mobile
# # red book
# # red table
# # red mobile
# # black book
# # black table
# # black mobile






