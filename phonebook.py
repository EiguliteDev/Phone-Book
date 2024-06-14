firstNlist = []
lastNlist = []
addressList = []
postalCodeList = []
phoneList  = []
fileName = "contact.txt"

print("Welcome to Phonebook!")
print()

# Create a new contact
def newContact(firstName, lastName, phoneNumber, address, postalCode):
    firstNlist.append(firstName)
    lastNlist.append(lastName)
    phoneList.append(phoneNumber)
    addressList.append(address)
    postalCodeList.append(postalCode)

    print("Contact added!")
    print()

# Deletes a contact based on first and last name
def deleteContact(firstName, lastName):
    if firstName in firstNlist and lastName in lastNlist:
        index = firstNlist.index(firstName)
        if lastNlist[index] == lastName:
            firstNlist.pop(index)
            lastNlist.pop(index)
            addressList.pop(index)
            postalCodeList.pop(index)
            phoneList.pop(index)
            
            print("Contact deleted!")
        else:
            print("Contact not found!")
    else:
        print("Contact not found!")

# Searches for a contact based on the choice
def findContact(data, nlpa):
    found = False

    if nlpa == "first":
        for i in range(len(firstNlist)):
            if firstNlist[i] == data:
                printContacts(i)
                found = True
    elif nlpa == "last":
        for i in range(len(lastNlist)):
            if lastNlist[i] == data:
                printContacts(i)
                found = True
    elif nlpa == "phone":
        for i in range(len(phoneList)):
            if phoneList[i] == data:
                printContacts(i)
                found = True
    elif nlpa == "postal":
        for i in range(len(postalCodeList)):
            if postalCodeList[i] == data:
                printContacts(i)
                found = True
    else:
        print("Incorrect input!")
    
    if not found:
        print("Contact not found!")

# Update Contact
def updateContact(firstName, lastName):
    if firstName in firstNlist and lastName in lastNlist:
        index = firstNlist.index(firstName)
        if lastNlist[index] == lastName:
            newFirstName = input("New first name: ")
            newLastName = input("New last name: ")
            newAddress = input("New address: ")
            newPostalCode = input("New postal code: ")
            newPhone = input("New phone number: ")

            firstNlist[index] = newFirstName
            lastNlist[index] = newLastName
            addressList[index] = newAddress
            postalCodeList[index] = newPostalCode
            phoneList[index] = newPhone

            print("Contact updated!")
        else:
            print("Contact not found!")
    else:
        print("Contact not found!")

# Prints a contact
def printContacts(index):
    print()
    print("Name: {} {}".format(firstNlist[index], lastNlist[index]))
    print("Address: {}".format(addressList[index]))
    print("Postal Code: {}".format(postalCodeList[index]))
    print("Phone: {}\n".format(phoneList[index]))

# Lists all contacts
def listAll():
    for i in range(len(firstNlist)):
        printContacts(i)

# Saves contacts into the "contact.txt" file
def saveContacts():
    writeFile = open(fileName, "w")
    for i in range(len(firstNlist)):
        writeFile.write("{},{},{},{},{}\n".format(firstNlist[i], lastNlist[i], addressList[i], postalCodeList[i], phoneList[i]))
    writeFile.close()

# Loads the contacts from the "contact.txt" file into the lists
def loadContacts():
    readFile = open(fileName, "r")
    lines = readFile.readlines()
    for line in lines:
        line = line.strip()
        if not line:
            continue

        firstName, lastName, address, postalCode, phone = line.split(',')

        firstNlist.append(firstName)
        lastNlist.append(lastName)
        addressList.append(address)
        postalCodeList.append(postalCode)
        phoneList.append(phone)

# Lists contacts with the last name starting letter
def listContacts(letter):
    for i in range(len(lastNlist)):
        if lastNlist[i].lower().startswith(letter):
            printContacts(i)

# Ends the program after saving
def quit():
    saveContacts()
    print("Contacts saved. End of program . . .")
    exit()

loadContacts()

while True:
    num = input("1. New Contact\n2. Delete Contact\n3. List All Contacts\n4. List Contacts\n5. Find Contact\n6. Update Contact\n7. Quit\n")
    if num == "1":
        firstName = input("First name: ")
        lastName = input("Last name: ")
        phoneNumber = input("Phone number: ")
        address = input("Address: ")
        postalCode = input("Postal code: ")
        newContact(firstName, lastName, phoneNumber, address, postalCode)
    elif num == "2":
        firstName = input("First name: ")
        lastName = input("Last name: ")
        deleteContact(firstName, lastName)
    elif num == "3":
        listAll()
    elif num == "4":
        letter = input("Starting letter of the last name: ").lower()
        listContacts(letter)
    elif num == "5":
        data = input("Enter first name, last name, phone number, or postal code: ")
        nlpa = input("Search by 'first', 'last', 'phone', or 'postal': ").lower()
        findContact(data, nlpa)
    elif num == "6":
        firstName = input("First name: ")
        lastName = input("Last name: ")
        updateContact(firstName, lastName)
    elif num == "7":
        quit()
    else:
        print("Invalid command. Please try again")
