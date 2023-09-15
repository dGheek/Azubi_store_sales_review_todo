# Todo Store sales review  

"""
Azubi store has products that customers love. Below are the products, 
prices and the number of customers that purchased products last week.

The owner wants you to do some calculations on the data with these criteria's:

    -calculate the total price average for all products
    -create a new price list that reduces the old prices by $ 5
    -calculate the total revenue generated from the products
    -calculate the average daily revenue generated from the products
    -based on the new prices, which products are less than $ 30 

"""


# calculate the total price average for all products

# Define the lists
products = ["Sankofa Foods", "Jamestown Coffee", "Bioko Chocolate", "Blue Skies Ice Cream", "Fair Afric Chocolate", "Kawa Moka Coffee", "Aphro Spirit", "Mensado Bissap", "Voltic"]
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

# Calculate the total price
total_price = sum(prices)

# Calculate the average price
average_price = total_price / len(products)

# Print the result
print(f"The average price for all products is ${average_price:.2f}")
print()

# create a new price list that reduces the old prices by $ 5

# old price list
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]

# Create a new list with reduced prices
new_prices = [price - 5 for price in prices]

# Print the new prices list
print("Old Prices:", prices)
print("New Prices:", new_prices)
print()



# calculate the total revenue generated from the products

# Define the lists
prices = [30, 25, 40, 20, 20, 35, 45, 50, 35]
last_week = [2, 3, 5, 8, 4, 4, 6, 2, 9]

# Calculate the total revenue for each product and sum them up
total_revenue = sum(price * customers for price, customers in zip(prices, last_week))

# Print the total revenue
print(f"The total revenue generated from the products is ${total_revenue:.2f}")
print()

# calculate the average daily revenue generated from the products

# Define the total revenue and the number of days
total_revenue = 0  # You should calculate this using the previous code
number_of_days = 7  # Assuming data is available for a week

# Calculate the average daily revenue
average_daily_revenue = total_revenue / number_of_days

# Print the average daily revenue
print(f"The average daily revenue generated from the products is ${average_daily_revenue:.2f}")
print()



# based on the new prices, which products are less than $ 30 

# Define the new prices list (prices reduced by $5)
new_prices = [25, 20, 35, 15, 15, 30, 40, 45, 30]

# Initialize a list to store products with prices less than $30
products_less_than_30 = []

# Iterate through the products and their new prices
for product, price in zip(products, new_prices):
    if price < 30:
        products_less_than_30.append(product)

# Print the products with prices less than $30
print("Products with prices less than $30:")
for product in products_less_than_30:
    print(product)
