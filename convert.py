from typing import Optional

# Converts a string to a float, returns None if conversion fails
# INPUT: str to be converted
# OUTPUT: str in type float, otherwise None
def str_to_float(string : str) -> Optional[float]:
    try:
        return float(string)
    except ValueError:
        print("An error occurred.")
        return None
