import pandas as  pd 
import numpy as np
data = {
    "Name": ["bavan", "ben","", "jana","none"],
    "Age": [21,23,22,23,24],
    "City": ["chennai","","banglore","mumbai","none"]
}
df= pd.DataFrame(data)
log={}
log['null values']=df.isnull().sum()
log['empty strings']=(df =='').sum()
duplicates_per_column={}
for col in df.columns:
    duplicates_per_column[col]=df.duplicated(keep=False).sum()
log['duplicates value']=pd.Series(duplicates_per_column)
log_df=pd.DataFrame(log)
print("data quality log:")
print(log_df)
log_df.to_csv("bavan1.csv",index=True)
print("\n log saved to bavan1.csv")


print(" original data:")
print(df)
df["salary"]=[50000,60000,55000,65000,70000]
print("\n update salary column:")
print(df)

df["Age"] = df["Age"]+1
print("\n update age column:")
print(df)


df.drop(columns=["City"],inplace=True)
print("\n removed city")
print(df)


new_row={"Name":"yuva","Age":25,"salary":75000}
df.loc[len(df)] = new_row
print("\n added new row:")
print(df)


df.loc[df["Name"]=="ben","salary"]=62000
print("\n updated salary for ben:")
print(df)


df=df[df["Name"]!="jana"]
print("\n removed row where name is jana:")
print(df)

df.to_csv("bavan_updated.csv",index=False)
print("\n updated data saved to bavan_updated.csv")
  