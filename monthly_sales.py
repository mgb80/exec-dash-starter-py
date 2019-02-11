# monthly_sales.py

# TODO: import some modules and packages here
import os
import pandas

def to_usd(my_price):
    return "${0:,.2f}".format(my_price)

sales = []
csv_filename = "sales-201710.csv" #allow user to specify

csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)

csv_data = pandas.read_csv(csv_filepath)

#print(list(csv_data.columns))
#TODO: read csv file

#CALCULATIONS

monthly_total = csv_data["sales price"].sum()

products_sold = csv_data["product"].unique()

for names in products_sold:
    print(names)


#breakpoint()


top_sellers = [
    {"rank": 1, "name": "Button Down Shirt", "monthly_sales": 6960.35},
    {"rank": 2, "name": "Super Soft Hoodie", "monthly_sales": 1875.00},
]


    
# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print("MONTH: March 2018")

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")

for d in top_sellers:
    print(" " + str(d["rank"]) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))

print("-----------------------")
print("VISUALIZING THE DATA...")
