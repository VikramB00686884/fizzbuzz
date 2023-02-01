import random

# This function will help in coverting the text file to requirements 

# l33t code rules

# - Replace o or O with 0(number) and a or A with 4
# - Replace e or E with 3 and i or I with 1
# - Words ending with (suffix) "-er" ends with "-xor" or "-zor" [ hacker -> h4x0r) 

def l33t_code_rule(s):
    s = s.replace("o", "0").replace("O", "0")
    s = s.replace("a", "4").replace("A", "4")
    s = s.replace("e", "3").replace("E", "3")
    s = s.replace("i", "1").replace("I", "1")
    if s.endswith("er"):
        s = s[:-2] + random.choice(["xor", "zor"])
    return s

# This function will help to copy target to new target file 
def copy_files_to_new(target,new_target):
    # open both files
    try:
        with open(target,'r') as firstfile, open(new_target,'w') as secondfile:
            
            # read content from first file
            for line in firstfile:
                line1=l33t_code_rule(line)
                secondfile.write(line1)

    except Exception as e:
        print("An error occurred while copying the file: ", e)


# This function will help to get the report based on requirements        
def get_report(target_destination):

        with open(target_destination, 'r') as f:
            text = f.read()
            # Counting the number of lines, pages and words
            lines = len(text.split("\n"))
            pages = len(text.split("\f"))
            words = len(text.split())
            # Counting the number of alphabetic characters and numeric characters
            alpha_chars = sum(c.isalpha() for c in text)
            num_chars = sum(c.isdigit() for c in text)
        
        print("File copied successfully.")
        print(f"Number of lines in the copied file: {lines}")
        print(f"Number of pages in the copied file: {pages}")
        print(f"Number of words in the copied file: {words}")
        print(f"Number of alphabetic characters in the copied file: {alpha_chars}")
        print(f"Number of numeric characters in the copied file: {num_chars}")

# This is the main function  
def Menu():
    target="original.txt"
    target_destination="copy_original.txt"
    copy_files_to_new(target,target_destination)
    get_report(target_destination)

# Calling main menu 
Menu()
