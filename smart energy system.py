u = input("Enter username: ")
p = input("Enter password: ")

if u != "jashu" or p != "995910":
    print("exit")
    exit()
else:
    print("Login successful")
    
    n = int(input("Enter number of buildings to analyze: "))
    
    readings = []
    
    for i in range(n):
        x = int(input("Enter reading for building " + str(i+1) + ": "))
        readings.append(x)
    
    d = {"efficient": [], "moderate": [], "high": [], "invalid": []}
    
    for i in readings:
        if i < 0:
            d["invalid"].append(i)
        elif i <= 50:
            d["efficient"].append(i)
        elif i <= 150:
            d["moderate"].append(i)
        else:
            d["high"].append(i)
    
    t = sum([x for x in readings if x >= 0])
    
    print("\nEnergy usage classification:")
    print("efficient buildings:", d["efficient"])
    print("moderate buildings:", d["moderate"])
    print("high buildings:", d["high"])
    print("invalid buildings:", d["invalid"])
    
    print("\nTotal energy consumed:", t)
    print("Number of buildings analyzed:", n)
