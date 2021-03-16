shoppingbasket = {

}

print("""Please select one of the Following:
********************************************

1. Add Item
2. View Cart
3. Remove item
4. Compute Total
5. Exit 

*******************************************
""")    
print()
choice = int(input("Enter your option. "))

while choice != 5:
    if choice == 1:
        item = input("Enter an Item: ")

        if item in shoppingbasket:
            print("item already in shopping basket")
            qnty = int(input("Enter the Quantity: "))
            shopping.basket[item] = shoppingbasket[item] + qnty
        else:
            qnty = int(input("Enter the Quantity: "))
            shoppingbasket[item] = qnty
    
    elif choice == 2:
        item = input("Enter an Item: ")
        del(shoppingbasket)
    
    elif choice == 3:
        for item in shoppingbasket:
            print(item, ":", shopping.basket[item])

    
    # elif choice == 4:
    #     total = 

    elif choice != 0:
        print("You didn't enter a valid number.")

    choice = int(input("\n\nEnter your choice"))

else:
    print("Shopping basket progream closed")

# cart_items = ["Milk $2.50", "Eggs $1.99", "Cheese $3.25", "Bread $1.00", "Butter $2.55"]
# for x in cart_items:
#     print(x)
