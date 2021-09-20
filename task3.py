#!python3

"""
##### Task 3
When shopping, we pay 12% combined GST and PST on many items.  Write a program that asks the user to enter in the prices of 4 items that they are buying.  Find the total price, the amount of tax and the overall price.  Taxes are rounded appropriately

example:
Enter the first price: 11.99
Enter the second price: 14.76
Enter the third price: 12.99
Enter the fourth price: 15.98
Enter the fift price: 7.99
Your subtotal is $63.71 and your taxes total $7.65 for a total of $71.36

"""

p1 = input("Enter the first price")
p2 = input("Enter the second price")
p3 = input("Enter the third price")
p4 = input("Enter the fourth price")
p5 = input("Enter the fift price")

p1 = float(p1)
p2 = float(p2)
p3 = float(p3)
p4 = float(p4)
p5 = float(p5)

sub = p1 + p2 + p3 + p4 + p5

sub = round(sub,2)

sub = float(sub)

tax = sub*(12/100)

tax = round(tax, 2)

tax = float(tax)

total = sub + tax

total = round(total, 2)

total = str(total)

tax = str(tax)

sub = str(sub)

print("Your subtotal is $"+sub, "and your taxed total $"+tax,"for a total of $"+total)