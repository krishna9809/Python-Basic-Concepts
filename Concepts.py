print("krishna")
print("krishna sharma")

#Variables

employee_name = "sam"
print(employee_name)
employee_name = "matt"
print(employee_name)

#data type 
a = 100
print(type(a))
b = 3.34
print(type(b))
c = True
print(type(c))
d = "sam"
print(type(d))
e = 2+5j
print(type(e))


# operators
a = 10
b = 20
#arithmatic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#relational operators
print(a>b)
print(a<b)
print(a==b)
print(a!=b)

#logical operators
a = True
b = False
print(a and b)
print(a or b)


#string

s1 = 'hello'
print(s1)
s1 = "hello"
print(s1)
s1 = '''this is multi
line string'''
print(s1)
print(s1[0])
print(s1[0:3])

#functions in string

str = "My Name, Is, Krishna"

print(len(str))
print(str.upper())
print(str.lower())
print(str.replace('Is','Great'))
print(str.count('Name'))
print(str.find('Krishna'))
print(str.split(','))

# Tuples in Python

tp1 = (1,'a',True)
print(tp1)
print(tp1[0])
print(tp1[1:3])
print(tp1[-1])
# tp1[2] = 'h throw an ==> error assingnment operator does not work on tuple

#operation on tuple

tup1 = (1,2,3,3,4)
print(len(tup1))

tup2 = (5,5,6,7,7)
print(tup1 + tup2)

print(tup1*3)
print(tup1*3 + tup2) 

#functions of tuple

print(min(tup1))
print(max(tup2))
print(tup1.count(3))
print(tup1.index(2))

#List in pyhton

l1 = [1,'a',True]
print(type(l1))
print(l1)
print(l1[1])
print(l1[-1])
print(l1[1:3])
print(len(l1))

#modifying list

l1.append("aa")
print(l1)

l1.pop()
print(l1)

l2 = [1,5,3,4]
l2.reverse()
print(l2)

l2.insert(2,'d')
print(l2)

l3 = ["apple","mango","banana"]
l3.sort()
print(l3)

print(l2+l3)
print(l3*3)

# Dictionary 

fruit = {"apple":10,"orange":20}
#type
print(type(fruit))
print(fruit)
#printing keys
print(fruit.keys())
# printing values
print(fruit.values())
print(fruit.items())
#insert new 
fruit["mango"] = 50
print(fruit)
fruit["apple"] = 100
print(fruit)

# functions of dictionary

#update funnction
fruit1 = {"apple":10,"mango":20}
fruit2 = {"orange":30,"banana":40}
fruit1.update(fruit2)
print(fruit1)

#pop function
fruit3 = {"apple":10,"banana":40}
fruit3.pop("apple")
print(fruit3)

#Set

s1 = {1,"a",True}
print(type(s1))

#operation in set

#add element
s1.add("hello world")
print(s1)

#update multiple element
s1.update([2,3,4,5,"aaa"])
print(s1)

#remove element
s1.remove(1)
print(s1)

#functions in set

#union
s2 = {1,2,3,4}
s3 = {"a","b"}

s4 = s2.union(s3)
print(s4)

#intersection
s2 = {1,2,3,4}
s3 = {2,4}

s4 = s2.intersection(s3)
print(s4)

