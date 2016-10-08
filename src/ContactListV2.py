'''
Created on 19-Jun-2016

@author: pavitra-ubuntu

Hash map search implementation
Ranking done by sorting during initial insertion and merging results

'''

import bisect
import Contact

class ContactList(object):
    '''
    Class that maintains all contacts and provides methods to access them
    '''


    def __init__(self):
        self.contact_list = []  # for reference to entire contact object when the object contains more than a name
        self.contact_total = 0
        self.word_map = {}
        
        
    def add_name_to_map(self, name, contact):
        # adding the name to corresponding maps, leaf maps contain list of sorted contact names   
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
        # Add contact in sorted order
        full_name = contact.get_contact()
        current_map[None].insert(bisect.bisect_right(current_map[None], full_name), full_name)

        
    def add_contact(self, name):
        # adding Contact objects to the list and maps
        c = Contact.Contact(name)
        self.contact_list.append(c)
        self.add_name_to_map(c.get_first(), c)
        self.add_name_to_map(c.get_last(), c)
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
            
        '''print ("For debugging purposes:")
        print (self.word_map)'''
        
        return result            
     
   
    def get_all_values(self, input_map, final_list):
        # returns all leaf arrays in input_map, takes care of sorting while adding 2 lists
        for v in input_map.values():
            if isinstance(v, dict):
                self.get_all_values(v, final_list)
            elif isinstance(v, list):
                if (len(final_list) == 0):
                    final_list.extend(v)
                else:
                    index_to_insert_at = bisect.bisect_right(final_list, v[0])
                    final_list[index_to_insert_at:index_to_insert_at] = v
        return final_list
   
     
    def find_in_map(self, search_term):
        # Method to traverse the mapped dictionary
        # Returns list of contacts that completely match the search_term or have search_term as substring
        # Returns empty list if search_term is not found at all
        current_map = self.word_map            
        for alp in search_term:
            if (alp in current_map):
                current_map = current_map[alp]
            else:
                return []
            
        return self.get_all_values(current_map, [])
    
    
    
    def remove_duplicates(self, input_list):
        found = set()
        add_to_found = found.add
        return [a for a in input_list if not (a in found or add_to_found(a))]
    
        
        
    def search_contact(self, search_term):
        # Method to search first and/or last name in contacts
        result = []
        if (self.contact_total):
            result = self.remove_duplicates(self.find_in_map(search_term))
            if len(result) == 0:
                result.append("Did not match any contact")
        else:
            result.append("No contacts available")
        return result
        
        
        
        