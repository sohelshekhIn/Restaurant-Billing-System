# import pywinusb.hid as hid

# # Set up a callback function to handle USB events
# def on_event(data):
#     print(f'USB event: {data}')

# # Find all HID devices connected to the system
# all_devices = hid.HidDeviceFilter(vendor_id=0x0000, product_id=0x0000).get_devices()

# # Register the callback function for each device
# for device in all_devices:
#     try:
#         device.set_raw_data_handler(on_event)
#     except Exception as ex:
#         print(f'Error setting data handler: {ex}')

# # Run the event loop to listen for USB events in the background
# while True:
#     hid.check_for_events()

# import sqlite3
# conn = sqlite3.connect('billing_system.db')
# c = conn.cursor()
# c.execute("INSERT INTO menu VALUES (?, ?, ?)", ("Cheese Burger", 79, 102))
# conn.commit()
a = "123"
def hi():
    print(a)
    
hi()