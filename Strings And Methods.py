name = "'tarek'"
age = '"23" '
country= 'damascus'
print('"'"hello " + name + "," "how you doing \ " '""" ' "your age is " + age + "+ " + "and your country is: " + country)
print('"'"hello " + name + "," "how you doing \ " '\n' '""" ' "your age is " + age + "+ " '\n' + "and your country is: " + country)
name = "'Elzero'"
print(f"{name[2]}\n{name[3]}\n{name[6]}")
print(f"{name[2:5]}\n{name[1:7:2]}\n{name[-3:-8:-2]}")
name = '"#@#@Elzero#@#@"'
print(name[5:11])
c="9"
print(c.rjust(4,"0"))
a="OSamA"
b="osaMA_alzero"
print(a.rjust(20,"#"))
print(b.rjust(20,"#"))
d="OSamA"
e="osaMA_alzero"
print(a.swapcase())    
print(b.swapcase())   
l="i love python and althogh love elzero web school"
print(l.count("love"))
m="elzero"
print(m.index("z"))
n="i <3 python and althogh <3 elazero web school"
print(n.replace("<3","love",1))
o="i <3 python and althogh <3 elazero web school"
print(o.replace("<3","love"))
j="tarek"
l=23
k="damas"
print(f"my name is {j}, and my age is {l}, and my country is {k} ")
