def Reverse(list):
    length = len(list)

    s = length

    new_list = [None] * length

    for item in list:
        s = s - 1

        new_list[s] = item

        return new_list

list = [4,5,7,9,10]
print(Reverse(list))
