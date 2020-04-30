def findMaximum(list):

    maximum = list[0]
    for x in list:
        if x > maximum:
            maximum = x
    return maximum
list = [ 2,4,6,8]
print(findMaximum(list))
