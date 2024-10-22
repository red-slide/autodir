import sys

async def get_range():
    try:
        # Prompts the user for the minimum and maximum lengths
        min_length = int(input("\033[36m[+]\033[0m Enter the minimum length: "))
        max_length = int(input("\033[36m[+]\033[0m Enter the maximum length: "))

        # Checks if the lengths are positive and if the maximum is not less than the minimum
        if min_length <= 0 or max_length <= 0:
            raise ValueError("Values must be greater than zero.")
            sys.exit()
        if min_length > max_length:
            raise ValueError("The maximum length cannot be less than the minimum length.")
            sys.exit()
            
        # If everything is correct, return the list with the values
        return [min_length, max_length]
        
    except ValueError as e:
        # Displays an error message and exits the program
        print("\n\033[41mPlease enter valid values.\033[0m")
        sys.exit()
