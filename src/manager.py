'''
Created on 12-Jun-2016

@author: pavitra-ubuntu

Driver module
'''

#import ContactList as ContactList
#import ContactListV1 as ContactList
import ContactListV2 as ContactList

if __name__ == '__main__':
    
    choice = 0
    cl = ContactList.ContactList()
    
    while (choice != 4):
        print ("Menu: 1) Add contact    2) Search contact    3) Show all contacts    4) Exit")
        try:
            choice = int(input("Please enter choice..."))
        except (ValueError, NameError) as e:
            print("Invalid number")
            continue
        except SyntaxError:
            print("Need something...")
            continue
            
        if (choice == 1):
            name = raw_input("Enter name :")
            if name:
                try:
                    cl.add_contact(name)
                except ValueError as e:
                    print (e)
            else:
                print("Contact needs at least a name")
            continue
            
        if (choice == 2):
            name = raw_input("Enter name :")
            if name:
                result = cl.search_contact(name)
                for contact in result:
                    print(contact)
            else:
                print ("Need a search term")
            continue
                
        if (choice == 3):
            result = cl.show_all_contacts()
            for contact in result:
                print(contact)
            continue
                
        if (choice == 4):
            print("Happy Searching")
            exit(0)
            
        if (choice < 1 or choice > 4):
            print ("Wrong choice")
            
       
        