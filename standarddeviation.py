import pandas as pd
import plotly.express as px
import math
import csv
with open("class1.csv", newline = '') as file:
    readfile = csv.reader(file)
    filedata = list(readfile)

filedata.pop(0)
length = len(filedata)

marksum = 0

for data in filedata:
    integer = int(data[1])
    marksum += integer

mean = marksum/length
print(mean)

dataf = pd.read_csv("class1.csv")

#to calculate standard deviation

numerator = []

for data in filedata:
    integer1 = int(data[1])
    square = (integer1 - mean)*(integer1 - mean)
    numerator.append(square)

standarddev = math.sqrt((1/length)*(sum(numerator)))
print(standarddev)

scattergraph = px.scatter(dataf, x = "Student Number", y ="Marks", color = "Student Number")
scattergraph.update_layout(shapes = [dict(type = 'line', y0 = standarddev, y1 = mean, x0= 0, x1 = length)])
scattergraph.show()


