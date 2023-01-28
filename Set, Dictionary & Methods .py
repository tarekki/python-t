my_li,unique_list=[1,5,4,3,3,2,1],[1,5,4,3,2]
print(f"{unique_list}\n{type(unique_list)}\n{unique_list[0:4]}")
nums={1,2,3}
let={"a","b","c"}
print(f"{nums.union(let)}\n{nums|let}")
x={1,2,3}
print(x)
x.clear()
print(x)
x.add("a")
x.add("b")
print(x)
x.discard("c")
print(x)
y={1,2,3}
z={1,2,3,4,5,6}
print(z.issuperset(y))
user={
    "java":"75%",
    "c": "90%",
    "python":"60%"
}
print("prgress with java :"+ user["java"])
print( "progress with c :"+user["c"] )
print("progress with python"+ user["python"])