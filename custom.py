import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
visitors = [120, 150, 135, 170, 200]
plt.figure(figsize=(8, 4))
plt.plot(days, visitors, marker="o", color="purple",
linestyle="--", linewidth=2, label="Visitors")
plt.title("Website Visitors", fontsize=14)
plt.xlabel("Day")
plt.ylabel("Visitors")
plt.grid(True, alpha=0.3)
plt.legend()
plt.tight_layout()
plt.show()