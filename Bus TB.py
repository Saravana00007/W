import time
print("Welcome to BTB App")
bus={1:"Kuppam To Anantapur",2:"Kuppam To Benglure",3:"Benglure To Anantapur",4:"Kuppam To Gudapalli",5:"Kuppam To Ramkuppam",6:"Kuppam to V.Kota"}
busc1=50
busc2=50
busc3=50
busc4=50
busc5=50
busc6=50
busbl1=[]
busbl2=[]
busbl3=[]
busbl4=[]
busbl5=[]
busbl6=[]
time.sleep(2)
while True:
    print("1.Show the bus list:\n2.Booking ticket")
    opt=int(input("Enter no:"))
    if opt==1:
        print("1",bus[1],"\n2",bus[2],"\n3",bus[3],"\n4",bus[4],"\n5",bus[5],"\n6",bus[6])
    if opt==2:
        while True:
            print("1.Kuppam To Anantapur.\n2.Kuppam To Benglure.\n3.Benglure To Anantapur.\n4.Kuppam To Gudapalli.\n5.Kuppam To Ramkuppam.\n6 Kuppam to V.Kota")
            opt=int(input("Enter a Bus No:"))
            if opt==1:
                while True:
                    print("1.Available Seats\n2.Book a Seat\n3.Exit")
                    opt=int(input("Enter a No:"))
                    if opt==1:
                        print("Avalliable Seates:",busc1)
                    elif opt==2:
                        print("Book a seat 1 between 50")
                        seat=int(input("Enter a Seat  avalible No:"))
                        if seat <=50:
                            busc1 -=seat
                            busbl1.append(seat)
                            print("The Distance Kms:200 Kms")
                            print("Rupess:",seat*200*25)
                            print("Successfully Booked :",seat)
                            print("Successfully Booked :",busbl1)

                    elif opt==3:
                        break

                    else:
                        print("Your entered number is not a available")
                    
            
            else:
                print("Your entered number is not a available")