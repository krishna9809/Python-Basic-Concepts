# 1.Selection Sort

# def selection_sort(lst):
#     n  = len(lst)
#     for i in range(n):
#         min_pos = i
#         for j in range(i+1,n):
#             if lst[j]<lst[min_pos]:
#                 min_pos = j
        
#         temp = lst[i]
#         lst[i] = lst[min_pos]
#         lst[min_pos] = temp
    
# lst = [8,7,6,54,3,2,1,0]

# selection_sort(lst)
# print(lst)



# 2. factorial without recursion 

# def fact(n):
#     if n == 0:
#         return 1
    
#     fact = 1
#     for i in range(1,n+1):
#         fact = fact*i
    
#     return fact

# n = int(input("enter the no:"))
# print(fact(n))



# 3. factorial with Recursion 

# def fact_rec(n):
#     if n==0:
#         return 1
    
#     return n*fact_rec(n-1)

# n = int(input("enter the no:"))
# print(fact_rec(n))



# 4. prime no.

# def prime(n):

#     for i in range(2,n):
#         if n%i==0:
#             print("No is not prime")
#             break
#     else:   
#        print("No. is prime")

# n = int(input("enter the no:"))
# prime(n)



# 5. calculate the uppercase,lowercase,digit

# str = input("Enter a sentence:")
# d,u,l = 0,0,0

# for c in str:
#     if c.isdigit():
#        d =d+1
#     elif c.isupper():
#         u = u+1
#     elif c.islower():
#         l = l+1
# print("no. of digit:",d)
# print("no. of uppercase:",u)
# print("no. of lowercase:",l)




# 6.leap year or not

# year = int(input("Enter the Year:"))

# if(year%100==0) and (year%400==0):
#     print("yes! year  is leap year")
# elif(year%4==0) and (year%100!=0):
#     print("Yes! year s leap year")
# else:
#     print("Year is not leap year")



# 7. Swap the variable without temp

# a = 10
# b = 20

# a = a+b
# b= a-b
# a = a-b

# print(a)
# print(b)




# 8. Implement Binary technique

# def binary(lst,find):
#     start = 0
#     end = len(lst) - 1

#     while(start<=end):
#         mid = start+end//2
#         if lst[mid] == find:
#             return 1
#         elif lst[mid] > find:
#             end = mid - 1
#         else:
#             start = mid + 1

#     return 0

# lst = [2,3,4,5,67,7]
# result = binary(lst,4)

# if result ==1:
#     print("Element Found")
# else:
#     print("Element Not found")




# 9. compute average use try case 

# def average(lst):
#     sum = 0
#     for i in lst:
#         sum = sum + i
#     try:
#         print(sum/len(lst))
#     except:
#         print(0.0)

# lst = []
# average(lst)




# 10. Tower of Hanoi 

# def TOH(num,start,aux,end):
#     if num ==1:
#         print("Disk 1 move from rod {} to rod {}".format(start,end))
#         return
    
#     TOH(num-1,start,end,aux)
#     print("Disk {} mmve from rod {} to rod {}".format(num,start,end))
#     TOH(num-1,aux,start,end)

# disk = int(input("Enter the no. of disk:"))
# TOH(disk,"A","B","C")





# 11. Sieve of Eratosthenes

# def prime_sieve(n):
#     prime = [0 for i in range(101)]
#     for i in range(2,n+1):
#         if prime[i] == 0:
#             for j in range(i*i,n+1,i):
#                 prime[j] = 1
    
#     for i in range(2,n+1):
#         if prime[i] == 0:
#             print(i,end=' ')

# n = int(input("Enter the range to find prime numbers:"))
# prime_sieve(n)


# 12. Fabonnaci Series without Recursion

# def Fabonnci_series(n):
#     a = 0
#     b = 1
#     print(a)
#     print(b)
#     for i in range (2,n):
#         c = a+b
#         a = b
#         b = c
#         print(c)

# n = int(input("Enter the no:"))
# Fabonnci_series(n)




# 13. Fabonnaci Series with Recursion

# def fab_rec(n):
#     if n<=1:
#         return n
    
#     return fab_rec(n-1) + fab_rec(n-2)

# n = int(input("Enter the no:"))
# for i  in range(n):
#     print(fab_rec(i))



# 14. Merge sort

# def Merge(left,right):
#     result = []
#     i,j = 0,0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i = i + 1
#         else:
#             result.append(right[j])
#             j = j+1
    
#     result = result + left[i:]
#     result = result + right[j:]
#     return result

# def merge_sort(lst):
#     if len(lst)<=1:
#         return lst
#     mid = int(len(lst)/2)
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return Merge(left,right)

# lst = [2,3,0,49,5,60,7,8]

# print(merge_sort(lst))