li=[1, 2, 3, 9, 5]
li2=[4, 5, 6, 7]
li.append(6) # add element at the end of list
li.insert(2,7) # insert element in a remove value on particular place and add new value
li.extend(li2) # add list 2 at the end of list 1
li.index(5) # searches for the given element from the start of the list and returns its index
li.remove(5) # searches for the first instance of the given element and removes it
li.sort()  # sorts the list in place
li.reverse() # reverses the list in place
li.pop() # remove last element 
print(li)