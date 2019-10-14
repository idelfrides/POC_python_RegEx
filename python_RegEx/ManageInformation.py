""" Manage informations to user module """


class ManageInformation(object):
    """ Manage informations to user """

    def __init__(self):
        """ Thunder init do nothing """
        pass


    def show_results(self, result, the_method):
        """ Show all return of called method 
            
            :param self: autoreference parameter
            :type self: python reserved word
            :param result: the result returned by a method 
            :type result: list or object
            :param the_method: Name of the method called
            :type the_method: str
            :returns: None
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
      
        