def billReport(count,customers,money):
    customers = sorted(customers.items())
    print(f"Day {count}")
    for name,bill in customers:
        print(f"{name} ${bill*money:.2f}")
    print("")

def notAmused(test,money):
    count = 0
    for i in test:
        if i == "OPEN":
            customers = {}
            count+=1
        elif i == "CLOSE":
            billReport(count,customers,money)
        else:
            aux = i.split(" ")
            client = aux[1]
            time = int(aux[2])
            if "ENTER" in i:
                customers[client] = customers.get(client,0) - time
            if "EXIT" in i:
                customers[client] = customers.get(client,0) + time



if __name__ == '__main__':
    inputTest = """OPEN
ENTER Sam 0
ENTER Alice 15 
EXIT Sam 20
EXIT Alice 700
CLOSE
OPEN
ENTER Sam 5
ENTER Alice 10
EXIT Sam 20
EXIT Alice 35
ENTER Sam 700
EXIT Sam 710
CLOSE"""
    test = inputTest.split("\n")

    notAmused(test, 0.10)