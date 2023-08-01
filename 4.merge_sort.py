

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

