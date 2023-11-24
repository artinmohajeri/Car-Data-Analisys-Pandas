import pandas as pd
import os
from pathlib import Path
path = Path("./special_cars.xlsx ")

df = pd.read_csv("./cars.csv")
df.dropna(how="all", inplace=True)
df["MSRP"] = pd.to_numeric(df["MSRP"].str.replace("$","").str.replace(",",""))
df["Cylinders"] = pd.to_numeric(df["Cylinders"], errors='coerce')

row1 = df[df['MSRP'] == df['MSRP'].max()]
row1["why special"] = "most expensive"

row2 = df[df['MSRP'] == df["MSRP"].min()]
row2["why special"] = "cheapest"

row3 = df[df['EngineSize'] == df["EngineSize"].max()]
row3["why special"] = "biggest engine size"

row4 = df[df['EngineSize'] == df["EngineSize"].min()]
row4["why special"] = "smallest engine size"

row5 = df[df['Cylinders'] == df['Cylinders'].max()]
row5["why special"] = "highest numbers of cylinders"

row6 = df[df['Cylinders'] == df['Cylinders'].min()]
row6["why special"] = "Lowest numbers of cylinders"

row7 = df[df['Horsepower'] == df['Horsepower'].max()]
row7["why special"] = "highest horsepower"

row8 = df[df['Horsepower'] == df['Horsepower'].min()]
row8["why special"] = "least horsepower"

row9 = df[df['Weight'] == df['Weight'].max()]
row9["why special"] = "heaviest"

row10 = df[df['Weight'] == df['Weight'].min()]
row10["why special"] = "lightest"

row11 = df[df['Length'] == df['Length'].max()]
row11["why special"] = "tallest"

row12 = df[df['Length'] == df['Length'].min()]
row12["why special"] = "shortest"


data_frame = pd.concat([row1,row2,row3,row4,row5,row6,row7,row8,row9,row10, row11, row12])
data_frame["Cylinders"].fillna("unavailable", inplace=True)

if os.path.exists(path):
    os.remove(path)
else:
    data_frame.to_excel(path, index=False)

