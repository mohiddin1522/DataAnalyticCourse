li = [1,2,3,8,9,19,44,33,4,5,6,36,7]

print(li)
li.append(8)
li2 = li.copy() #copying list

li.clear() #clearing list
print(li)
print(li2)

li2.sort() #sorting list
print(li2)

li2.reverse() #reversing list
print(li2)

print(li2.index(8))  #index of 8 in list

print(li2.count(8))  #count of 8 in list

li2.pop() #removes last element from list
print(li2)

li2.remove(2) #removes 2 from list
print(li2)

li2.insert(2, 5) #inserting 5 at index 2
print(li2)

