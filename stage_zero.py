def stage_zero(arr):
    # highest = max(arr)
    # print(highest)
    highest = 0
    for i in arr:
        if i > highest:
            highest = i
    print(highest)

    return highest