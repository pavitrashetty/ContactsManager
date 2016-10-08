'''
Created on 18-Jun-2016

@author: pavitra-ubuntu

Hash map search implementation
Ranking done by sorting strings in the end, the only overhead

'''

import Contact

class ContactList(object):
    '''
    Class that maintains all contacts and provides methods to access them
    '''


    def __init__(self):
        self.contact_list = []
        self.contact_total = 0
        self.word_map = {}
        
        
    def add_name_to_map(self, name, index):
        # adding name to corresponding maps, index of name in contact_list saved in the map      
        if name is None:
            return
            # Because assumption 1        
        current_map = self.word_map                
        for alp in name:
            if (alp not in current_map):
                current_map[alp] = {}
            current_map = current_map[alp]
            
        if (None not in current_map):
            current_map[None] = []
        current_map[None].append(index)

        
    def add_contact(self, name):
        # adding Contact objects to the list and maps
        c = Contact.Contact(name)
        self.contact_list.append(c)
        self.add_name_to_map(c.get_first(), self.contact_total)
        self.add_name_to_map(c.get_last(), self.contact_total)
        self.contact_total += 1
        
        
    def show_all_contacts(self):
        # returns all Contacts, sorted for better display
        result = []
        if (self.contact_total):
            for contact in self.contact_list:
                result.append(contact.get_contact())
            result.sort()
        else:
            result.append("No contacts")
            
        ''' print ("For debugging purposes:")
        print (self.word_map) '''
        
        return result            
     
   
    def get_all_values(self, input_map, final_list):
        # returns all leaf arrays in input_map
        for v in input_map.values():
            if isinstance(v, dict):
                self.get_all_values(v, final_list)
            elif isinstance(v, list):
                final_list.extend(v)
        return final_list
   
     
    def find_in_map(self, search_term):
        # Method to traverse the mapped dictionary
        # Returns list of indices that completely match the search_term or have search_term as substring
        # Returns empty list if search_term is not found at all
        current_map = self.word_map            
        for alp in search_term:
            if (alp in current_map):
                current_map = current_map[alp]
            else:
                return []
            
        return self.get_all_values(current_map, [])
        
        
    def search_contact(self, search_term):
        # Method to search first and/or last name in contacts
        result = []
        if (self.contact_total):
            found_in_map = set(self.find_in_map(search_term))
            if len(found_in_map) == 0:
                result.append("Did not match any contact")
            else:
                for index in found_in_map:
                    result.append(self.contact_list[index].get_contact())
                result.sort()        
        else:
            result.append("No contacts available")
        return result
        
        
        
        