import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("customer_churn.csv")

df = df.drop_duplicates()
#know about the Column name and Nulls
df . info()

print(" \n Total Number of Rows :- " , len(df) )

print("Age Columns Total Null Values :- ")
print(df["Age"].isnull().sum())
print(df["Age"].unique)

df["Age"] = np.where((df["Age"]>100 )|(df["Age"]<0) , np.nan , df["Age"])
df["Age"] = df["Age"].fillna(df["Age"].mean())
print(df["Age"].dtype)
df["Age"] = df["Age"].astype(int)

print("Age Columns Total Null Values :- ")
print(df["Age"].isnull().sum())
print(df["Age"].dtype)

print("\n \n")



#Tenure Column
print(df["Tenure"].describe())
df["Tenure"] = np.where((df["Tenure"]>75)|(df["Tenure"]<0), df["Tenure"].mode() , df["Tenure"])
print(" \n  Again We try To Check :- ",df["Tenure"].describe() , "\n ")
print("\n ",df["Tenure"].info())
print("Here Done Tenure Col \n\n ")


#Gender Column 
print(df["Gender"].isnull().sum())
print(df["Gender"].unique())
df["Gender"] = np.where(df["Gender"]=="male", df["Gender"].replace("male" , "Male" ), df["Gender"])
df["Gender"] = np.where(df["Gender"]=="FEMALE" , df["Gender"].replace("FEMALE" , "Female"), df["Gender"])
df["Gender"] = np.where(df["Gender"]=="unknown" , df["Gender"].mode(), df["Gender"])

print("\n\n")


#Contract Colum
print(df["Contract"].info() , "\n \n ",df["Contract"].describe())
print(df["Contract"].unique())

df["Contract"] = df["Contract"].str.lower()
df["Contract"] = df["Contract"].str.capitalize()
print("After Cleaning the Data :- " , df["Contract"].unique())
print("\n \n")


#MonthlyCharges Column

print(df["MonthlyCharges"].describe())

df["MonthlyCharges"] = np.where((df["MonthlyCharges"]>2000)| (df["MonthlyCharges"]<0) , np.nan , df["MonthlyCharges"])
df["MonthlyCharges"] = df["MonthlyCharges"].fillna(df["MonthlyCharges"].mode().iloc[0] ) 
df["MonthlyCharges"]= df["MonthlyCharges"].round(2)

print(df["MonthlyCharges"].describe().round(2))
print(df["MonthlyCharges"].isnull().sum())



print(df["InternetService"].unique())
df["InternetService"] = df["InternetService"].str.capitalize()
df["InternetService"] = df["InternetService"].fillna(df["InternetService"].mode().iloc[0])

print(
    df["InternetService"].unique() ,
       "\n \n " , 
       "Total Null Number in the InternetService Colu " , 
       df["InternetService"].isnull().sum()
    )

