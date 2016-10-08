'''
Created on 12-Jun-2016

@author: pavitra-ubuntu

Brute force search implementation

'''

import Contact

class ContactList:
    '''
    Class to maintain all contacts and provide methods to manage them
    '''

    def __init__(self):
        self.contact_list = []
        self.contact_total = 0
        
        
    def add_contact(self, name):
        c = Contact.Contact(name)
        self.contact_list.append(c)
        self.contact_total += 1
        
    def show_all_contacts(self):
        result = []
        if (self.contact_total):
            for contact in self.contact_list:
                result.append(contact.get_contact())
        else:
            result.append("No contacts")
        return result            
        
    def search_contact(self, name):
        result = []
        if (self.contact_total):
            found = {}
            for contact in self.contact_list:
                '''
                Search ranking:
                1) complete exact match - assuming full name search
                2) first name exact match
                3) last name exact match
                4) first name starts with
                5) last name starts with
                
                Took care of case here, trivial
                '''
                if ( contact.get_contact().lower() == name.lower() ):
                    found[contact.get_contact()] = 1
                elif ( contact.get_first().lower() == name.lower() ):
                    found[contact.get_contact()] = 2
                elif( contact.get_last().lower() == name.lower() ):
                    found[contact.get_contact()] = 3
                elif ( contact.get_first().lower().startswith(name.lower()) ):
                    found[contact.get_contact()] = 4
                elif ( contact.get_last().lower().startswith(name.lower()) ):
                    found[contact.get_contact()] = 5
                    
            result = sorted(found, key=found.get)
        else:
            result.append("No contacts")
        return result
    
    
    
    
    
    