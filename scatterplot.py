import matplotlib.pyplot as plt
study_hr=(1,2,3,4,5,6,7,)
marks=(42,33,66,55,77,88,44)
plt.scatter(study_hr,marks,color="green")
plt.title("study_hr vs marks")
plt.xlabel(study_hr)
plt.ylabel(marks)
plt.show()