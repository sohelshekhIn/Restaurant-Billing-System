import matplotlib.pyplot as plt
import sqlite3

# connect to database
conn = sqlite3.connect('billing_system.db')
# make a cursor
c = conn.cursor()
# make a sales line graph and get the data from the database
def sales_line_graph():
    # get the data from the database
    c.execute("SELECT date, total FROM orders")
    # get the data from the database
    data = c.fetchall()
    # get the date and total
    date = [i[0] for i in data]
    total = [i[1] for i in data]
    # give the title
    # give the x and y label 
    # set window size to 10, 5
    
    # why 2 graphs are showing? one with the title and one without the title
    plt.figure(1,figsize=(10, 5))
    plt.plot(date, total)
    # show the graph
    plt.ylabel('Total')
    plt.title('Sales Line Graph')
    plt.xlabel('Date')
    # plt.show()


# make a item frequency pie chart from item_frequency table
def item_frequency_pie_chart():
    # get the data from the database
    c.execute("SELECT name, qty FROM item_frequency")
    # get the data from the database
    data = c.fetchall()
    # get name and qty in {name: qty}
    item_ids = [i[0] for i in data]
    qty = [i[1] for i in data]
    
    # add item_ids and qty in a dictionary
    item_ids_qty = {}
    for i in range(len(item_ids)):
        # if item_id is already in the dictionary then add the qty
        if item_ids[i] in item_ids_qty:
            item_ids_qty[item_ids[i]] += qty[i]
        # if item_id is not in the dictionary then add the item_id and qty
        else:
            item_ids_qty[item_ids[i]] = qty[i]

    # get the item_ids and qty in two different lists
    item_ids = list(item_ids_qty.keys())
    qty = list(item_ids_qty.values())
    
    # using item_ids get name from menu table
    item_names = []
    for item_id in item_ids:
        c.execute("SELECT item_name FROM menu WHERE item_id = ?", (item_id,))
        item_names.append(c.fetchone()[0])
    

    plt.figure(2,figsize=(10, 5)) 
    plt.pie(qty, labels=item_names, autopct='%1.1f%%')
    plt.title('Item Frequency Pie Chart')
    # plt.show()


# make a item frequency bar graph from item_frequency table
def item_frequency_bar_graph():
    # get the data from the database
    c.execute("SELECT name, qty FROM item_frequency")
    # get the data from the database
    data = c.fetchall()
    # get name and qty in {name: qty}
    item_ids = [i[0] for i in data]
    qty = [i[1] for i in data]
    
    # add item_ids and qty in a dictionary
    item_ids_qty = {}
    for i in range(len(item_ids)):
        # if item_id is already in the dictionary then add the qty
        if item_ids[i] in item_ids_qty:
            item_ids_qty[item_ids[i]] += qty[i]
        # if item_id is not in the dictionary then add the item_id and qty
        else:
            item_ids_qty[item_ids[i]] = qty[i]

    # get the item_ids and qty in two different lists
    item_ids = list(item_ids_qty.keys())
    qty = list(item_ids_qty.values())
    
    # using item_ids get name from menu table
    item_names = []
    for item_id in item_ids:
        c.execute("SELECT item_name FROM menu WHERE item_id = ?", (item_id,))
        item_names.append(c.fetchone()[0])
    
    plt.figure(3,figsize=(10, 5)) 
    plt.bar(item_names, qty)
    plt.title('Item Frequency Bar Graph')
    # plt.show()


# pie chart to show top 5 items sold
def top_5_items_sold_pie_chart():
    # get the data from the database
    c.execute("SELECT name, qty FROM item_frequency ORDER BY qty DESC LIMIT 5")
    # get the data from the database
    data = c.fetchall()
    # get name and qty in {name: qty}
    item_ids = [i[0] for i in data]
    qty = [i[1] for i in data]
    
    # add item_ids and qty in a dictionary
    item_ids_qty = {}
    for i in range(len(item_ids)):
        # if item_id is already in the dictionary then add the qty
        if item_ids[i] in item_ids_qty:
            item_ids_qty[item_ids[i]] += qty[i]
        # if item_id is not in the dictionary then add the item_id and qty
        else:
            item_ids_qty[item_ids[i]] = qty[i]

    # get the item_ids and qty in two different lists
    item_ids = list(item_ids_qty.keys())
    qty = list(item_ids_qty.values())
    
    # using item_ids get name from menu table
    item_names = []
    for item_id in item_ids:
        c.execute("SELECT item_name FROM menu WHERE item_id = ?", (item_id,))
        item_names.append(c.fetchone()[0])
    
    plt.figure(4,figsize=(10, 5)) 
    plt.pie(qty, labels=item_names, autopct='%1.1f%%')
    plt.title('Top 5 Items Sold Pie Chart')
    plt.show()
    
    
# bar graph to show customer frequency
# def customer_frequency_bar_graph():
#     # get the data from the database
#     c.execute("SELECT cust_name, date FROM orders")
#     data = c.fetchall()

#     # at what hour max orders are placed
#     # get the hour and total
#     cust_name = [i[0] for i in data]
#     date = [i[1] for i in data]

        
    
#     # plot the bar graph
#     plt.figure(5,figsize=(10, 5))
#     plt.bar(cust_name_freq.keys(), cust_name_freq.values())
#     plt.title('Customer Frequency Bar Graph')
#     plt.show()
        
    

# sales_line_graph()
# item_frequency_pie_chart()
# item_frequency_bar_graph()
# top_5_items_sold_pie_chart()
# customer_frequency_bar_graph()
# close the connection
conn.close()