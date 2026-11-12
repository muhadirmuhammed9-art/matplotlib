import matplotlib.pyplot as plt
months = ["Jan", "Feb", "Mar", "Apr"]
sales = [100, 130, 125, 160]
expenses = [70, 85, 90, 105]
fig, axes = plt.subplots(1, 2, figsize=(10, 4))
axes[0].plot(months, sales, marker="o")
axes[0].set_title("Monthly Sales")
axes[0].set_xlabel("Month")
axes[0].set_ylabel("Sales")
axes[1].bar(months, expenses, color="coral")
axes[1].set_title("Monthly Expenses")
axes[1].set_xlabel("Month")
axes[1].set_ylabel("Expenses")
plt.tight_layout()
plt.show()