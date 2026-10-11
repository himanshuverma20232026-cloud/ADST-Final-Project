import pandas as pd #Panel Data)
import numpy as np #Numerical Python)

#1.Loading my data
df = pd.read_excel("AmazonGroceryData.xlsx")

print("This is my Original Data")
print(df.shape) #df (dataframe)
print(df.head(25)) #first 5 rows of data from my dataset


#2.Now I am Checking Missing data and also checking duplicate data
print("\nThese are the Missing Values")
print(df.isnull().sum())
#these are the duplicate records
print("\nDuplicate Rows:", df.duplicated().sum())

#3.Fixing the confusing data
print (df["Item Fat Content"].value_counts())
df["Item Fat Content"] = df["Item Fat Content"].replace({"LF": "Low Fat","low fat": "Low Fat",
    "reg": "Regular"})
print (df["Item Fat Content"].value_counts())

# 4. Fill missing Item Weight

# If any missing value remains
df["Item Weight"]=df["Item Weight"].fillna(df["Item Weight"].mean())
print(df.isnull().sum())


# 5. Fix Item Visibility = 0
df["Item Visibility"] = df["Item Visibility"].replace(0, np.nan)
print(df.isnull().sum())


df["Item Visibility"] = df["Item Visibility"].fillna(df["Item Visibility"].mean())
print(df.isnull().sum())



# 6.To find out how old is the establishment (adding a new column)
df["Outlet_Age"]=2026-df["Outlet Establishment Year"]



# 7. Create Sales Category to better understand it
df["Sales_Category"] = pd.qcut(df["Sales"],3,labels=["Low", "Medium", "High"])


#8. Final check
print("\nAfter Cleaning:")
print("Updated Rows count :", len(df))
print("Updated Columns count:", len(df.columns))
print("Missing Values count:", df.isnull().sum().sum())
print("Duplicates count:", df.duplicated().sum())

print("\nColumns After Conversion:")
print(df.columns.tolist())


#9. Save cleaned data
df.to_csv("amazon_grocery_cleaned.csv", index=False)
df.to_excel("amazon_grocery_cleaned.xlsx", index=False)

print("\nData cleaning completed!")
print("amazon_grocery_cleaned.csv created")
print("amazon_grocery_cleaned.xlsx created")

