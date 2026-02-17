
import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv(r"C:\Users\user\OneDrive\PYTHON\Supermart Grocery Sales - Retail Analytics Dataset.csv")
print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.dtypes) 
print(df.isnull().sum())
print(df.describe())

sales_by_category = df.groupby("Category")["Sales"].sum().sort_values(ascending=False)
print(sales_by_category)

profit_by_category = df.groupby("Category")["Profit"].sum().sort_values(ascending=False)
print(profit_by_category)

Sales_by_sub_category = df.groupby("Sub Category")["Sales"].sum() \
.sort_values(ascending=False) \
.head(10)
print(Sales_by_sub_category)

Sales_by_sub_category = df.groupby("Sub Category")["Sales"].sum().sort_values(ascending=False).head(10)
print(Sales_by_sub_category)

sales_by_category.plot(kind="bar", title="Total Sales by Category")
plt.show()

print(df[["Sales", "Profit"]].sum())

profit_margin = (            #Option 1-Advanced
    df.groupby("Category")
    .apply(lambda x:x["Profit"].sum() / x["Sales"].sum())
    .sort_values(ascending=False)
)
print(profit_margin)

#Option 2 - Beginner friendly
category_summary = df.groupby("Category")[["Sales", "Profit"]].sum()
print(category_summary)

category_summary["Profit_Margin"] = (      
    category_summary["Profit"] / category_summary["Sales"]
)
print(category_summary["Profit_Margin"])

category_summary[["Sales", "Profit"]].plot(kind="bar")
plt.show()

#Ranking-comparing category by region       
profit_by_category_region = df.groupby(["Region", "Category"])["Profit"].sum()
print(profit_by_category_region)

df[df["Category"] == "Snacks"].groupby("Region")["Profit"].sum().plot(kind="bar")
plt.show()

#Total profit by region
profit_region_highest = df[df["Category"] == "Snacks"].groupby("Region")["Profit"].sum().sort_values(ascending=False)
print(profit_region_highest)