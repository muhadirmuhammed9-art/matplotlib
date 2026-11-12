import matplotlib.pyplot as plt

marks = [45, 52, 60, 61, 65, 68, 72, 75, 78, 82, 88, 91]
plt.hist(marks, bins=5, edgecolor="black")
plt.title("Distribution of Student Marks")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.show()
 