""" Main method 

    This is a proof of concept made 
    to Regular Expressions in Python
    -------------------------------------
"""

from python_RegEx import reg_ex 


def main():
    """ Main method 

        This is a proof of concept made 
        to Regular Expressions in Python
    """

    reo = reg_ex.RegExModule()

    text = input('\n\n Enter a string:  ')

    reo.find_all("Eu", text)
    reo.search("[a-e]", text)
    reo.replace(r"\s", '7', text)   
    
    print('\n\n\n')


# Start the main method
main()
