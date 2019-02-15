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
top_sellers = [
    {"name": "Button Down Shirt", "monthly_sales": 6960.35},
    {"name": "Super Soft Hoodie", "monthly_sales": 1875.00},
    {"name": "Product 3", "monthly_sales": 2000.00},
    {"name": "Product 4", "monthly_sales": 6000.00},

]

products_sold = csv_data["product"].unique()

#for names in products_sold:
#    print(names)


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

bar_graph = [
    {"types": "Thriller", "viewers": 12345},
    {"types": "Horror", "viewers": 8463},
    {"types": "Comedy", "viewers": 1294},
    {"types": "Romance", "viewers": 2398},
]

types = []
viewers = []

for this in bar_graph:
    types.append(this["types"])
    viewers.append(this["viewers"])

plt.bar(types, viewers)
plt.ylabel("Viewers")
plt.xlabel("Type")
plt.show()