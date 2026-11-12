import matplotlib.pyplot as plt
products = ["Laptop", "Phone", "Tablet", "Watch"]
units_sold = [35, 60, 25, 40]
plt.bar(products, units_sold, color="red")
plt.title("Units Sold by Product")
plt.xlabel("Product")
plt.ylabel("Units Sold")
plt.show()