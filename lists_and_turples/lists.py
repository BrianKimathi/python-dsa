list1 = [1,2,2,3,4,2]
m_list = ["kim", "zagger"]

c_list = list()

print(list1)
print(list1[0]) # get first element
print(list1[-1]) # get last element

list1.append({'name' : 'cian'})
print(list1)

list2 = list1.copy()
print(list2)

# list1.extend(m_list)
# print(list1)

print(list1.index(2))
list1.insert(2, 2)
print(list1.count(2))

list1.pop()

print(list1)

list1.remove(2)
print(list1)

list1.reverse()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.remove(2)
print(list1)

del list1[0]
print(list1)

del list2
print(list2)