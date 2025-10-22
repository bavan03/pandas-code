import pandas as pd
data = {
    "Name": ["bavan", "ben", "jana","dinesh","sanakkiya","balaji","yuva","joo","aadhi","bala"],
    "age": [21, 23, 22,24,22,25,25,23,24,22],
    "phone": ["34567367", "1234567890", "7654321098","6543210987","5432109876","4321098765","3210987654","2109876543","1098765432","1987654321"],
    "dob": ["25-06-2004", "18-04-2002", "27-082004","25-06-2005","13-02-2004","13-07-2005","27-04-2004","10-06-2001","14-02-2005","23-06-2001"],
    "email": ["bavangmail.com", "ben@mail.com", "jana@gmailcom","dinesh@gmail.com","sanakkiya@gmail.com","balaji@gmail.com","yuva@gmail.com","joo@gmail.com","aadhi@gmail.com","bala@gmail.com"]
}
df = pd.DataFrame(data)
print("Original Data:")
print(df)

incorrectphones =df[df["phone"].str.len() < 10]
print("less then 10 numbers:\n",incorrectphones)
if incorrectphones==[]:
    print("no duplicate phone numbers found")


incorrectdob = df[~df['dob'].str.match('\d{2}-\d{2}-\d{4}')]
print("duplicate DOB entries:\n",incorrectdob)
if incorrectdob==[]:
    print("no duplicate DOB entries found")


incorrectemail = df[~df['email'].str.contains('@gmail.com')]
print("incorrect email entries:\n",incorrectemail)
if incorrectemail==[]:
    print("no incorrect email entries found")
print("\n Data shape:",df.shape)
print("print all duplicate\n",incorrectphones,incorrectdob,incorrectemail)
