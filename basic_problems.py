# # 1. Check Even or Odd

# a = int(input("Enter a number: "))

# if a%2==0:
#     print("Your Number is Even")
# else:
#     print("Your Number is Odd")

# #output ==>
# # Enter a number: 5
# # Your Number is Odd

# # 2. Check Postive, negative or Zero

# a = int(input("Enter a number: "))

# if a<0:
#     print("Your Number is Negative")
# elif a==0:
#     print("Number Equal to Zero")
# else:
#     print("Your Number is Postive")

# #output ===>
# # Enter a number: 5
# # Your Number is Postive

# # 3. Factorial of a number

# a = int(input("Enter a number: "))

# if a == 0 or a == 1:
#     print("Factorai is 1")
# else:
#     fact = 1
#     i = a
#     while i>0:
#         fact = fact * i
#         i = i - 1
#     print("Factorial is ",fact)

# #output ==>
# # Enter a number: 5
# # Factorial is  120

# # 4. Reversing a number

# a = int(input("Enter a number: "))

# rev = 0
# while a > 0:
#     rem = a%10
#     rev = rev*10 + rem
#     a = a//10

# print("Your reverse is ",rev)

# #output ==>
# # Enter a number: 345
# # Your reverse is  543

# # 5. Check if is it palindrome or not

# a = int(input("Enter a number: "))
# temp = a
# rev = 0
# while a > 0:
#     rem = a%10
#     rev = rev*10 + rem
#     a = a//10

# if rev == temp:
#     print("Your Number is Palindrome")
# else:
#     print("Your Number is not Palindrome")

# # output ==>
# # Enter a number: 333
# # Your Number is Palindrome

# # 6. Fabonacci Series

# num = int(input("Enter a number: "))

# if num <=0:
#     print("Incorrect Input")
# elif num == 1:
#     print(0)
# else:
#     a = 0
#     b = 1
#     print(a)
#     print(b)
    
#     for i in range(2,num):
#        c = a + b
#        print(c)
#        a = b
#        b = c
        
# #output ==>
# # Enter a number: 5
# # 0
# # 1
# # 1
# # 2
# # 3





# i=0
# while i< 3:
#  print(i)
# i += 1

def cube(x):
  return x * x * x
x = cube(3)
print x