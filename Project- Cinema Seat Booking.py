#Cinema Hall - Seat Booking Booking System
print("Cinema Hall - Seat Booking Booking System")
seats = []
seats.append([0,0,1,0,1,1,0,1])
seats.append([0,1,1,0,0,1,0,1])
seats.append([1,0,0,1,1,1,0,0])
seats.append([0,1,0,1,1,0,0,1])
seats.append([0,0,1,1,0,1,0,0])
seats.append([1,0,0,1,0,1,1,0])

#Password
def password():
    if passwd=='python':
        print("System Online")
        print("")
    else:
        print("Access Denied")
        sys.exit()
             
#Menu
print("")
print("\tMENU")
print(" 0. Display Menu \n 1. Display Bookings \n 2. Check Seat Availability \n 3. Book Seat \n 4. Book Seat at the front \n 5. Book Seat at the back \n 6. Cancel Booking \n 7. Cancel All Booking \n 8. Load Booking from file \n 9. Save bookings in a file \n 10. Exit " )
print("")

#Displays MENU
def displayMenu():
    print("")
    print("\tMENU")
    print(" 0. Display Menu \n 1. Display Bookings \n 2. Check Seat Availability \n 3. Book Seat \n 4. Book Seat at the front \n 5. Book Seat at the back \n 6. Cancel Booking \n 7. Cancel All Booking \n 8. Load Booking from file \n 9. Save bookings in a file \n 10. Exit" )
    print("")
    
#Displays all Seats
def displayBookings():
  print("===========================================")
  print("                  SCREEN             ")  
  print("")
  for row in seats:
    print("\t",row)
  print("")
  print("1 = Seat is Booked.")
  print("0 = Seat is Available")
  print("")
  print("===========================================")
  print("")

#Load Bookings from File
def loadBookings():
  file = open("seats.txt","r")
  row = 0
  for line in file:
    data = line.split(",")
    if len(data)==8: #Only process lines which contain 8 values
        for column in range (0,8):
            seats[row][column] = int(data[column])
        row = row + 1
  file.close()
  print("Bookings Loaded")

#Seat availability checking
def checkSeat():
  row = int(input("Enter a row number (between 0 and 5)"))
  column = int(input("Enter a column number (between 0 and 7)"))
  if seats[row][column]==1:
    print("This seat is already booked.")
  else:
    print("This seat is empty.")

#Booking Seat
import random
def bookSeat():
  booked = False
  F=open("BookingDetails.txt",'a')
  while booked == False:
    row = int(input("Enter a row number (between 0 and 5)"))
    column = int(input("Enter a column number (between 0 and 7)"))
    if seats[row][column]==1:
      print("This seat is already booked.")
    else:
      print("This seat is empty.")
      #Details
      Name=input("Enter Customer Name :")
      BookingIDD=random.randint(47136834,6753845683)
      BookingID=str(BookingIDD)
      F.write("\n")
      F.write(BookingID+'      ')
      F.write(Name+'                  ')
      F.write(str(row)+','+str(column))
      print("Booking seat...")
      seats[row][column]=1
      print("We have now booked this seat for you.")
      print("Your Booking ID is",BookingID)
      booked=True
      F.close()

#Booking Seat at the front
def bookSeatAtFront():
  print("Booking seat at the front")
  F=open("BookingDetails.txt",'a')
  for row in range(0,6):
    for column in range(0,8):
      if seats[row][column]==0:
        Name=input("Enter Customer Name :")
        BookingIDD=random.randint(47136834,6753845683)
        BookingID=str(BookingIDD)
        F.write("\n")
        F.write(BookingID+'      ')
        F.write(Name+'                  ')
        F.write(str(row)+','+str(column))
        print("Booking seat...")
        print("Row: ", str(row))
        print("Column: ", str(column))
        seats[row][column]=1
        print("We have now booked this seat for you.")
        F.close()
        return True
  print("Sorry the theatre is full - Cannot make a booking")
  return False




#Booking Seat at the Back
def bookSeatAtBack():
  print("Booking seat at the back")
  F=open("BookingDetails.txt",'a')
  for row in range(5,-1,-1):
    for column in range(7,-1,-1):
      if seats[row][column]==0:
        Name=input("Enter Customer Name :")
        BookingIDD=random.randint(47136834,6753845683)
        BookingID=str(BookingIDD)
        F.write("\n")
        F.write(BookingID+'      ')
        F.write(Name+'                  ')
        F.write(str(row)+','+str(column))
        print("Booking seat...")
        print("Row: ", str(row))
        print("Column: ", str(column))
        seats[row][column]=1
        print("We have now booked this seat for you.")
        F.close()
        return True
  print("Sorry the theatre is full - Cannot make a booking")
  return False


#Cancelling Seat Booking
def CancelBooking():
  booked = False
  while booked == False:
    row = int(input("Enter a row number (between 0 and 5)"))
    column = int(input("Enter a column number (between 0 and 7)"))
    if seats[row][column]==1:
        seats[row][column]=0
        print("Booking Cancelled")
        return True
    else:
        print("Seat is not booked")
        return True

#Cancelling All Booking
def CancelAllBooking():
    for row in range(0,6):
        for column in range(0,8):
            seats[row][column]=0
    print("All Booking Cancelled")

#Save Booking in file
def saveBookings():
  file = open("seats.txt","w")
  for row in range(0,6):
    line=""
    for column in range(0,8):
      line = line + str(seats[row][column]) + ","
    line = line[:-1] + ("\n") #Remove last comma and add a new line
    file.write(line)    
  file.close()
  print("Booking saved in seats.txt")







    
#Main Program
import sys
passwd= input("Enter the password to access the booking system:")
while True:
    password()
    break

F1=open("BookingDetails.txt",'w')
F1.write("Booking ID"+'      ')
F1.write("Name of Customer"+'      ')
F1.write("Seat Number"+'      ')
F1.close()
   

while True:
    choice= int(input("Enter your choice:"))
    print("")
    if choice==0:
        displayMenu()
    elif choice==1:
        displayBookings()
    elif choice==2:
        checkSeat()
    elif choice==3:
        bookSeat()
    elif choice==4:
        bookSeatAtFront()
    elif choice==5:
        bookSeatAtBack()
    elif choice==6:
        CancelBooking()
    elif choice==7:
        CancelAllBooking()
    elif choice==8:
        loadBookings()
    elif choice==9:
        saveBookings()
    else:
        print("Exiting...")
        sys.exit()
    print("")

#End of Program






