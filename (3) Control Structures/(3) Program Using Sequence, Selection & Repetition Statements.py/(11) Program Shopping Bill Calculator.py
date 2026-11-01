# Shopping Bill Calculator

print("===== SHOPPING BILL CALCULATOR =====")
total    = 0.0       # float - total bill amount
count    = 0         # int   - number of items
shopping = True      # bool  - controls the loop

# REPETITION: Keep adding items
while shopping:
    item = input("\nEnter Item Name (or 'done' to finish): ")
    # SELECTION: Check if user wants to stop
    if item.lower() == "done":
        shopping = False
    else:
        price = float(input(f"Enter Price of {item}: Rs. "))
        # SELECTION: Validate price
        if price <= 0:
            print("Invalid price! Try again.")
        else:
            total = total + price
            count = count + 1
            print(f"{item} added - Rs. {price:.2f}")

# --- Summary ---
print("\n======== BILL SUMMARY ========")
if count == 0:
    print("No items purchased.")
else:
    print(f"Total Items  : {count}")
    print(f"Total Bill   : Rs. {total:.2f}")

    # SELECTION: Apply discount based on total
    if total >= 5000:
        discount = total * 0.20
        label = "20% Discount"
    elif total >= 2000:
        discount = total * 0.10
        label = "10% Discount"
    else:
        discount = 0
        label = "No Discount"

    final = total - discount
    print(f"Discount     : {label}  (-Rs. {discount:.2f})")
    print(f"Final Bill   : Rs. {final:.2f}")
    print("===============================")