import matplotlib.pyplot as plt
products = ["Laptop", "Mobile", "Tablet", "Keyboard", "Mouse"]
units_sold = [50, 80, 40, 60, 30]
plt.barh(products, units_sold, color="seagreen")
plt.title("Product Sales Comparison")
plt.xlabel("Units Sold")
plt.show()