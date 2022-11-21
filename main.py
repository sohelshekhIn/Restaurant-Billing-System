import os, time
import random
import sqlite3
from getpass import getpass
conn = sqlite3.connect('billing_system.db')
c = conn.cursor()

# Global Variables
logedin_name = False
customer_name = ""
order_details = {}


def screen_header():
    # clears the screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("""
                BurgerDi - The Burger House
        21/3 Kokran Temple, College Road, Nadiad 387001 
        
                Resturant Billing System
""")

def login():
    global logedin_name
    screen_header()
    username = input("""Username: """)
    if username != "":    
        password = getpass("""Password: """)
        query = 'SELECT * FROM login WHERE Username = ? AND Password = ?'
        c.execute(query, (username, password))
        result = c.fetchone()
        conn.commit()
        if result != None:
            logedin_name = result[0]
            return result
        else:
            return False
    else:
        logedin_name = "Sohel Shekh"
        return True

def show_menu():
    screen_header()
    print("""
          
          
                                Our Menu
                            
        Sr.  Item Id    Item Name                     Price (Rs)
          """)
    
    # load menu from database
    c.execute("SELECT * FROM menu")
    menu = c.fetchall()
    i = 1
    for item in menu:
        print(f"          {i}.     {item[2]}    {item[0]}{' '*(30-len(item[0]))}{item[1]}")
        i+=1
    input("""
          Press enter to continue...""")
    
def main_menu():
    while True:
        screen_header()
        menu_choice = input("""
        1. Take Order
        2. Show Menu
        3. Add Item
        4. Edit Item
        5. Remove Item
        6. Add User
        7. Remove User
        8. Logout
                
            
        Enter your choice: """)
        
        if menu_choice == '1':
            order_page()
        elif menu_choice == '2':
            show_menu()
        elif menu_choice == '3':
            add_item()
        elif menu_choice == '4':
            edit_item()
        elif menu_choice == '5':
            remove_item()
        elif menu_choice == '6':
            add_user()
        elif menu_choice == '7':
            remove_user()
        elif menu_choice == '8':
            break
        else:
            print("Invalid choice")
            time.sleep(2)
            continue
     
def add_item():
    screen_header()
    print("\t\tAdd New Item to Menu", end='\n'*2)
    item_name = input("\tItem Name: ")
    item_price = input("\tItem Price: ")

    # get last item id from database
    c.execute("SELECT item_id FROM menu ORDER BY item_id DESC LIMIT 1")
    last_item_id = c.fetchone()[0]
    # add new item to database
    c.execute("INSERT INTO menu VALUES (?, ?, ?)", (item_name, item_price, last_item_id+1))
    conn.commit()
    print("""
        Item added successfully""")  
    time.sleep(2)


def edit_item():
    # show menu and ask item id and prompt to edit item
    while True:
        show_menu()
        item_id = input("Enter item id to edit: ")
        if item_id != "":
            # load item from database
            c.execute("SELECT * FROM menu WHERE item_id = ?", (item_id,))
            item = c.fetchone()
            if item != None:
                # prompt to edit item
                screen_header()
                print(f"""
                        Edit Item
                    """)
                print(f"""
                    Item Name: {item[0]}
                    Item Price: {item[1]}
                    """)
                new_item_name = input("Enter new item name: ")
                new_item_price = input("Enter new item price: ")
                if new_item_name != "" and new_item_price != "":
                    # update item in database
                    c.execute("UPDATE menu SET item_name = ?, item_price = ? WHERE item_id = ?", (new_item_name, new_item_price, item_id))
                    conn.commit()
                    print("Item updated successfully")
                    time.sleep(2)
                    break
                else:
                    break
            else:
                print("Invalid item id")
                time.sleep(2)
                continue
        else:
            break

def remove_item():
    # show menu and ask item id to remove
    while True:
        show_menu()
        item_id = input("Enter item id to remove: ")
        if item_id != "":
            # load item from database
            c.execute("SELECT * FROM menu WHERE item_id = ?", (item_id,))
            item = c.fetchone()
            if item != None:
                # remove item from database
                c.execute("DELETE FROM menu WHERE item_id = ?", (item_id,))
                conn.commit()
                print("Item removed successfully")
                time.sleep(2)
                break
            else:
                print("Invalid item id")
                time.sleep(2)
                continue
        else:
            break


def add_user():
    # prompt to ask for username and password and add user to database
    screen_header()
    print("\t\tAdd New User", end='\n'*2)
    name = input("\tName: ")
    username = input("\tUsername: ")
    password = getpass("\tPassword: ")
    if username != "" and password != "":
        c.execute("INSERT INTO login VALUES (?, ?, ?)", (name, username, password))
        conn.commit()
        print("\tUser added successfully")
        time.sleep(2)

def remove_user():
    # ask for username and remove user from database
    screen_header()
    print("\t\tRemove User", end='\n'*2)
    username = input("\tUsername: ")
    if username != "":
        c.execute("DELETE FROM login WHERE username = ?", (username,))
        conn.commit()
        print("\tUser removed successfully")
        time.sleep(2)

def invoice_header():
    global customer_name
    # clear screen  
    os.system('cls' if os.name == 'nt' else 'clear')
    screen_header()
    # current time
    current_time = time.strftime("%d/%m/%Y %H:%M:%S")
    # generate invoice number with current time and random number
    invoice_number = str(time.time()).replace('.', '')[5:9] + str(random.randint(1000, 9999))
    print(f"""
---------------------- Tax Invoice ----------------------
    
Invoice No: {invoice_number}\t\t\tCashier:  {logedin_name}           
Date: {current_time}\t\tCustomer: {customer_name}

          """)   

def show_order(order_ids):
    invoice_header()
    print("""
            Order Details

Sr.  Item Id    Item Name                 Qty.        Price (Rs)""")
    # load name and price of items from database with order ids
    c.execute("SELECT * FROM menu WHERE ItemId IN ({})".format(','.join('?'*len(order_ids))), order_ids)
    menu = c.fetchall()
    i = 1
    total = 0
    # if same item is ordered multiple times then add quantity
    
    for item in menu:
        print(f"  {i}.     {item[2]}    {item[0]}{' '*(20-len(item[0]))}   {item[1]}")
        total += item[1]
        i+=1
    print(f"""
            {'-'*50}
            Total{' '*(40-len(str(total)))}{total}
            """)
    input("""
Press enter to continue""")
    return total

                

def order_page():
    global customer_name, order_details
    screen_header()
    print(f"""
                    Tax Invoice   
          """)
    customer_name = input("""
        Customer Name: """)
    while True:
        invoice_header()
        order_details = take_order()
        if order_details != False:
            invoice_header()
            print(order_details)
            input("5")
            break
    

def take_order():
    print("""
          
                    Select Items from Menu
                            
Sr.  Item Id    Item Name                     Price (Rs)
          """)
    
    # load menu from database
    c.execute("SELECT * FROM menu")
    menu = c.fetchall()
    # generate list of item ids
    item_ids = []
    i = 1
    for item in menu:
        item_ids.append(item[2])
        print(f"  {i}.     {item[2]}    {item[0]}{' '*(30-len(item[0]))}{item[1]}")
        i+=1
 
    ask_for_order = input("""
Enter order id to add items: """)
    # make list of order ids from user input comma seperated
    temp_order_ids = ask_for_order.split(',')
    # check if order ids are valid
    for order_id in temp_order_ids:
        if int(order_id) not in item_ids:
            print(f"""
Invalid order id: {order_id}
""")
            time.sleep(2)
            return False
    temp_order_details = {}
    for item in menu:
        for order_id in temp_order_ids:    
            # if item is already in order details then add quantity
            if item[2] in temp_order_details:
                print("yess, already in order details")
                print(temp_order_details)
                temp_order_details[item[2]]["qty"] += 1
            else:
                # if item is not in order details then add item
                if str(item[2]) in temp_order_ids:
                    temp_order_details[item[2]] = {"name": item[0], "price": item[1], "qty": 1}
                print(temp_order_details)
    print(temp_order_details)
    # print(type(item[2]))
    # print(type(temp_order_details[101]))
    # if all order ids are valid then return order details
    time.sleep(10)
    return temp_order_details



while True:
    screen_header()
    welcome_screen_cmd = input(f"""
    1. Login
    2. View Menu
    3. View Analytics
    4. Exit

    Enter command: """)

    if welcome_screen_cmd == "1":    
        while True:
            if login() == False:
                print("""
    Invalid username or password""")
                time.sleep(1)
            else:
                break
        print("""
                Loged in successfully""")
        time.sleep(1)
        main_menu()
        break
    elif welcome_screen_cmd == "2":
        show_menu()
    elif welcome_screen_cmd == "3":
        # view_analytics()
        print("Viewing Analytics...")
        pass
    elif welcome_screen_cmd == "4":
        # exit the program
        print("Exiting...")
        time.sleep(2)
        os._exit(0)
    else:
        pass
    
    