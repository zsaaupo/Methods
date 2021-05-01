"""
List Method
"""
print(__doc__)
a = [1, 2, 3, 4, 5, "Hello", "Python"]
b = [6, 7, 8, 9, "hello", "python"]
d = [1, 2, 3, 4, 5, "Hello", "Python"]

# add item as last value of lint  
a.append(0)
print(a)
b.append(7)
print(b)

#clear list
c = [6, 7, 8, 9, "hello", "python"]
c.clear()
print(c)

# copy list
c = b.copy()
print(c)

# count item
print(b.count(7))
print(a.count(5))

# extend a list with anothor
d.extend(b)
print(d)

# find index number
print(a.index(5))
print(b.index(7))
print(a.index(0))

# add item by index
a.insert(5, 7)
print(a)
b.insert(3, "thony")
print(b)

# move item form list by index
a.pop(0)
print(a)
e = b.pop(4) # move from "b" to "e"
print(e)

# remove from list by item
a.remove(2)
print(a)
b.remove(7)
print(b)

# reverse list item
d.reverse()
print(d)
b.reverse()
print(b)

# sorting list
f = [2, 4, 8, 5, 97, 9, 5, 48]
f.sort()
print(f)
f.sort(reverse=True) # reverse by sort
print(f)

"""
END
"""