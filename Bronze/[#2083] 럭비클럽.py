#2083 럭비 클럽
while True:
    name, age, weight = input().split()
    weight = int(weight); age = int(age)
    if name=="#" and age ==0 and weight == 0 :
        break
    if age > 17 or weight >= 80:
        print(name+ ' ' +"Senior")
    else:
        print(name+' '+"Junior")


