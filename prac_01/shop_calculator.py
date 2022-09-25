"""
total_price = 0
get number_of_items
while number_of_items < 0
    display Invalid number of items!
    get number_of_items
for each item in number_of_items
    get price_of_item
    total_price = total_price + price_of_item
if total_price > 100
    discounted_price = total_price * 0.90
    display "Total price for number_of_items is discounted_price"
else
    display "Total price for number_of_items is total_price"
"""

total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))

for item in range(0, number_of_items, 1):
    price_of_item = float(input("Price of items: "))
    total_price = total_price + price_of_item

if total_price > 100:
    discounted_price = total_price * 0.90
    print("Total price for {} items is ${:.2f}".format(number_of_items, discounted_price))
else:
    print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
