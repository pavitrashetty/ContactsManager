'''
Created on 12-Jun-2016

@author: pavitra-ubuntu

'''

class Contact:
    '''
    Class that defines a contact and gives methods for handling a Contact object
    A Contact object could have many fields for detailing the contact
    Currently, a Contact is first name [+ ' ' + last name]
    
    Having a separate contact object helps when there are lot of contacts;
    they can be dumped to a file or DB and retrieved as needed
    '''

    def __init__ (self, name):
        # Creates a contact object, uses only a name, could have many more details
        words = name.strip().split(" ", 1)
        if (words[0] == ''):
            raise ValueError("No name given")
            # Assumption 1: A contact should have some 'name'
        self._firstname = words[0]
        if (len(words) > 1):
            self._lastname = words[1]
            
            
    def __lt__(self, other):
        # In case a contact object has to be compared
        return self.get_contact() < other.get_contact()
    
        
    def get_contact(self):
        if (hasattr(self, "_lastname")):
            return self._firstname + " " + self._lastname
        else:
            return self._firstname
        
        
    def get_first(self):
            return self._firstname
        
        
    def get_last(self):
        if (hasattr(self, '_lastname')):
            return self._lastname
        else:
            return None
        
        