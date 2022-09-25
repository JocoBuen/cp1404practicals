"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.

sales = 0
get sales

while sales >= 0
    if sales < 1000
        bonus = sales * 1.1
        display The bonus from your sales is 10% more
    else
        bonus = sales * 1.15
        display The bonus from your sales is 15% more
    get sales
"""
sales = 0
sales = float(input("Enter sales: $"))

while sales >= 0:
    if sales < 1000:
        bonus = sales * 1.1
        print("The bonus from your ${:.2f} sales is ${:.2f}".format(sales, bonus))
    else:
        bonus = sales * 1.15
        print("The bonus from your ${:.2f} sales is ${:.2f}".format(sales, bonus))
    sales = float(input("Enter sales: $"))
