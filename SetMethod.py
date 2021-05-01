"""
Set Method
"""
print(__doc__)

a = {1, 2, 3, 4, 5, "Hello", "Python"}
b = {6, 7, 8, 9, "hello", "python"}
d = {1, 2, 3, 4, 5, 6,}
e = {1, 2, 0, 7, 8, 5}
print(a)
print(b)
print(type(a))
print(type(b))

# add item to set
a.add(7)
print(a)
b.add(1)
print(b)

# copy set
c = b.copy()
print(c)

# clear set
c.clear()
print(c)

# remove set item from another set
print(d.difference(e))
print(e.difference(d))

# remove set item from another set and save the output value
d.difference_update(e)
print(d)

# delete a itel
e.discard(0)
print(e)

# intersection (take all common item of tow set)
f = {1, 2, 3, 4, 5, 6,}
g = {1, 2, 0, 7, 8, 5}
print(f.intersection(g))
print(g.intersection(f))

# intersection and save
f.intersection_update(g)
print(f)

# cheking common
print(d.isdisjoint(e))
print(a.isdisjoint(b))

# subset check
print(f.issubset(g))

# move item
g.pop()
print(g)

# remove item
g.remove(1)
print(g)

# sum tow set's all item
i = {1, 2, 3, 4, 5, 6,}
j = {1, 2, 0, 7, 8, 5}
print(i.symmetric_difference(j))

# sum tow set's all item and save
i.symmetric_difference_update(j)
print(i)

# union (take all item of tow set)
k = {1, 2, 3, 4, 5, 6,}
l = {1, 2, 0, 7, 8, 5}
print(k.union(l))

# take all item of tow set and save (union and update)

k.update(l)
print(k)

"""
END
"""