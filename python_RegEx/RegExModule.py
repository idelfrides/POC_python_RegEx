
import re


class RegExModule(object):
    """ Regular expression class """

    def __init__(self):
        """ Thunder init do nothing """
        pass


    def search(self, search_string, text):
        """ Search function 
            -------------------------
            Returns a Match object if there is 
            a match anywhere in the string
        """

        result = re.search(search_string , text)
        self.show_results(result, 'search')

              
    def find_all(self, search_string, text):
        """ Find all function 
            -------------------------
         	Returns a list containing all matches
        """

        result = re.findall(search_string, text)
        self.show_results(result, 'findall')

    
    def replace(self, car2remove, car2add, text):
        """ Sub function 
            -------------------------
         	The sub() function replaces the matches 
            with the text of your choice:
        """

        result = re.sub(car2remove, car2add, text, 3)
        self.show_results(result, 'sub')



    def show_results(self, result, the_method):
        """ Show all return of called method 
            
            :type self: autoreference parameter
            :type result: the result returned by a method 
            :type the_method: the method called 
            :rtype: None
        """

        print('\n\n')
        print('-' * 80)

        if the_method == 'findall':
            print('\n\n\t RESPONSE OF  {}  METHOD \n\n'.format(the_method))

            print('\t RESULT LIST --> {} '.format(result))         
            print('\n')
            print('-' * 80)

        if the_method == 'search':
            print('\n\n\t RESPONSE OF  {}  METHOD \n\n'.format(the_method))

            print('\t STRING --> {} '.format(result.string))
            print('\t SPAN --> {} '.format(result.span()))
            print('\t WORD --> {} '.format(result.group()))            
            print('\n')
            print('-' * 80)
        
        if the_method == 'sub':
            print('\n\n\t  RESPONSE OF  {}  METHOD \n\n'.format(the_method))

            print('\t STRING --> {} '.format(result))      
            print('\n')
            print('-' * 80)            
        