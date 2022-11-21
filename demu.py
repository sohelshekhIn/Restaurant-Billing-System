# hello= {}

# hello["Soh"] = {"name": "spje;"}
# print(hello)
# hello["Soh"]["name"] = "Sohel"
# hello[12]= {"name":"shekh"}
# print(hello)
# if 12 in hello:
#     print("Soh is in hello")
# print(type(hello))
b = 102
a = {101: {'name': 'Aloo Tikki Burger', 'price': 49.0, 'qty': 1}, 102: {'name': 'Paneer Tikka Burger', 'price': 99.0, 'qty': 1}}
if b in a:
    print("101 is in a")
    a[b]["qty"] += 1
print(a)