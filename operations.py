def ID_exception(d):
    exec = False
    while exec == False:
        try:
            LaptoP_ID = int(input("Please enter the id: "))
        # Valid ID
            while LaptoP_ID <= 0 or LaptoP_ID > len(d):
                print("Please provide valid laptop ID!")
                print("\n")
                LaptoP_ID = int(input("Please enter the id: "))

            exec = True    
                
        except:
            print("No string allowed")
    return LaptoP_ID


            

def QuantitY_exception(d,LaptoP_ID):

    exec = False
    while exec == False:
        try: 
            laptoP_QuantitY = int(input("Enter the quantity of the laptop you want to purchase: "))       
            print("\n")
            # Valid Quantity
            DesireDQuantitY = d[LaptoP_ID][3]
            while laptoP_QuantitY <= 0 or laptoP_QuantitY > int(DesireDQuantitY):
                print("Dear user, the quantity you've asked for is not available right now.")
                print("\n")
                laptoP_QuantitY = int(input("Enter the quantity of laptop you want to purchase: "))
            exec = True 
        except:
                print("No string allowed")
    return laptoP_QuantitY



def QuantitY_exception_SELL():

    exec = False
    while exec == False:
        try: 
            laptoP_QuantitY = int(input("Enter the quantity of the laptop you want to purchase: "))       
            print("\n")
            exec = True 
        except:
                print("No string allowed")
    return laptoP_QuantitY


  
            

def UpdatE_TablE(d,CustomerQuantity,laptop_sold,PurchasE_ID):  
         
    ProducT_NamE = d[PurchasE_ID][0]
    SelecteDQuantitY = CustomerQuantity
    UniTPricE = d[PurchasE_ID][2]
    SelecteD_QuantitY_PricE = d[PurchasE_ID][2].replace("$", '')
    Total_Price = int(SelecteD_QuantitY_PricE) * int(SelecteDQuantitY)
    Graphics_card = d[PurchasE_ID][5]

    laptop_sold.append([ProducT_NamE, SelecteDQuantitY, UniTPricE, Total_Price, Graphics_card])
    return laptop_sold



