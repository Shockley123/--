import plotly as py
from plotly.graph_objs import Scatter,Layout,Data
line_1=Scatter(x=[1,2,3,4],y=[70,80,90,100])
data=Data([line_1])
py.offline.plot(data,filename="my_first_scatter")