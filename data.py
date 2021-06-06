
import plotly.figure_factory as ff
import pandas as pd
import csv

df=pd.read_csv("./108/data.csv")
fig=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)

#y axis can be anystring  ex: "Height" is taken here..
#you can take "abc" or "xyz"
#frequency shows in y axis(out of 1)
fig.show()