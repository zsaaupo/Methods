"""
Dictionary Method
"""
print(__doc__)
a = {"a" : "1", "b" : "2", "c" : "3",}
g = a.copy()
print(a)
print(g)
print(type(a))

# copy dictionary
c = a.copy()
print(c)

# clear dictionary
c.clear()
print(c)

# assain a tuple value to every key
b = ("a", "b", "c", "d")
d = 7
e = dict.fromkeys(b, d)
print(e)

# get value by key
print(a.get("a"))
print(a.get("b"))
print(a.get("c"))

# show item
print(a.items())
print(e.items())

# change key value
a["a"] = 7
print(a)

# add dictonary item
a["x"] = 8
print(a)

# show keys
print(a.keys())
print(e.keys())

# move item
a.pop("x")
print(a)

f = a.pop("a")
print(f) # move only value

# move last key with value
a.popitem()
print(a)
h = a.popitem()
print(h)
print(type(h)) # but the data type change to tuple
print(a)

# show value or add key with value
print(g.setdefault("b"))
print(g.setdefault("x",7))
print(g)

# and item (key with value)
g.update({"y" : 8})
print(g)

# show values
print(g.values())
print(e.values())
print(a.values())

"""
END
"""