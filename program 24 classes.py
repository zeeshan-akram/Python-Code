class Shopping:
    def shoes(self):
        footwear = input("""We have only 
Sneakers.
Formal.
Joggers.
> """).lower()
        if footwear == 'sneakers' or footwear == 'sneaker':
            print("Added to your shopping cart...")
        elif footwear == 'formal':
            print("Added to your shopping cart...")
        elif footwear == 'joggers' or footwear == 'jogger':
            print("Added to your shopping cart...")
        else:
            print("We don't have that.")
    def cloths(self):
        cloth = input("""We have only
Jeans.
Chinos
Dress
> """).lower()
        if cloth == 'jeans' or cloth == 'jean':
            print("Added to your shopping cart...")
        elif cloth == 'chinos' or cloth == 'chino':
            print("Added to your shopping cart...")
        elif cloth == 'dress' or cloth == 'formal':
            print("Added to your shopping cart...")
        else:
            print("We don't have this item.")


cart = Shopping()
shop = input('''What do you want to shop.
Cloths?
Shoes?
> ''').lower()
if shop == 'cloths' or shop == 'cloth':
    cart.cloths()
    cart.foot = 'Price is $50.'
    print(cart.foot)
elif shop == 'shoe' or shop == 'shoes':
    cart.shoes()
    cart.bottom = 'Price is $70.'
    print(cart.bottom)
else:
    print('Sorry! ')