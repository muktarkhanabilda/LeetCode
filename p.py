yers = int(input())
month = int(input())
def monthnn(yers,month):
    l = [1,3,5,7,8,10,12]
    p = [4,6,9,11]
    if yers == 2020:
        if month == 2:
            print("Yers 2020")
            print("")
            print("This month 29 days")
    for i in l:
        if i == month:
            print("Yers " + str(yers))
            print("")
            print("This month 31 days")
    for i in p:
        if i == month:
            print("Yers " + str(yers))
            print("")
            print("This month 30 days")
    if month == 2:
        print("Yers " + str(yers))
        print("")
        print("This month 28 days")
monthnn(yers,month)

