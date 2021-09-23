# self_learning-manipulating_string
Reference to Stanford University’s assignment CS106AP: Programming Methodologies in Python and CS106B: Programming Abstractions as practice, focusing topic: manipulating string
## Projects Source Codes:
* [01_complement_DNA](https://github.com/An022/self_learning-manipulating_string/blob/main/01_complement_DNA/complement_DNA.py)\
  This program uses string manipulation to tackle a real world problem - finding the complement strand of a DNA sequence.\
  The program asks uses for a DNA sequence as a python string that is case-insensitive and output the complement of it.\

  ```
  User can input a DNA strand, and this program can find the complement.
  
  pre-condition:
  Inform user enter a DNA strand.
  post-condition: 
  Show the complement of DNA to user.
  ```
* [02_DNA_similarity](https://github.com/An022/self_learning-manipulating_string/blob/main/02_DNA_similarity/DNA_similarity.py)\
  This program compares short dna sequence, s2, with subsequences of a long dna sequence, s1\
  the way of approaching this task is the same as what people are doing in the bio- industry.
  
  ```
  Use this program can help user find the homology in a DNA sequence.
  
  pre-condition: 
  Inform user to input "a DNA sequence to search" and "a DNA sequence to match".
  post-condition: 
  Show user the best match DNA sequence.
  ```
* [03_caesar_cryptography](https://github.com/An022/self_learning-manipulating_string/blob/main/03_caesar_cryptography/caesar.py)\
  The program demonstrates the idea of the caesar cipher.\
  Users will be asked to input a number to produce shifted alphabet as the cipher table.\
  After that, any strings typed in will be encrypted.\
  
  ```
  Use the concept of Caesar Cipher to cipher the secret message.
  
  Pre-condition: 
  Inform user entered the secret number and the ciphered string.
  Post-condition: 
  Give user the correct message from the ciphered string.
  ```
* [04_hangman](https://github.com/An022/self_learning-manipulating_string/blob/main/04_hangman/hangman.py)\
  This program plays a hangman game.\
  Users see a dashed word, trying to correctly figure the un-dashed word out by inputting one character each round.\
  If the user input is correct, show the updated word on the console.\
  Players have N_TURNS chances to try and win this game.\
  
  ```
  The program will play a hangman game with user.
  
  pre-condition:
  The program will pick up a word randomly as the right answer
  then hide the answer with and show the question.
  post-condition:
  Show user's guess is right or wrong every time until the user win or lose the game.
  
  One right guess:
  (1)Reveal the right character in the hiding string. (2)The life will not be reduced.
  One wrong guess:
  (1)Maintain the unknown character in hiding string. (2)The life will be reduced 1 time.
  
  User win:
  When life is bigger than 0 and all the character are answered correctly by user.
  Inform user that he/she win this game and show the correct answer.
  User lose:
  When life is  0 and all the character are not answered correctly by user.
  Inform user 'game over' and show the correct answer.
  ```
