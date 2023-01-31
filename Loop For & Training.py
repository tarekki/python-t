nums=[15,81,5,17,20,21,13]
nums.sort(reverse=True)
count=0
for i in range(len(nums)):
    if nums[i]%5==0:
        count+=1
        print(f"{count}=>{nums[i]}")
print("all numbers printed")
print("*"*125)
for k in range(1,21):
    if k==6:
        continue
    elif  k==8:
          continue
    elif k==12:
        continue      
    elif k<10:
       print(str(k).zfill(2))
    else:
        print(k)
print ("loop complete")
print("*"*125)
my_ranks={
     'math' : 'A',
     'science' :'B',
     'drawind': 'A',
     'sport': 'C'
     }
ranks={
        "A":100,
        "B":80,
        "C":40
      }
total=0
for l,k in my_ranks.items():
    print(f"my rank in {l} is {k} and this equal {ranks[k]} points")
    total += ranks[k]
print(f"tf is {total}")
print("*"*150) 
students = {
  "Ahmed": {
    "Math": "a",
    "Science": "d",
    "Draw": "b",
    "Sports": "c",
    "Thinking": "a"
  },
  "Sayed": {
    "Math": "b",
    "Science": "b",
    "Draw": "b",
    "Sports": "d",
    "Thinking": "a"
  },
  "Mahmoud": {
    "Math": "d",
    "Science": "a",
    "Draw": "a",
    "Sports": "b",
    "Thinking": "b"
  }
}
ranks={
        "a":100,
        "b":80,
        "c":40,
        "d":20
 }
for namen,data in students.items():
    print("------------------------------")
    print(f"-- Student Name => {namen}")
    print("------------------------------")
    totali=0
    for subject,rank  in data.items():
        print(f"- {subject} => {ranks[rank]} points")
        totali+=ranks[rank]
print(f"total points for {namen} is {totali}")

