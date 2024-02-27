import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
data = pd.read_excel("Kaggle.xlsx")

data["Date"] = pd.to_datetime(data["Date"])
data.set_index('Date', inplace=True)
grouped_obj = data.groupby(["District"])
for key, item in grouped_obj:
   #print(item.to_string())
   #print("Weekly Averages District Wise")
   #print(grouped_obj.resample('w').mean().to_string())
   print("------------------------------------------Monthly Averages District Wise-----------------------------------------------------")
   print(grouped_obj.resample('m').mean().to_string())
   print("------------------------------------------Yearly Averages District Wise-------------------------------------------------------")
   print(grouped_obj.resample('y').median().to_string())
   print("-------------------------------------------Monthly Median Distrct Wise--------------------------------------------------------")
   print(grouped_obj.resample('m').median().to_string())
   print("-------------------------------------------Yearly Median District Wise---------------------------------------------------------")
   print(grouped_obj.resample('y').median().to_string())
   break
   
