import matplotlib.pyplot as plt


names=['sai','raj','nani','satya']
sal=[22000,17500,19000,24500]
rents=[9000,7500,8000,12000]
ages=[21,23,25,27]
savings=[10000,8000,13000,15000]
plt.subplot(2,2,1)
plt.title("salaries")
plt.xlabel("names")
plt.ylabel("salaries")
plt.plot(names,sal,'ro--')

plt.subplot(2,2,2)
plt.title("rents")
plt.xlabel("names")
plt.ylabel("rents")
plt.plot(names,rents,'ro--')

plt.subplot(2,2,3)
plt.title("Ages")
plt.xlabel("names")
plt.ylabel("ages")
plt.plot(names,ages,'ro--')

plt.subplot(2,2,4)
plt.title("savings")
plt.xlabel("names")
plt.ylabel("savings")
plt.plot(names,savings,'ro--')

plt.show()