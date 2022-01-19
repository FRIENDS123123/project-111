from os import device_encoding
from numpy import DataSource
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import statistics
import csv
import random

df=pd.read_csv("studentmarks.csv")
data = df["Math_score"].tolist()
#fig=ff.create_distplot([data],["Math_score"],show_hist=False)
#fig.show()
#mean=statistics.mean(data)
#std_deviation=statistics.stdev(data)
#print("mean",mean)
#print("standarddeviation",std_deviation)
def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean
mean_list=[]
for i in range(0,1000):
        set_of_means=random_set_of_mean(100)
        mean_list.append(set_of_means)
        mean=statistics.mean(data)
#mean=statistics.mean(data)
std_deviation=statistics.stdev(mean_list) 
#print("mean",mean)
#print("standarddeviation",std_deviation)
#fig=ff.create_distplot([mean_list],["student mark"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.2],mode="lines",name="MEAN"))
#fig.show()     
#def show_fig(mean_list):
    #df=mean_list                   
    #fig=ff.create_distplot([df],["Math_score"],show_hist=False)
    #fig.show()
first_std_deviation_start,first_std_deviation_end=mean-std_deviation,mean+std_deviation
second_std_deviation_start,second_std_deviation_end=mean-(2*std_deviation),mean+(2*std_deviation)
third_std_deviation_start,third_std_deviation_end=mean-(3*std_deviation),mean+(3*std_deviation)
#print("std_deviation1",first_std_deviation_start,first_std_deviation_end)
#print("std_deviation2",second_std_deviation_start,second_std_deviation_end)
#print("std_deviation3",third_std_deviation_start,third_std_deviation_end)
#fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_start,first_std_deviation_start],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 1"))
#fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 1"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_start,second_std_deviation_start],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 2"))
#fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 2"))
#fig.add_trace(go.Scatter(x=[third_std_deviation_start,third_std_deviation_start],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 3"))
#fig.add_trace(go.Scatter(x=[third_std_deviation_end,third_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 3"))
#fig.show()

df=pd.read_csv("MATHSCOREEEEE.csv")
data=df["Math_score"].tolist()
meanofsample1=statistics.mean(data)
print("mean of sample 1",meanofsample1)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample1,meanofsample1],y=[0,0.17],mode="lines",name="mean of sample 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 2"))
fig.show()

df=pd.read_csv("MATHSCOREEEEE2.csv")
data=df["Math_score"].tolist()
meanofsample2=statistics.mean(data)
print("mean of sample 2",meanofsample2)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample2,meanofsample2],y=[0,0.17],mode="lines",name="mean of sample 2"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 2"))
fig.show()

df=pd.read_csv("MATHSCOREEEEE3.csv")
data=df["Math_score"].tolist()
meanofsample3=statistics.mean(data)
print("mean of sample 3",meanofsample3)
fig=ff.create_distplot([mean_list],["student marks"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[meanofsample3,meanofsample3],y=[0,0.17],mode="lines",name="mean of sample 3"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end,first_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end,second_std_deviation_end],y=[0,0.17],mode="lines",name="STANDERD DEVIATION 2"))
fig.show()

