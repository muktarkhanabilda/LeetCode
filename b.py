n = str(input())
kn = 0
for i in n:
    kn+=ord(i)
if(kn > 300):
    print("It is tasty!")
else:
    print("Oh, no!")