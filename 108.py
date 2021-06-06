import random
import plotly.express as px

dice_result=[]
count=[]
#we want to add this 100 times
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    #print(dice1,dice2)
    dice_result.append(dice1+dice2)
    count.append(i)


fig=px.bar(x=dice_result,y=count)
fig.show()


#y axis can be anystring  ex: "Height" is taken here..
#you can take "abc" or "xyz"
#frequency shows in y axis(out of 1)


#more values in the center
#the higher values and lower values are less

#if you join all the left edges of the bar graph, you would see that the
#distribution of numbers is almost like a bell shape

#bell shape distribution is very common--thats why is called
#normal distribution
#most of the data in the universe follow this pattern




