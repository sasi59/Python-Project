def TERMINAL_buy(NamE, PhonE_NumbeR, DateAndTime, LaptoP_SolD, TOtaL, ShippinG_Charge, GranD_Total):
    
            print("\n")
            print("\t \t \t \t \t \t \t Shutter Bill")
            print("\n")
            print("\t \t \t \t \t Chabahil , Kathmandu | Phone no: 1111111111")
            print("\n")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            print("Product details: \n")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            print("Customer's Name: "+ str(NamE))
            print("Contact number: "+ str(PhonE_NumbeR))
            print("Date and time of purchase: "+ str(DateAndTime))
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            print("\n")
            print("Purchase Details are: ")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            for i in LaptoP_SolD:
                print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
            print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
            print("Your total is : $"+str (TOtaL))
            print("Your Shipping charge is : $", ShippinG_Charge)
            print("Vat : 13%")
            print("Grand Total : $"+ str(GranD_Total))
            print("\n")

def invoice_buy(NamE, yr, PhonE_Number, DateAndTime, LaptoP_Sold, TOtaL, ShippinG_Charge, GranD_Total):
        file= open(str(NamE)+"_"+str(yr)+".txt", "w")
        file.write("\n")
        file.write("\t \t \t \t \t \t \t Shutter Bill")
        file.write("\n")
        file.write("\t \t \t \t \t Chabahil, Kathmandu | Phone no: 1111111111")
        file.write("\n" )
        file.write("\nCustomer's Name: " + str(NamE))
        file.write("\nContact number: " + str(PhonE_Number))
        file.write("\nDate and time of purchase: " + str(DateAndTime))
        file.write("\n" )
        file.write("\n")
        file.write("Purchase Details are: ")
        file.write("\n------------------------------------------------------------------------------------------------------------------------\n" )
        file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        file.write("\n------------------------------------------------------------------------------------------------------------------------ \n" )


        for i in LaptoP_Sold:
            file.write(str(i[0])+"\t\t\t "+str(i[1])+"\t\t\t\t\t\t "+str(i[2])+"\t\t\t\t\t\t\t"+"$"+str(i[3]) +"\n")


        file.write("------------------------------------------------------------------------------------------------------------------------" )
        file.write("\nYour total is : $" + str(TOtaL))
        file.write("\nYour Shipping charge is : $ " +""+ str(ShippinG_Charge) +"\n")
        file.write("Vat : 13%")
        file.write("\nGrand Total : $" + str(GranD_Total))
        file.write("\n")
        file.close()

def TERMINAL_sell(NamE, PhonE_NumbeR, DateAndTime, LaptoP_Sold, TotaL, ShippinG_Charge, GranD_Total):
        print("\n")
        print("\t \t \t \t \t \t \t Maanifacturer")
        print("\n")
        print("\t \t \t \t \t Chabahil , Kathmandu | Phone no: 1000000000")
        print("\n")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
        print("Product details: \n")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
        print("Customer's Name: "+ str(NamE))
        print("Contact number: "+ str(PhonE_NumbeR))
        print("Date and time of purchase: "+ str(DateAndTime))
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
        print("\n")
        print("Purchase Details are: ")
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
        print("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        print("-")
        for i in LaptoP_Sold:
            print(i[0], "\t\t\t" ,i[1], "\t\t\t " ,i[2], "\t\t\t " ,"$", i[3] )
        print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ")
        print("Your total is : $"+str (TotaL))
        print("Your Shipping charge is : $", ShippinG_Charge)
        print("VAT: 13%")
        print("Grand Total : $"+ str(GranD_Total))
        print("\n")

def invoice_sell(NamE,yr, PhonE_Number, DateAndTime, LaptoP_Sold, TOtaL, ShippinG_Charge, GranD_Total):
        file= open(str(NamE)+ str(yr)+ ".txt", "w")
        file.write("\n")
        file.write("\t \t \t \t \t \t \t Manifacturer")
        file.write("\n")
        file.write("\t \t \t \t \t Chabahil, Kathmandu | Phone no: 1000000000")
        file.write("\n" )
        file.write("\nCustomer's Name: " + str(NamE))
        file.write("\nContact number: " + str(PhonE_Number))
        file.write("\nDate and time of purchase: " + str(DateAndTime))
        file.write("\n" )
        file.write("\n")
        file.write("Purchase Details are: ")
        file.write("\n------------------------------------------------------------------------------------------------------------------------\n" )
        file.write("Product Name \t \t Total Quantity \t\t Price(per piece) \t\t\t Total")
        file.write("\n------------------------------------------------------------------------------------------------------------------------ \n" )


        for i in LaptoP_Sold:
            file.write(str(i[0])+"\t\t\t "+str(i[1])+"\t\t\t\t\t\t "+str(i[2])+"\t\t\t\t\t\t\t"+"$"+str(i[3]) +"\n")


        file.write("------------------------------------------------------------------------------------------------------------------------")
        file.write("\nYour total is : $" + str(TOtaL))
        file.write("\nYour Shipping charge is : $" + str(ShippinG_Charge) +"\n")
        file.write("Vat : 13% \n")
        file.write("\nGrand Total : $" + str(GranD_Total))
        file.write("\n")
        file.close()


def file_append_buy(d, PurchasE_ID, PurchasE_Quantity):
    d[PurchasE_ID][3] = int(d[PurchasE_ID][3]) - int(PurchasE_Quantity)
    file = open("file.txt", "w")

    for values in d.values():
            file.write(str(values[0])+ "," +str(values[1])+ "," +str(values[2])+ "," +str(values[3])+ "," +str(values[4]+ "," +str(values[5])))
            file.write("\n")
    file.close()


def file_append_sell(d, PurchasE_ID, PurchasE_Quantity):
    d[PurchasE_ID][3] = int(d[PurchasE_ID][3]) + int(PurchasE_Quantity)
    file = open("file.txt", "w")

    for values in d.values():
            file.write(str(values[0])+ "," +str(values[1])+ "," +str(values[2])+ "," +str(values[3])+ "," +str(values[4]+ "," +str(values[5])))
            file.write("\n")
    file.close()
    

