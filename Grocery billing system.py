import time
#Variables initialized
choice = 1
currentTotal = 0
price = 0
discount = 0



milkCounter = 0
juiceCounter = 0
chipsCounter = 0
chocolateCounter = 0
tissuesCounter = 0
yoghurtCounter = 0
icecreamCounter = 0
waterCounter = 0
energydrinkCounter = 0
gumCounter = 0            

#print heading statement
print("Welcome to the grocery store!")

#Required input id from user/customer

id = input("Please Enter your ID: ")
BDay = id[1:3]
BMonth = id[3:5]
BYear = int(id[5:9])       

while(choice!=0):
    print("Please select from the choices below: ")
    print("1.   Milk        :  2    AED")
    print("2.   Juice       :  3    AED")
    print("3.   Chips       :  0.99 AED")
    print("4.   Chocolate   :  3.50 AED")
    print("5.   Tissues     :  2.5  AED")
    print("6.   Yoghurt     :  1.5  AED")
    print("7.   Ice Cream   :  4    AED")
    print("8.   Water       :  1    AED")
    print("9.   Energy Drink:  5.50 AED")
    print("10.  Gum         :  1.5  AED")          #These are the choices for you to select from those, what u want.

    choice = int(input("Enter choice from 1-10. Enter 0 to Exit: "))
    
    if choice >=11 or choice<=-1: #Here you can not put more than 10 and less than 1.
        print("Error, Please enter a valid number from 1-10")
        continue
    
    if choice == 0:
        break           #if choice is 0 then it would be exit.

    quantity = int(input("How many do you want? "))  #asking for quantity.
    if choice == 1:
        price = 2
        print(quantity," Milk Selected")
        milkCounter+=quantity           #quantity added.
    elif choice == 2:
        price = 3
        print(quantity," Juice Selected")
        juiceCounter+=quantity
    elif choice == 3:
        price = 0.99
        print(quantity," Chips Selected")
        chipsCounter+=quantity
    elif choice == 4:
        price = 3.50
        print(quantity," Chocolate Selected")
        chocolateCounter+=quantity
    elif choice == 5:
        price = 2.5
        print(quantity," Tissues Selected")
        tissuesCounter+=quantity
    elif choice == 6:
        price = 1.5
        print(quantity," Yoghurt Selected")
        yoghurtCounter+=quantity
    elif choice == 7:
        price = 4
        print(quantity," Ice Cream Selected")
        icecreamCounter+=quantity
    elif choice == 8:
        price = 1
        print(quantity," Water Selected")
        waterCounter+=quantity
    elif choice == 9:
        price = 5.50
        print(quantity," Energy Drink Selected")
        energydrinkCounter+=quantity
    else:
        price = 1.5
        print(quantity," Gum Selected")         # From choice 1-10 same coding just to get quantity of items.
        gumCounter+=quantity

    currentTotal = currentTotal + (quantity * price)    #Simple formula for calculating the prices of items.

    print("Your current total is ",currentTotal," AED")

print("Thank you for shopping with us!") #Final message

time.sleep(2)

print("ID: ",id) #This is used to show the input id on summary of shopping.

value = id[0]

age = 2020 - BYear

if age>70:           #This is for age older people, those who are more than 70 years , will be awarded with discount.
    if value=='a' or value=='A':
        print("You are entitled to a 15% discount!")
        discount = round(currentTotal*.15,2)
        print("Your total before the discount is ",currentTotal," AED")
        print("Discount Amount is ",discount," AED")
        finalCost = round(currentTotal-discount,2)
        print("Your total after discount is ",finalCost," AED")  #Final prices after cutting discounts

finalCost = round(currentTotal - discount,2)
freeMilk = int(milkCounter/2)
milkCounter+=freeMilk

freeJuice=int(juiceCounter/2)
juiceCounter+=freeJuice

freeChips=int(chipsCounter/2)
chipsCounter+=freeChips

freeChocolate=int(chocolateCounter/2)
chocolateCounter+=freeChocolate

freeTissues=int(tissuesCounter/2)
tissuesCounter+=freeTissues

freeYoghurt=int(yoghurtCounter/2)
yoghurtCounter+=freeYoghurt

freeIcecream=int(icecreamCounter/2)
icecreamCounter+=freeIcecream

freeWater=int(waterCounter/2)
waterCounter+=freeWater

freeEnergydrink=int(energydrinkCounter/2)
energydrinkCounter+=freeEnergydrink

freeGum=int(gumCounter/2)
gumCounter+=freeGum          #These above all will be gifted as free to you.

print("Total Bill to pay ",finalCost," AED")
print("Shopping Summary:")
print("Milk            :",milkCounter)
print("Juice           :",juiceCounter)
print("Chips           :",chipsCounter)
print("Chocolate       :",chocolateCounter)
print("Tissues         :",tissuesCounter)
print("Yoghurt         :",yoghurtCounter)
print("Ice Cream       :",icecreamCounter)
print("Water           :",waterCounter)
print("Energy Drink    :",energydrinkCounter)
print("Gum             :",gumCounter)                   #This is the summary of your purchases.

print("You got ",freeMilk," free Milk")
print("You got ",freeJuice," free Juice")
print("You got ",freeChips," free Chips")
print("You got ",freeChocolate," free Chocolate")
print("You got ",freeTissues," free Tissues")
print("You got ",freeYoghurt," free Yoghurt")
print("You got ",freeIcecream," free Ice Cream")  
print("You got ",freeWater," free Water")
print("You got ",freeEnergydrink," free Energy Drink")
print("You got ",freeGum," free Gum")    #This is what you got free.
