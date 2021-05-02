import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

a = pd.read_csv("C:/Users/shubham/Desktop/Sublime/pandas/ipl2021bat.csv")

x = a["PLAYER"][:5]
y = a["Runs"][:5]
plt.title("Orange Cap Holder")
plt.subplot(2,1,1)
#plt.xlabel("Player Name")
plt.ylabel("Runs")

plt.bar(x,y)

plt.subplot(2,1,1)
#plt.xlabel("Player Name")
#plt.ylabel("Strike Rate")
x = a["PLAYER"][:5]
y = a["SR"][:5]
plt.plot(x,y,"o:r",label="Strike Rate")
plt.legend()

plt.subplot(2,1,2)
plt.xlabel("Player Name")
plt.ylabel("Average")
x = a["PLAYER"][:5]
y = a["Avg"][:5]
plt.bar(x,y)



plt.show()
