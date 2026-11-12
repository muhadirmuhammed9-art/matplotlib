import matplotlib.pyplot as plt
categories=["food","travel","internet","shopping","others"]
expense=[800,400,600,1000,300]
plt.bar(categories,expense,color="steelblue")
plt.title("trip expense")
plt.xlabel("categories")
plt.ylabel("expense")
plt.show()
