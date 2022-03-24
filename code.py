import csv
from statistics import correlation 
import plotly.express as px
import numpy as np

def plotfigure(data_path):
    with open(data_path) as a:
        read = csv.DictReader(a)
        fig = px.scatter(read, x = "Marks In Percentage", y = "Days Present")
        fig.show()

def getdatasource(data_path):
    days = []
    marks = []
    with open(data_path) as b:
        read = csv.DictReader(b) 
        for i in read:
            marks.append(float(i["Marks In Percentage"]))
            days.append(int(i["Days Present"]))
    return{"x":marks, "y":days}

def findcorrelation(data_source):
    correlation = np.corrcoef(data_source["x"],data_source ["y"])
    print("Correlation:", correlation[0,1])

def main():
    data_path = "123.csv"
    data_source = getdatasource(data_path)
    findcorrelation(data_source)
    plotfigure(data_path)

main()