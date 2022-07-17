import pandas as pd
import plotly.express as pe
import numpy as n
 
data = pd.read_csv("marksVSattendence.csv")
marks=data["Marks In Percentage"].to_list()
attendence=data["Days Present"].to_list()


sgraph=pe.scatter(data, x=attendence, y=marks)

# sgraph.show()



cc=n.corrcoef(attendence, marks)
print("Correlation coefficient is : " , cc[0,1])










