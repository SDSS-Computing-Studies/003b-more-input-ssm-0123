#!python3

pop = input("Enter the population")
rate = input("Enter the rate of growth in percent")
days = input("Enter the number of days")

rate = float(rate)

rate = (rate/100)

pop = float(pop)
days = float(days)

future = pop*(1+rate)**(days/365)

days = round(days)
future = round(future)
days = str(days)
future = str(future)

print ("There will be",future,"people after",days,"days")
