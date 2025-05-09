lst = [1,2,3,4,5,6,7,8,9,10]
lst1 = lst[0:5]

print("Extracted first five elements from the list: ", lst1)
lst1.reverse()
print("Reversed extracted elements: ", lst1)


# reverse() methos change the index only it does not return new list, it return none that why
# print("Reversed extracted elements: ",lst1.reverse()) cannot use this line
# to make we have to do print("Reversed extracted elements: ", lst1)  like that