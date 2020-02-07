import matplotlib.pyplot as mplt
import numpy as np
import random
print("Hallotest")


#daten aus corey video


# Median Developer Salaries by Age

liste1 = []
liste2 = []

for x in range(22):
    liste1.append(random.randint(0,999))

for y in range(22):
    liste2.append(random.randint(0,999))

liste1.sort()
liste2.sort()


#------------------------------------------



mplt.style.use("ggplot") #sehr guter style
#mplt.xkcd() #comic style
ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]

mplt.plot(ages_x,dev_y,color =  "k", linestyle = "--",marker = ".",label= "All Devs") #format string : -- = gestrichelt , k = black
#marker sind einfach punkte in den Graphen

# Median Python Developer Salaries by Age
py_dev_y = [45372, 48876, 53850, 57287, 63016,65998, 70003, 70000, 71496, 75370, 83640]

mplt.plot(ages_x,py_dev_y,color = "blue", linestyle = ":",marker = "o",linewidth = 3,label = 'Py Devs') # format string: : = gepunktet, b = blue

# Median JavaScript Developer Salaries by Age
js_dev_y = [37810, 43515, 46823, 49293, 53437,56373, 62375, 66674, 68745, 68746, 74583]

mplt.plot(ages_x,js_dev_y,color = "orange",linewidth = 2, label = 'JScript Devs')  

mplt.xlabel("Ages")

mplt.ylabel("Median Salary (EUR)")

mplt.title("Median Salary (EUR) by Age")

#mplt.legend(["All Devs","Py Devs"]) nur eine Möglichkeit
mplt.legend() #in plot function label eingeben und dann nur leere legend() methode anwenden

#mplt.grid(True) #Gitter für Visualisierung

mplt.tight_layout() #damit patting besser ist


mplt.savefig("plotnummer1.png")

mplt.show()

