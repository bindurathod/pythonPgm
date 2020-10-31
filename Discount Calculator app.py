amt = int(input("Enter Sale Amount: "))

# checking conditions and calculating discount
if(amt>0):
    if amt<=1000:
       disc = amt*0.00
    elif amt<=2000:
        disc=amt*0.1
    elif amt<=3000:
        disc= 0.2 * amt
    else:
         disc=0.25 * amt

    print("Discount : ",disc)
    print("Net Pay  : ",amt-disc)
else:
    print("Invalid Amount")
