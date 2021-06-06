# we can also draw a distribution using plotly's 
#figure_factory module
#install scipy package

#pip install scipy
#use displot() to draw the distribution graph
#it takes two arguments, --the data, the label

import random
import plotly.express as px
import plotly.figure_factory as ff

dice_result=[]
count=[]
#we want to add this 100 times
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    #print(dice1,dice2)
    dice_result.append(dice1+dice2)
    count.append(i)

#y axis can be anystring  ex: "Result" is taken here..
#you can take "abc" or "xyz"
#frequency shows in y axis(out of 1)


#if for loop is for a bigger number like i=1000 ,the graph will be nearly same everytime you run it
#if for loop is for a smaller no like i=10,graph will be different everytime you run it.

fig=ff.create_distplot([dice_result],["Result"])
fig.show()
