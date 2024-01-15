tup = tuple()
print(tup)

tup1 = (2)
print(type(tup1))

tup2 = (2,)
print(type(tup2))

name = "briankimathi"
tup3 = tuple(name)
print(tup3)

list1 = [7,1,2,3,4]
tup4 = tuple(list1)
print(tup4)


print(tup3.count("i"))

print(tup3.index("i"))

print(tup3[2:8])


del tup1

m_dict = {'name':'kim', 'age':23}

tup5 = tuple(m_dict.items())
print(tup5)

print(max(tup4))
print(min(tup4))

print(sorted(tup4, reverse=True))