import pandas as  pd 
import numpy as np
data = {
    "Name": ["bavan", "ben","", "jana",None],
    "Age": [21,23,22,23,24],
    "City": ["chennai","","banglore","mumbai",None]
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
