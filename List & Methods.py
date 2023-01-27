a=["osama","ahmed","sayed","ali","mahmoud"]
b=["osama","ahmed","sayed","ali","mahmoud"]
print(f"{a[0]}\n{a.pop(0)}\n{a[-1]}\n{a.pop(-1)}")
print(f"{b[0:5:2]}\n{b[1:5:2]}")
c=["osama","ahmed","sayed","ali","mahmoud"]
print(f"{c[1:4]}\n{c[-2]} {c[-1]}")
d=["osama","ahmed","sayed","ali","mahmoud"]
e=["osama","ahmed","sayed","elzero","elzero"]
print(e)
l=["osama","ahmed","sayed"]
l.insert(0,"test")
l.insert(4,"teto")
print(l)
m=["osama","ahmed","sayed","elzero","elzero"]
m.remove("osama")
m.remove("ahmed")
print(m)
m.remove("elzero")
print(m)
o=["osama","ahmed","sayed","elzero","elzero"]
b=["osama","ahmed","sayed","elzero","elzero"]
q=["osama","ahmed","sayed","elzero","elzero"]
o.extend(b)
o.extend(c)
print(o)
r=["osama","ahmed","sayed","elzero","elzero"]
r.sort()
print(r)
r.sort(reverse=True)
print(r)
w=["osama","ahmed","sayed","elzero","elzero"]
print(w.count("w"))
program=["html","css","js","python",["django","flask","web"]]
print(f"{program[4][0]}\n{program[4][-1]}")


