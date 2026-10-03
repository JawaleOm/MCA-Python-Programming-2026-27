# 5_product_bill.py

subtotal = 0

for i in range(1, 4):
    price = float(input(f"Enter price of product {i}: "))
    quantity = int(input(f"Enter quantity of product {i}: "))
    subtotal += price * quantity

if subtotal >= 5000:
    discount = subtotal * 0.20
elif subtotal >= 3000:
    discount = subtotal * 0.10
elif subtotal >= 1000:
    discount = subtotal * 0.05
else:
    discount = 0

amount_after_discount = subtotal - discount
gst = amount_after_discount * 0.18
final_amount = amount_after_discount + gst

print("\nSubtotal =", subtotal)
print("Discount =", discount)
print("GST =", gst)
print("Final Payable Amount =", final_amount)