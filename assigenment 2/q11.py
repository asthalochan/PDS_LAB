name = input("Enter consumer name: ")
unit = int(input("Enter units used: "))

if unit<=199:
    charge = 1.20*unit
elif unit >=200 and unit <400:
    charge = (199*1.20) + ((unit - 199)*1.50)
elif unit >=400 and unit <600:
    charge = (199*1.20) + (200*1.50)+ ((unit-400)*1.80)
else:
    charge =  (199*1.20) + (200*1.50) + (200*1.8)+ ((unit-400)*2.00)

if charge<100:
    net = 100  
elif charge > 400:
    net = 400 + (400*0.15)
else:
    net = charge

print(f"Hey! {name}\nYou have to pay: ₹{round(net,2)}")


