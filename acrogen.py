'''Acronym Generator in Python'''

userInput = input('Enter a Phrase You Would Like to Convert into an Acronym: ')

exclusions = userInput.replace('and', '')

reformatedUserInput = exclusions.split(' ')

acronym = ''
for word in reformatedUserInput:
    if(word != ''):
        acronym += word[0]

print(acronym)
