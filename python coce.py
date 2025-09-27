veg=['tomotoes','chilles','ladyfingeres','potatoes','brinjals','onions']
quantity=[40,20,25,45,30,60]
selling_price=[30,25,35,45,20,30]
original_price=[20,20,25,30,15,20]
customer_veg=[]
veg_qty=[]
customer_name=[]
customer_number=[]
selling_veg=[]
sel_veg_price=[]
Total_Amount=0
Profit=0
sold_veg=[]
sold_qty=[]
while True:
    mode = input('Enter your option(1-shopkeeper/2-user/3-exit): ')
    if mode.isalpha():
        print("enter correct option")
    username = 'narendra'
    password = 'narendra2369'
    if mode == '1':
        print(' '*20,'*'*10,'Shopkeeper','*'*10)
        user_name = input('Enter username: ')
        pswrd = input('Enter your password: ')
        if user_name == username and pswrd == password:
            for v,or_p,qua in zip(veg,quantity,original_price):
                print(v, '-', or_p, 'kgs', '-', qua, 'per kg')
                print()
            print('' * 10, 'SHOPKEEPER MENU', '' * 10)
            while True:
                
                    print('*'*10,"Iventory",'*'*10)
                    print('1.Add items to iventory')
                    print('2.Remove items to iventory')
                    print('3.Update items to inventory')
                    print('4.view inventory')
                    print('5.view users Details')
                    print('6.view Report')
                    print('7.total revenue and itemized profit')
                    print('8.Exit')
                    ch=input("Enter An option:")
                    if ch.isalpha():
                        print('enter correct option')
                    if ch=='1':
                        while True:
                            item=input("Enter a new item:")
                            if item not in veg:
                                item_qty=float(input("Enter the Quantity: "))
                                item_selling_price=int(input("Enter the selling_Price per KG: "))
                                item_original_price=int(input("Enter the original_price per KG: "))
                                veg.append(item)
                                quantity.append(item_qty)
                                selling_price.append(item_selling_price)
                                original_price.append(item_original_price)
                                print(item,'is added')
                            else:
                                print(item,'is already in veg')
                            stop=input('do you want to add any item to inventory(yes/no):')
                            if stop=='no':
                                break
                    elif ch=='2':
                        while True:
                            item=input('enter which vegetable do you want to remove: ')
                            if item in veg:
                                idx=veg.index(item)
                                veg.pop(idx)
                                quantity.pop(idx)
                                selling_price.pop(idx)
                                original_price.pop(idx)
                                print(item,'is removed from list')
                            else:
                                print(item,'is not available to remove')
                            stop=input('do you want to remove any other item from cart(yes/no):')
                            if stop=='no':
                                break
                    elif ch=='3':
                        while True:
                            item=input('enter which vegetable do you want to update:')
                            if item in veg:
                                idx=veg.index(item)
                                ch_qnty=input('do you want to update the item quantity(yes/no):')
                                if ch_qnty=='yes':
                                    new_quantity=float(input('Enter quantity to update item quantity :'))
                                    quantity[idx]=quantity[idx]+new_quantity
                                    print('new quantity updated')
                                ch_selling_price=input('do you want to update the selling price of this item(yes/no):')
                                if ch_selling_price=='yes':
                                    new_price=int(input('enter new price to update:'))
                                    selling_price[idx]=selling_price[idx]+new_price
                                ch_original_price=input('do you want to update original_price(yes/no):')
                                if ch_original_price=='yes':
                                    new_original_price=int(input('enter original price to update:'))
                                    original_price[idx]=original_price[idx]=new_original_price
                            else:
                                print(item,'not available')
                            stop=input('do you want to modify any item quantity or price(yes/no):')
                            if stop=='no':
                                break
                    elif ch=='4':
                        print(f'Vegname  Quantity  selling_price')
                        for vname, qty, prc in zip(veg, quantity,selling_price):
                            print(vname, '-', qty, 'kgs', '-', prc, 'per kg')
                    elif ch=='5':
                        if len(customer_name)==0 and len(customer_number)==0:
                               print('customer is not avilable')
                        else:
                            for k,v in zip(customer_name,customer_number):
                                print(k,'-',v)
                    elif ch=='6':
                        for k,v,m,n in zip(veg,quantity,selling_price,original_price):
                            print(k,'-',v,'kgs','-',m,'rs','selling price','-', n,'original price')
                    elif ch=='7':
                        total_price=0
                        print("totalprofit-",Profit)
                        for i, j in zip(sold_veg, sold_qty):
                            if i in veg:
                                idx = veg.index(i)
                                total_price = j * (selling_price[idx] - original_price[idx])
                                print(i, '-', total_price)
                            else:
                                print(f"{i} was sold but is no longer in inventory. Cannot calculate profit.")
                    elif ch=='8':
                        stop=input('do you want to close the shop(yes/no):')
                        if stop=='yes':
                            break
                    else:
                        print("enter correct option")
    elif mode=="2":
        print(' '*20,'*'*10,'Customer','*'*10)
        for v,or_p,qua in zip(veg,quantity,original_price):
                print(v, '-', or_p, 'kgs', '-', qua, 'per kg')
                print()
        while True:
            print('1.add cart')
            print('2.remove cart')
            print('3.modify cart')
            print('4.view cart')
            print('5.biling')
            print('6.exit')
            ch=input('select one option from above:')
            if ch.isalpha():
                print("enter correct option")
            if ch == '1':
                while True:
                    item = input('Which vegetable you want to add to cart: ')
                    if item in veg:
                        if item in customer_veg:
                            print(item, 'is already in cart')
                        else:
                            customer_veg.append(item)
                            print(item, "is added to the cart")
                            qty=float(input('how many kgs do you want:'))
                            idx=veg.index(item)
                            if qty<=quantity[idx]:
                                veg_qty.append(qty)
                                print(qty," kgs is added to the cart")
                    else:
                        print("out of the stock")
                    ch=input("do you want add another item(yes/no):")
                    if ch=='no':
                        break
            elif ch == '2':
                while True:
                    item = input('Which vegetable you want to remove: ')
                    if item in customer_veg:
                        idx=customer_veg.index(item)
                        customer_veg.pop(idx)
                        veg_qty.pop(idx)
                        print(item, 'has been removed from cart')
                    
                    else:
                        print(item, 'is not in cart')
                    ch=input("do you want remove another item(yes/no):")
                    if ch=='no':
                        break
            elif ch=='3':
                while True:
                    item=input('which item do you want to modify:')
                    if item in customer_veg:
                        idx=customer_veg.index(item)
                        ch=input('do you want to modify your quantity(increase/decrease):')
                        qty=float(input('how much quantity do you want to modify:'))
                        if ch=='increase':
                            veg_qty[idx]=veg_qty[idx]+qty
                        else:
                            veg_qty[idx]=veg_qty[idx]-qty
                    else:
                        print('out of stock')
           
                    stop=input('do you want to modify any item(yes/no):')
                    if stop=='no':
                        break
            elif ch=='4':
                print(f'customer_veg veg_qty')
                for k,v in zip(customer_veg,veg_qty):
                    print(k,'-',v,'kgs')
            elif ch=='5':
                if len(customer_veg)!= len(veg_qty):
                    print("Cart item list and quantity list are not equal. Something went wrong.")
                else:
                    for i in range(len(customer_veg)):
                        item = customer_veg[i]
                        idx = veg.index(item)
                        quantity[idx] = quantity[idx] - veg_qty[i]

                        Amount = veg_qty[i] * selling_price[idx]
                        Total_Amount += Amount
                        Profit += Amount - veg_qty[i] * original_price[idx]

                        selling_veg.append(item)
                        sel_veg_price.append(Amount - veg_qty[i] * original_price[idx])

                        if item not in sold_veg:
                            sold_veg.append(item)
                            sold_qty.append(veg_qty[i])
                        else:
                            sol_idx = sold_veg.index(item)
                            sold_qty[sol_idx] += veg_qty[i]

                cust_name = input('Enter customer name: ')
                cust_number = input('Enter customer mobile number: ')  # Keep it as a string for length check

                if len(cust_number) == 10 and cust_number.isdigit():  # Ensure it's 10 digits and numeric
                    customer_name.append(cust_name)
                    customer_number.append(cust_number)
                    print('pay the bill:', Total_Amount)
                    customer_veg.clear()
                    veg_qty.clear()
                    Total_Amount = 0

                else:
                    print("correct number")
           
                
           
                    

            elif ch=='6':
                stop=input('do you want to exit(yes/no):')
                if stop=='yes':
                    break
            else:
                print("enter correct option")
    elif mode=='3':
        print("exit")
        break
