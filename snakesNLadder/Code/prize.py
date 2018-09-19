

def findSmallest(arr):
    if 1 in arr:
        return "Fake Offer!"
    max_possible = sum(arr)+max(arr)
    res = max(arr) + 1
    new_arr = []
    for i in arr:
        new_arr += [i] * int(max_possible / i)
    print(new_arr)
    for i in range (0, len(new_arr)):
        if res> max_possible:
            return "Fake Offer!"
        elif new_arr[i] <= res:
            res = res + new_arr[i]
        else:
            break
    return res