"""
String Method
"""
print(__doc__)

a = "Hello Python"
b = "python"
e = "HELLO PYTHON"
x = "700$"
y = "007 jems"
z = "33"

c = b.capitalize()
print(c) # change 1st letter to capital

# convert all letter to lower case
d = a.casefold()
print(d) 
print(e.lower())

# string shifting
print(a.center(200))
print(b.center(200))

# count letter
print(a.count("l"))
print(a.count("o"))
print(a.count("h"))
print(d.count("h"))

# encode
print(a.encode())
print(b.encode())
print(c.encode())
print(d.encode())

# endswith (cheking the last letter or word or value)
print(a.endswith("n"))
print(b.endswith("python"))
print(c.endswith("."))

# checking the strating letter or word or value
print(a.startswith("H"))
print(b.startswith("py"))
print(c.startswith("."))

# expandtabs set indentation value
f = "Hello\tPython" # (\t) is indentetion
print(f)
print(f.expandtabs())
print(f.expandtabs(200))
print(f.expandtabs(100))
print(f.expandtabs(20))

# find index number
print(a.find("P"))
print(a.find("Python"))

# find index number
print(a.index("P"))
print(b.index("n"))

"""
is function start (checking function)
"""
# check all charecter is alphanumeric
print(a.isalnum())
print(b.isalnum())

# check all harecter is alphabet
print(a.isalpha())
print(b.isalpha())

# check all charecter is decimal

print(z.isdecimal())
print(a.isdecimal())
print(y.isdecimal())

# check all charecter is digit
print(z.isdigit())
print(y.isdigit())

# check all charecter is identifier
print(x.isidentifier())
print(a.isidentifier())
print(z.isidentifier())
print(b.isidentifier())

# lower case check
print(d.islower())
print(a.islower())

# numeric check
print(z.isnumeric())
print(x.isnumeric())

# check for do the full string is printable
print(f.isprintable())
print(a.isprintable())

#check for whitespace
l = "    "
print(l.isspace())
print(l.isspace())

#check str is follow the title rule
print(a.istitle())
print(e.istitle())

# check upper case
print(e.isupper())
print(a.isupper())

"""
is function end
"""

# change value or word or letter
a1 = a.maketrans(a, e)
print(a.translate(a1))
b1 = b.maketrans("py", "  ")
print(b.translate(b1))

# make 3 partition by base on word
print(a.partition("Py"))
print(x.partition("$"))
print(a.partition("null")) # null partition add left

print(a.rpartition("Py"))
print(x.rpartition("$"))
print(a.rpartition("null")) # null partition add right

# insert something in multi value variable
h = "i", "am", "Python"
print("-".join(h))
print(" ".join(h))

# add space or any single character left of string
print(z.ljust(20, "$"))
print(a.ljust(20),"007")
print(b.ljust(33, "P"))

# add space or any single character right of string
print(z.rjust(20, "$"))
print("007", a.rjust(20))
print(b.rjust(33, "P"))

# trim the string or delete selected charecter
i = "         Hello Python"
i1 = "0078issoss......,,,,,Python"
i4 = "0078issoss......,,,,,Python0078issoss......,,,,,"
print(i.strip())
print(i.strip("Hello "))
print(i1.strip("078iso.,"))
print(i4.strip("078iso.,"))

# trim the string or delete selected charecter from left
print(i.lstrip())
print(i.lstrip("Hello "))
print(i1.lstrip("078iso.,"))

# trim the string or delete selected charecter from right
i2 = "Hello Python         "
i3 = "Python0078issoss......,,,,,"
print(i2.rstrip())
print(i2.rstrip(" Python         "))
print(i3.rstrip("078iso.,"))

# replacing
g = "python is a python that a python"
print(g.replace("python", "thony"))
print(g.replace("python", "thon", 1))
print(g.replace("python", "thony", 2))

# find index nubmer of the last character
print(a.rfind("o"))
print(a.rfind("o", 1, 6)) # find index number of the character between index 1 to 6
print(a.rfind("z"))
# rindex
print(a.rindex("l"))
print(a.rindex("o", 1, 7)) # find index number of the character between index 1 to 7

# spliting
j = ("Hello, Pytone, hello, python thony")
print(a.split())
print(j.split(","))
print(j.split(",", 1))

print(a.rsplit())
print(j.rsplit(","))
print(j.rsplit(",", 1)) # split from right

# splite lines
k = "Hello Pyhton \nHello Human"
print(k.splitlines())
print(k.splitlines(True)) # (true) show full string

# inverse case of string
print(e.swapcase())
print(x.swapcase())
print(y.swapcase())
print(b.swapcase())

# convert to upper case every word's frist letter
print(g.title())
print(j.title())

# convert all character to upper case
print(b.upper())
print(a.upper())

# zfill (fill up the defined len with 0)
print(b.zfill(10))
print(a.zfill(100))

"""
END
"""