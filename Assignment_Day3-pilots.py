#!/usr/bin/python

#1)You all are Pilots, you want to land a plane safely, so altitude required for landing a plane is
#1000ft, it it is less than tell pilot to land the plane, or it is more than that but less than 5000ft ask
#the pilot to “come down to 1000ft”, else if it more than 5000ft ask the pilot to “go around and try
#later

val=int(input("Enter amount: "))
print(val)

if val==1000:
    print("Safe to Land")

elif val==4500:
    print("Bring down to 1000")

elif val==6500:
    print("Turn Around")

else:
    print("go around and try later")


