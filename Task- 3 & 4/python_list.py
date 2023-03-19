#3-1. Names:
Names = ['Ali','Usman','Shazam','Zahid']
for i in range(0,len(Names)):
    print(Names[i])


#3-2. Greetings
for i in range(0,len(Names)):
    print("Hello!",Names[i])

#3-3. Your Own List
transport = ['Honda CG150cc','Yamaha R6', 'Suzuki GSXR 1000','Suzuki Hayabusa']
for i in range(0,len(transport)):
    print("I would like to own a",transport[i])

#3-4. Guest List
guest_list = ["Ahmad","Hassan","Qasim","Rimzan"]
for i in range(0,len(transport)):
    print("Hi,", guest_list[i],"I would like to invite you on Dinner!")

#3-5. Changing Guest List
guest_list.remove("Qasim")
guest_list.append("Ali Haider")
for i in range(0,len(transport)):
    print("Hi,", guest_list[i],"I would like to invite you on Dinner!")

#3-6. More Guests
guest_list.insert(0,"Imran")
guest_list.insert(-1,"Haider")
guest_list.append("Safdar")
for i in range(0,len(transport)):
    print("Hi,", guest_list[i],"I would like to invite you on Dinner!")



#3-7. Shrinking Guest List
for i in range(0,len(list())):
    print("I'm Sorry i can't invite you on dinner",guest_list[i])
    guest_list.pop()
    if len(guest_list) <= 2:
        break

for i in range(0,len(guest_list)):
    print("Hi", guest_list[i],"you are stil invited on dinner")

del guest_list
