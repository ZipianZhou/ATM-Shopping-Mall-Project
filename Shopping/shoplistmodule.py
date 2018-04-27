goods = [{"name": "Computer", "price": 1999}, {"name": "Cupcake", "price": 10}, {"name": "Book", "price": 20},
         {"name": "Iphone", "price": 998}, ]
shoppingcart = []
import sys,os,creditpay
sys.path.append(os.path.dirname(sys.path[0]))
def shoplist():
    print('-------------List of product---------------')
    print("(Press q for checkout)")
    for index, p in enumerate(goods):
        print(index, p.get("name"), p.get("price"))

    choice = input('Please input the product number：')
    if choice.isdigit():
        choice = int(choice)
        expect = goods[choice]
        shoppingcart.append(goods[choice])
        print("Added product %s into shoppingcart." % (expect.get("name")))
        shoplist()

    elif choice == 'q':
        if shoppingcart == []:
            pass
        else:
            total=0
            print("You have selected:")
            for index, p in enumerate(shoppingcart):
                print(index, p.get("name"), p.get("price"))
                total+=int(p.get("price"))

            print("The total amount that you need to pay is $%s."%(total))
            creditpay.creditpay(total)
    else:
        print("Invalid Input. Please try again.")
        shoplist()