
import re
from python_RegEx import info


class RegExModule(object):
    """ Regular expression class """

    def __init__(self):
        """ Thunder init do nothing """
        self.info_obj = info.ManageInformation()



    def search(self, search_string, text):
        """ Search function 
            -------------------------
            Returns a Match object if there is 
            a match anywhere in the string
        """

        result = re.search(search_string , text)
        self.info_obj.show_results(result, 'search')

              
    def find_all(self, search_string, text):
        """ Find all function 
            -------------------------
         	Returns a list containing all matches
        """

        result = re.findall(search_string, text)
        self.info_obj.show_results(result, 'findall')

    
    def replace(self, car2remove, car2add, text):
        """ Sub function 
            -------------------------
         	The sub() function replaces the matches 
            with the text of your choice:
        """

        result = re.sub(car2remove, car2add, text, 3)
        self.info_obj.show_results(result, 'sub')

