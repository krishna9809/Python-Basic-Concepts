# def merge(left,right):
#     result = []
#     i,j = 0,0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
        
#     result += left[i:]
#     result += right[j:]
#     return result

# def merge_sort(lst):

#     if(len(lst) <= 1):
#         return lst
    
#     mid = int(len(lst)/2)
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return merge(left,right)


# lst = [2,4,5,1,9,7,6,5]

# print(merge_sort(lst))

# def merge(left,right):
#     result = []
#     i,j = 0,0

#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j+= 1
        
#     result += left[i:]
#     result += right[j:]
#     return result

# def merge_sort(lst):
#     if (len(lst) <=1):
#         return lst
    
#     mid = int(len(lst)/2)
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return merge(left,right)

# lst = [2,4,5,1,9,7,6,5]

# print(merge_sort(lst))

# def binarySearch(Arr, s, e, find):
#     while s <= e:
#         mid = (s+e)//2  # Calculate the middle index of the list

#         if Arr[mid] == find:
#             return mid  # Element found at index mid
#         elif Arr[mid] > find:
#             return binarySearch(Arr, s, mid - 1, find)  # Search in the left half
#         else:
#             return binarySearch(Arr, mid + 1, e, find)  # Search in the right half
        
#     return -1  # Element not found

# # Example usage:                                      
# arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
# x = 23
# result = binarySearch(arr, 0, len(arr) - 1, x)
# if result != -1:
#     print("found")
# else:
#     print("Element not found.")

def palindrome(n):
    rev = 0
    temp = n

    while n>=0:
        rem = n%10 # 111%10 == 1 # 11%10 == 1 # 1%10 == 1
        rev = rev * 10 + rem # ==1 # == 11 # 110 + 1 = 111
        n = n//10 # 111//10 == 11 # 11//10 == 1 # 1 //10 == 0.1 == 0
    
    if rev == temp:
        print("no. is palindrome")
    else:
        print("No. is not palindrome")

n = int(input("Enter the Number:"))

palindrome(n)