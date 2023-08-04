""" The file responsible for running the `.amm` file """

import sys

known_keywords = [
    "whatif",
    "orelse",
    "log"
]

def get_code(file_path: str):
    with open(file_path, 'r') as program_file:
        return program_file.read()

def get_file(file_path: str):
    with open(file_path, 'r') as program_file:
        return program_file

def run(file, program):
    """Very important func"""
    keyword: str = ""
    pause_scan = False
    
    # Str scanning stuff
    scanning_str = False
    scanned_str: str = ""
    double_quotes_count: int = 0
    
    for char in program:
        
        if keyword in known_keywords:
            pause_scan = True
            match keyword:
                case "log": # Print function
                    if char == "\"":
                        double_quotes_count += 1
                        scanning_str = not scanning_str
                        continue
                    if scanning_str == True:
                        scanned_str += char
                    
                    if double_quotes_count == 2:
                        print(scanned_str)
                        
                        scanned_str = ""
                        scanning_str = False
                        double_quotes_count = 0
                        
                        pause_scan = False
                
                case "whatif":
                    pass
                case "orelse":
                    pass
                case _:
                    print(" [ERROR]")
        
        if pause_scan == False:
            keyword += char
        
        
        if char in [";", "\n"]:
            keyword = ""
            continue

# EXPLANATION:
#       > This `.py` file will execute the `.amm` file by scanning every keyword
#       and based on what it scanned it will do certain tasks
#       > This `.py` file will use a for loop to loop into EVERY CHARACTER in the `.amm` file


argc = len(sys.argv)
filename = sys.argv[1]
code = get_code(filename)
codefile = get_file(filename)

# print(f"\n - Filename : '{filename}'")
# print(f" - File's content:\n\n{code}\n")
# print(f" - Output: \n")
run(filename, code)