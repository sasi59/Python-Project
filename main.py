from datetime import datetime
from read import *
from write import *
from operations import *



print("------------------------------------------------------------------------------------------------------------------------------------------------")
print(" \t \t \t \t \t \t \t Welcome to Shutter!")
print("------------------------------------------------------------------------------------------------------------------------------------------------")
print ("\n")


r=dict_update()


    
LooP = True
while LooP == True:
    print("1. Sell laptops to Customer")
    print("2. Purchase laptop from manifacturer")
    print("3. Exit")
    print("\n")
    exec = False
    while exec == False:
        try:
            opt= int(input("Enter the option to continue: "))
            exec = True
        except:
            print("No string allowed")

    print("\n")
    if opt == 1:
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("To generate bill, please provide the details: ")

        NamE = input("Enter your name: ")
        PhonE_NumbeR = input("Enter your phone number: ")
        print("\n")

        LaptoP_Purchase = []
        MorE_Products = True
        while MorE_Products== True:
            
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N      \t Product name              Brand \t \t Price \t  Quantity  \t\t Processor \t\t Graphics Card")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")


            tabular_format()

            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------" )
        
            print("\n")

            

            while True:
            #Validating id
                PurchasE_ID = ID_exception(r)
                if int(r[PurchasE_ID][3]) <= 0:
                    print("OUT OF STOCK")
                    print("\n")
                else:
                    PurchasE_Quantity = QuantitY_exception(r, PurchasE_ID)
                    break



            
            #d[PurchasE_ID][3] = int(d[PurchasE_ID][3]) - int(PurchasE_Quantity)
            print("\n")
            file_append_buy(r,PurchasE_ID, PurchasE_Quantity)
            LaptoP_Purchase= UpdatE_TablE(r,PurchasE_Quantity,LaptoP_Purchase,PurchasE_ID)

            
            while True:
                CustomeR_Request = input("Do you want to continue (Y/N)?").upper()
                print("\n")

                if CustomeR_Request == "Y":
                    MorE_Products = True
                    break

                elif CustomeR_Request == "N":
                    TOtaL = 0
                    ShippinG_Charge = 10
                    vat = 0.13
                    for i in LaptoP_Purchase:
                        TOtaL += int(i[3])

                    GranD_Total = vat * TOtaL + TOtaL + ShippinG_Charge

                    DateAndTimE = datetime.now()
                    dat = str(DateAndTimE).split(" ")
                    exec = "_".join(dat)
                    DAT = exec.replace(":","_")

                    TERMINAL_buy(NamE, PhonE_NumbeR, DateAndTimE, LaptoP_Purchase, TOtaL, ShippinG_Charge, GranD_Total)
                    
                    invoice_buy(NamE,DAT,PhonE_NumbeR,DateAndTimE,LaptoP_Purchase,TOtaL,ShippinG_Charge, GranD_Total)

                    
                    MorE_Products= False
                    break
                else:
                    print("Please enter correct input!")


    elif opt == 2:
        print("--------------------------------------------------------------------------------------------------------------------------------------")
        print("To generate bill, please provide the details: ")   
        

        NamE = "Shutter"
        PhonE_NumbeR = 1111111111
        print("\n")

        LaptoP_Purchase = []
        MorE_Products = True
        while MorE_Products== True:
            
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")
            print("S.N      \t Product name              Brand \t \t Price \t\t  Quantity  \t\t Processor \t\t Graphics Card")
            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------")


            tabular_format()

            print("--------------------------------------------------------------------------------------------------------------------------------------------------------------" )
        
            print("\n")

            
            
            
            PurchasE_ID = ID_exception(r)
            PurchasE_Quantity = QuantitY_exception_SELL()
            
            
            print("\n")
            file_append_sell(r, PurchasE_ID, PurchasE_Quantity)
            LaptoP_Purchase= UpdatE_TablE(r,PurchasE_Quantity,LaptoP_Purchase,PurchasE_ID)

            
            print("\n")

            while True:
                CustomeR_Request = input("Do you want to continue (Y/N)?").upper()
                print("\n")

                if CustomeR_Request == "Y":
                    MorE_Products = True
                    break

                elif CustomeR_Request == "N":
                    TOtaL = 0
                    ShippinG_Charge = 10
                    vat = 0.13
                    for i in LaptoP_Purchase:
                        TOtaL += int(i[3])

                    GranD_Total = vat * TOtaL + TOtaL + ShippinG_Charge

                    DateAndTimE = datetime.now()
                    x = str(DateAndTimE).split(" ")
                    exec = "_".join(x)
                    DAT = exec.replace(":","_")

                    TERMINAL_sell(NamE, PhonE_NumbeR, DateAndTimE, LaptoP_Purchase, TOtaL, ShippinG_Charge, GranD_Total)
                    
                    invoice_sell(NamE,DAT,PhonE_NumbeR,DateAndTimE,LaptoP_Purchase,TOtaL,ShippinG_Charge, GranD_Total)

                    
                    MorE_Products= False
                    break
                else:
                    print("Please give correct input!")


      





        print("\n")
        
    elif opt == 3:
        LooP = False
        print("Thank you for visiting our store!")
        print("\n")
    else:
        print("Your option", opt, "does not match. try again.")
        print("\n")
