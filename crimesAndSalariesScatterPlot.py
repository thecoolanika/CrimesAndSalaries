'''
I compared the Average Monthly Net Salary (After Tax) and the crime index in the cities in the United States. 
In this file, I created a scatterplot with my data. 
'''
import random
from bokeh.models import Title
from bokeh.plotting import figure, output_file, show
import math

c = open("crimesAndSalaries.txt", "r")

crimes = []
salaries = []

for line in c:
  line = line.strip()
  data = line.split(",")
  crimes.append(float(data[0])) 
  salaries.append(float(data[1]))


def scatterPlot (xVals, yVals, dotSize, dotColor, figure):
  for i in range (len (xVals)):
    figure.circle(xVals[i], yVals[i], size = dotSize, color = dotColor)

f = figure()



f = figure(title="Average Salaries", title_location="left")

f.add_layout(Title(text="Crime Indicies", align="center"), "below")

f.add_layout(Title(text="Average Salaries vs Crime Indicies", align="left"), "above")

scatterPlot (crimes, salaries, 10, "red", f)

show(f)
