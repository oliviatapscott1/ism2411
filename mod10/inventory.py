# Refleciton
# 1. The most suprising thing to me is all the rules we have to remember so we don't accidentally break the code or the loop. It surprised me that using normal functions in some scenarios isn't a good idea. 
# 2 A business could use a Python list to keep track of customer orders and their prices. Instead of manually entering and checking each order in Excel, a list could store the prices and allow Python to calculate totals or update information more efficiently. This would save time when handling large numbers of orders and reduce manual errors.








# inventory.py
# Author: Olivia Tapscot
# Module 10 Lab: Inventory List Manager

print("---Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker" ]
print(inventory)
print(len(inventory))


print("---Exercise 2: Index Practice ---")
print(inventory[0])     # first item
print(inventory[-1])    # last item
middle = len(inventory) // 2
print(inventory[middle])    # middle item



print("---Exercise 3: Slicing Practice ---")
print(inventory[:3])     # items from start to index 2 / gives first 3 items (0-2)
print(inventory[-2:])     # last 2 items
print(inventory[::2])     # every second item


print("---Exercise 4: Modifying the List ---")
inventory.append("envelope")
# inventory.append("tape")  # adds another tape to the end
print(inventory)   
inventory.remove("tape")
print(inventory)   # output is ['pen', 'notebook', 'stapler', 'marker', 'envelope', 'tape']
#removing tape just goes and removes the first tape it sees


# inventory.append("zoo")
# inventory.append("Zoo")  #capitalization goes first in sort
# inventory.append("apple")
# #inventory.append("1")
#inventory.append("11")
#inventory.append("4")
#inventory.append("-1")
#inventory.append("%")
#inventory.append("-")


inventory.sort()
print(inventory)




print("--- Exercise 5: Tuple Comparison --- ")
coords = (40.7128, -784.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)



print("--- Exercise 6: Average of a list of sales")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")



print("--- Exercise 7: Accumlator Pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2))  # 10% discount

print("Original prices:", prices)
print("Discounted prices:", discount)




print("--- Exercise 8: Filter above threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales)}")
