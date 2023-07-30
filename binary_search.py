def binary(lst,find):
    start = 0
    end = len(lst) - 1

    while start<=end:
        mid = (start+end)//2

        if lst[mid] == find:
            return 1
        elif lst[mid] > find:
            end = mid -1
        else:
            start = mid + 1

    return 0

lst = [1,2,3,4,5,6,7]
result = binary(lst,8)

if result == 1:
    print("no. is found")
else:
    print("no. is not found")           

