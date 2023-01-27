# Inwk6312 - Winter 2023

# Programming Task 

Welcome to your first openbook quiz

  - You have to clone this repo to your account, you should be seeing this on your account.
  - Use your dev environment to do these task and record them with your comments (Audio/Video and screen cast)
  - Use the terminal to do most of the actions, explain your environment (The Linux variant, the kernel, the shell, your editor, IDE and anyother relavant information)
  - Attempt to solve this on your own
  - Provide comments as you try to solve this task

 
# Task 0 - Fizz Buzz

### Objectives
- Create your own empty repository in your github account called fizzbuzz (Public)
- Create a local repository on your computer called fizzbuzz-yourname and set the github repository as remote 
- Write a python program to solve the problem given below
- Add, Commit and Push the code
- In your openbook final repository(the one you cloned from github-classroom) create a file called task0.link and paste the https link to clone your fizzbuzz github repo.  
- This is just to check if you can create your own repo and link it. PLEASE READ THIS QUESTION CAREFULLY!

### Problem 
 "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
 
 ### Note:
 You only need to provide a file with a link to your repository.  YOU SHOULD NOT WRITE THE PROGRAM IN THIS REPO.


# Task 1 - l33t copy 

### Objectives

Write the solution in task1.py
You are to create a program that does text file copying. But with a twist!

    - You get a target file name and (optionally a target folder) 
    - Copy specific pages of text to a new file (Assume 25 lines to be a page of a text)
    - Copy with l33t code on (Write a function for this!)
    - Create a menu to provide these options and get all the input from the users
    
Also, when done copying display a report indicating success and the count of pages, line and words copied and the count of alphabetic characters and also a count of numeric characters written. 
Please ensure that the code handles errors in user input or system faluts. [Handle exceptions]

### l33t code rules

    - Replace o or O with 0(number) and a or A with 4
    - Replace e or E with 3 and i or I with 1
    - Words ending with (suffix) "-er" ends with "-xor" or "-zor" [ hacker -> h4x0r) 

# Task 2 - Book play

### Objectives

The books are Book1.txt, Book2.txt, Book3.txt they are found in your repo. You also have, a file called 20k.txt that contains a list of common english words. Using this you can find the characters and nouns in the books. 
Open the book in python and write the following functions to perform the following operations on each of the book. Pass the book as a argument to the functions and return the requested data structure / type.

1. Function name: unique_words - Returns: A list containing only one copy of the words. (for example, if the word "it" appears 50 times in the book, there should be only one "it" in the tuple)

2. Function name: count_the_article - Returns: An Integer that counts the total number of words that are in the list. => ["a", "the", "at", "run", "to","and","are","or","for","an","this"]

3. Function name: sorted_words - Returns: A list containing the words in the book in descending order based on character count.

4. Function name: character_word_count - Returns: A Dicionary containing words in the book as key and the character count as the values. 

5. Function name: starts_with_vow - Returns: An Integer In each book count the total number of words that start with this following collection tuple =>  ("a", "e", "i", "o", "u").

6. Function name: rare_words - Returns: A list of words in Books that are non present in 20k.txt [Do it for each book]

7. Function name: unused_word - Returns: A list of words in the 20k.txt that are non present in any Books and the count. 

