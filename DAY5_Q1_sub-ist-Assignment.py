#case 1
lst1 = [1,5,6,4,1,2,3,5]
lst2 = [1,5,6,5,1,2,3,6]

lst = [1,1,5]
count = 0
r=0
for x in lst:
    for y in lst1[r:]:
        r+=1
        if (x==y):
            count+=1
            break;
        else:
            pass
        

if(count==3):
    print("it’s a Match")
else:
    print("it’s Gone")

#case 2

count = 0
r=0
for x in lst:
    for y in lst2[r:]:
        r+=1
        if (x==y):
            count+=1
            break;
        else:
            pass
        

if(count==3):
    print("it’s a Match")
else:
    print("it’s Gone")

