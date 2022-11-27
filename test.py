import sqlite3

conn = sqlite3.connect('billing_system.db')

# make a cursor
c = conn.cursor()
# create a table
# c.execute("""CREATE TABLE IF NOT EXISTS menu (
#             item_name text,
#             item_price real
#             )""")

# insert data in table
# c.execute("INSERT INTO menu VALUES ('Aloo Tikki Burger', 49)")
# c.execute("INSERT INTO menu VALUES ('Paneer Tikka Burger', 99)")
# c.execute("INSERT INTO menu VALUES ('Veg Burger', 69)")
# c.execute("INSERT INTO login VALUES ('Admin', 'admin', 'admin')")
# c.execute("INSERT INTO login VALUES ('Sohel Shekh', 'sohel', 'shekh')")

# modify data in table
# c.execute("UPDATE menu SET item_id = 101 WHERE item_name = 'Aloo Tikki Burger'")
# c.execute("UPDATE menu SET item_id = 102 WHERE item_name = 'Paneer Tikka Burger'")
# c.execute("UPDATE menu SET item_id = 103 WHERE item_name = 'Veg Burger'")
# c.execute("UPDATE menu SET item_id = 104 WHERE item_name = 'Chicken Tikka Burger'")
# query = "CREATE TABLE login(Name VARCHAR, Username VARCHAR UNIQUE, Password VARCHAR)"
# conn.execute(query)
# create new table for orders
c.execute("CREATE TABLE IF NOT EXISTS item_frequency (date text,name text,qty integer)")



# commit changes
conn.commit()
# close connection
conn.close()