import matplotlib.pyplot as plt
import random
import numpy as np #damit wir mehrere barplots in einer figure anzeigen können

plt.style.use("ggplot")

dev_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35] #age

x_indexes = np.arange(len(dev_x)) #numpy array?
width = 0.25

dev_y = [38496, 42000, 46752, 49320, 53200,56000, 62316, 64928, 67317, 68748, 73752] #income per age


py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
"""
x_axis = []

for x in range(1,12):
    x_axis.append(random.randint(1,100))

x_axis.sort()
js_dev_y =  []

for x in range(25,36):
    js_dev_y.append(random.randint(30000,80000))

js_dev_y.sort()

plt.figure(1)
plt.title("PLOT")
plt.xlabel("Age")
plt.ylabel("Income per Age")
plt.plot(x_axis,js_dev_y,color = "b", label = "js devs")
plt.legend()
plt.show()

plt.figure(2)
plt.title("PLOT")
plt.xlabel("Age")
plt.ylabel("Income per Age")
plt.plot(dev_x,dev_y,color = "k", label = "normale devs")
plt.legend()
plt.show() """



plt.bar(x_indexes - width,dev_y,width = width ,color = "g", label = "Normale Developer") #hier mit width diagramm nach links verschieben
plt.xlabel("Age")
plt.ylabel("Income")
plt.title("Income per Age")
plt.bar(x_indexes,py_dev_y,width = width ,color = "y", label = "Python Developer")
plt.bar(x_indexes + width,js_dev_y ,width = width ,color = "b", label = "JScript Developer") #hier mit width diagramm nach rechts verschieben

plt.xticks( ticks= x_indexes, labels=dev_x) #hier wieder unseren richtigen x-achsen werte hinzufügen


plt.legend()
plt.show()