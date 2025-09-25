"""
Shop calculator

"""
total_price = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    total_price += float(input("Price of item: "))
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {number_of_items} is {total_price:.2f}")
