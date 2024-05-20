#Wordle Program

secret_word = 'dog'
attempts = 0

hint_list = []
word_length = len(secret_word)

length = 0

while length < word_length:
    hint_list.append('_ ')
    length += 1

hint_str  = ''.join(str(x) for x in hint_list)

while (True):
    try:
         print('Welcome to the word guessing game\n')

         print(f'Your hint is: {hint_str}')
         guess = input('What is your guess? ')
         attempts += 1

         if len(guess) != word_length:
             raise ValueError

         if guess == secret_word:
             print(f'\nCongrats! You guess the word {secret_word} correctly in {attempts} attempts')
             break
         else:  
              for i,(letter, word ) in enumerate(zip(secret_word, guess)):
                if word in secret_word and word in letter:
                 hint_list[i] =  ' ' + word.capitalize()
          
                elif word in secret_word:
                     hint_list[i] =  ' ' + word.lower()
                else:
                    hint_list[i] = ' _'
         hint_str  = ''.join(str(x) for x in hint_list)
         print(hint_str)
    except ValueError:
        print('\nERROR')
        print(f'\nPlease input {int(word_length)} characters\n')

