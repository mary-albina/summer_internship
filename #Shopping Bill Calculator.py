#Shopping Bill Calculator
item1 = float(input("Enter the price of item 1: "))
qnt1= float(input("Enter the quantity of item 1: "))
item2 = float(input("Enter the price of item 2: "))
qnt2= float(input("Enter the quantity of item 2: "))
item3 = float(input("Enter the price of item 3: "))
qnt3= float(input("Enter the quantity of item 3: "))
subtotal= (item1*qnt1)+ (item2*qnt2) + (item3*qnt3)
GST= subtotal*(18/100)
total= subtotal+GST
print(f"SUBTOTAL= {subtotal}")
print(f"GST= {GST}")
print(f"Total= {total}")
