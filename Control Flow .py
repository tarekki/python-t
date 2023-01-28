num_f=int(input())
num_s=int(input())
operators=input()
if operators=="+":
    print(num_f+num_s)
elif operators=="*":
    print(num_f*num_s)
elif operators=="/":
    print(num_f/num_s)
else:
    print(num_f-num_s)
age=17
if age >16 :print("accepted")
else:print("not accepted") 
age=int(input())
if age<100:
    print(f"your age in month is {age*12}\n in week {age*48}\n in days {age*365} \n in minutes {age*525600}")
else:
    print("error")
countrties=["syria","lebanon","usa","canada"]
discount=30
price=1000
country=input("what is your country:")
if country in countrties:
    print(f"you have sale about {price*0.03} %") 
else:
    print("there is no sale")