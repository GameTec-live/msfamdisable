print("Dbeug codes: User007, AT642")

code = input("Input Debug Code!")
if code == 'User007':
    data = 1
    print("Debug mode!")
    input("Comming Soon!")
elif code == 'AT642':
    x = 1
    w = open("data.txt", 'w')
    w.write(str(x))
    w.close()
    print("Restoring the Data.txt file!")
else:
    data = 2
    exit()