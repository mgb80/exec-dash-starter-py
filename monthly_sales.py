# monthly_sales.py

# TODO: import some modules and packages here
import os
import pandas
import matplotlib.pyplot as plt
import matplotlib.ticker as tick
import operator
import numpy


def to_usd(my_price):
    return "${0:,.2f}".format(my_price)


message = "Please input the file name with .csv appended: "
filename = input(message)
#sales = []
#sales-201710.csv
   
csv_filename = filename #allow user to specify
csv_filepath = os.path.join(os.path.dirname(__file__), "data", csv_filename)



#checking if the file exists --https://stackabuse.com/python-check-if-a-file-or-directory-exists/

#print(csv_filepath)
#print(csv_data)

if os.path.isfile(csv_filepath):
    print("Proceeding with calculations...")
    csv_data = pandas.read_csv(csv_filepath)
else:
    print("File does not exist! Exiting program...")
    exit()



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
    #productMonthlySales = 100.00
    productMonthlySales = matchRow["sales price"].sum()
    top_sellers.append({"name": names, "monthly_sales": productMonthlySales})


top_sellers = sorted(top_sellers, key=operator.itemgetter("monthly_sales"), reverse = True)
#breakpoint()

#used info from --https://github.com/prof-rossetti/georgetown-opim-243-201901/blob/master/exercises/sales-reporting/pandas_explore.py

def find_month(month):
    month_list={'01': 'January', '02': 'February', '03': 'March', '04': 'April', '05': 'May',
                '06': 'June', '07': 'July', '08': 'August', '09': 'September', '10': 'October', 
                '11': 'November', '12': 'December',}
    return month_list[month]

month = find_month(csv_filename[-6:-4])
year = int(csv_filename[6:10])

#print("month" + month)
#print("year" + str(year))
    
# TODO: write some Python code here to produce the desired functionality...

print("-----------------------")
print("MONTH: " + month + str(year))

print("-----------------------")
print("CRUNCHING THE DATA...")

print("-----------------------")
print("TOTAL MONTHLY SALES: $12,000.71")

print("-----------------------")
print("TOP SELLING PRODUCTS:")


rank = 1
for d in top_sellers:
    print("  " + str(rank) + ") " + d["name"] + ": " + to_usd(d["monthly_sales"]))
    rank = rank +1

print("-----------------------")
print("VISUALIZING THE DATA...")


#GRAPHS TO BE INSERTED BELOW...
##########################################


chart_title = ("Top Selling Products " + month + " " + str(year))

chart_products = []
chart_sales = []

for this in top_sellers:
    chart_products.append(this["name"])
    chart_sales.append(this["monthly_sales"])

chart_products.reverse()
chart_sales.reverse()

#########################################

fig, ax = plt.subplots()
usd_formatter = tick.FormatStrFormatter('$%1.0f')
ax.xaxis.set_major_formatter(usd_formatter)


plt.barh(chart_products, chart_sales)
plt.title(chart_title)
plt.ylabel("Product")
plt.xlabel("Monthly Sales (USD)")

plt.tight_layout()
plt.show()







