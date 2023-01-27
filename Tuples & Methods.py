a ="tarek",
print(type(a))
fr=("osama","rami","karem")
b=str(fr)
print(b.replace("osama","elzero"))
print(fr)
print(type(fr))
print(len(fr))
nums=(1,2,3)
cha=("a","b","c")
newtouple=nums + cha
print(f"{len(newtouple)}\n{newtouple}")
t=(1,"a",2,3)
x,_,y,z=t
print(f"{x}\n{y}\n{z}")