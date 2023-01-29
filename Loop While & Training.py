num=int(input())
if num<0:
    print("error")
else:
    while num<=10:
        num=num-1
        if num==6:
            continue
        elif num==0:
            break
        print(num)
print("*"*60)
count=0
sum=2
friends=["mohamed","ali","kareem","Maher","samer"]
while count!=2:
    if friends[count].lower():
        count+=1
    continue
while sum!=len(friends):
    print(friends[sum].capitalize())
    sum+=1
print(f" count of discard is {count}\n number of sum is {sum}")
print("*"*50)
skills=["html","css","javascript","php","python"]
for i in range(len(skills)):print(skills[i])
myfriends=[""]
tern=4
while tern>0:
    n=input().strip()
    if n.isupper():
        print("invalid name")
        continue
    elif n.islower():
        myfriends.append(n.capitalize())
        print(f"friend {n.capitalize()} added=> 1st letter become capital")
    elif n.istitle():
        myfriends.append(n)
        print(f"friend {n} added")
    tern-=1
    print(f"names left in list is {tern}") if tern > 0 else print("all your friends added")




    
    



