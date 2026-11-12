import matplotlib.pyplot as plt
apps=("insta","facebook","snap","x")
leads=(50,10,20,20)
plt.pie(leads,labels=apps,autopct="%1.1f%%",startangle=90)
plt.title("app usage")
plt.show()


