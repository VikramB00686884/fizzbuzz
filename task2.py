import string

def find_unique_words(words_20k, book):
    try:
        # Open the first file and read its contents
        with open(words_20k, 'r') as f1:
            text1 = f1.read()
            words1 = text1.split()
            unique_words1 = set(words1)

        # Open the second file and read its contents
        with open(book, 'r') as f2:
            text2 = f2.read()
            words2 = text2.split()
            unique_words2 = set(words2)

        # Finding the unique words from the first file in the second file
        unique_words_in_file2 = list(unique_words1.intersection(unique_words2))

        return tuple(unique_words_in_file2)
    except Exception as e:
        print("An error occurred while reading the files: ", e)

# Function name: count_the_article - Returns: An Integer that counts the total number of words that are in the list. 
# => ["a", "the", "at", "run", "to","and","are","or","for","an","this"]

def count_the_article():
    given_list = ["a", "the", "at", "run", "to","and","are","or","for","an","this"]
    return len(given_list)


# Function name: sorted_words - Returns: A list containing the words in the book in descending order based on character count.
def sorted_words(book):
        
    with open(book, 'r') as f1:
        text1=f1.readlines()
        print(f"The total number of the words in {book} : ",sorted(text1, key=len, reverse=True))
        print("\n")



# 4) Function name: character_word_count - Returns: A Dicionary containing words in the book 
# as key and the character count as the values.

def character_word_count(book):
    word_counts = {}
    with open(book, 'r') as f1:
        words_list=f1.readlines()

    for word in words_list:
        word_counts[word] = len(word)
    return word_counts

# 5) Function name: starts_with_vow - Returns: An Integer 
# In each book count the total number of words that start with this following collection tuple => ("a", "e", "i", "o", "u").
def starts_with_vow(book):
    vowels = ("a", "e", "i", "o", "u")
    count = 0
    with open(book, "r") as f:
        for line in f:
            for word in line.translate(str.maketrans('', '', string.punctuation)).split():
                if word[0].lower() in vowels:
                    count += 1
    return count

# 6) Function name: rare_words - Returns: A list of words in Books that are non present in 20k.txt [Do it for each book]

def rare_words(book):
    common_words = set()
    rare_words = set()
    with open("20k.txt", "r") as f:
        for line in f:
            common_words.add(line.strip())
    with open(book, "r") as f:
        for line in f:
            for word in line.translate(str.maketrans('', '', string.punctuation)).split():
                if word.lower() not in common_words:
                    rare_words.add(word)
    return list(rare_words)

# 7) Function name: unused_word - Returns: A list of words in the 20k.txt that are non present in any Books and the count.

def unused_word(book):
    common_words = set()
    unused_words = set()
    with open("20k.txt", "r") as f:
        for line in f:
            common_words.add(line.strip())
    with open(book, "r") as f:
        for line in f:
            for word in line.translate(str.maketrans('', '', string.punctuation)).split():
                if word.lower() in common_words:
                    common_words.remove(word.lower())
    return list(common_words), len(common_words)

def Menu():
    file1="Book1.txt"
    file2="Book2.txt"
    file3="Book3.txt"
    words_20k="20k.txt"
    files = [file1,file2,file3]

    # Looping through and fetching EACH Book 
    for file in files:
        find_unique_words(file)
        count_the_article()
        sorted_words(file)
        character_word_count(file)
        starts_with_vow(file)
        rare_words(file)
        unused_word(file)

