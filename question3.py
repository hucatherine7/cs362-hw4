#Question 3: Full name

def generateFullName(first, last):

    #Check if input is a string or not
    if not isinstance(first, str) or not isinstance(last, str) or not first.isalnum() or not last.isalnum():
        print("\nError, you have not entered a string as input")
        return "Bad input"

    #Check if the first or last name doesn't exist
    if not first or not last:
        print("Please include both first and last name")
        
    fullName = first + " " + last
    return fullName


#generateFullName("John", "Test")
