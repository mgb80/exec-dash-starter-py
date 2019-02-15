# monthly_sales.py

# TODO: import some modules and packages here
import os
import pandas
import matplotlib.pyplot as plt

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

#sales = []
csv_filename = "sales-201710.csv" #allow user to specify

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

csv_data = pandas.read_csv(csv_filepath)

#print(list(csv_data.columns))
#TODO: read csv file

#CALCULATIONS

monthly_total = csv_data["sales price"].sum()


#Need to get info from csv instead of hardcoding...
#top_sellers = [
#    {"name": "Button Down Shirt", "monthly_sales": 6960.35},
#    {"name": "Super Soft Hoodie", "monthly_sales": 1875.00},
#    {"name": "Product 3", "monthly_sales": 2000.00},
#    {"name": "Product 4", "monthly_sales": 6000.00},
#]

product_names = csv_data["product"]

unique_product_names = product_names.unique()

unique_product_names = unique_product_names.tolist()

top_sellers = []

for names in unique_product_names:
    matchRow = csv_data[csv_data["product"]== names]
    productMonthlySales = 100.00
    top_sellers.append({"name": names, "monthly_sales": productMonthlySales})


#breakpoint()

    
# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")


rank = 1
for d in top_sellers:
    print( d["name"] + ": " + to_usd(d["monthly_sales"]))

print("-----------------------")
print("VISUALIZING THE DATA...")


#GRAPHS TO BE INSERTED BELOW...

#sample graph


chart_title = "Top Selling Products (February 2019)"

chart_products = []
chart_sales = []

for this in top_sellers:
    chart_products.append(this["name"])
    chart_sales.append(this["monthly_sales"])

plt.bar(chart_products, chart_sales)
plt.title(chart_title)
plt.ylabel("Product")
plt.xlabel("Monthly Sales (USD)")
plt.show()