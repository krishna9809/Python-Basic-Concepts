# def selection_sort(lst):
#     n = len(lst)

#     for i in range(n):
#         min_pos = i
#         for j in range(i,n):
#             if lst[j] < lst[min_pos]:
#                 min_pos = j
        
#         temp = lst[i]
#         lst[i] = lst[min_pos]
#         lst[min_pos] = temp

# lst = [2,4,5,6,0,1,7,5]

# selection_sort(lst)

# print(lst)

# def selection_sort(lst):

#     n = len(lst)

#     for i in range(n):
#         min_pos = i
#         for j in range(i,n):
#             if(lst[j] < lst[min_pos]):
#                 min_pos = j
        
#         temp = lst[i]
#         lst[i] = lst[min_pos]
#         lst[min_pos] = temp

# lst = [2,4,5,6,0,1,7,5]

# selection_sort(lst)

# print(lst)

def selction_sort(nums):
    n = len(nums)

    for i in range(n):
        min_pos = i
        for j in range(i,n):
            if(nums[j]<nums[min_pos]):
                min_pos = j
        
        temp = nums[i]
        nums[i] = nums[min_pos]
        nums[min_pos] = temp

nums = [3,5,1,0,6,3]
selction_sort(nums)
print(nums)