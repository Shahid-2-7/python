def sentence_logic():

    vowelcount = 0
    numbercount = 0


    sentence = input("Enter sentence here : ")

    print("Characters count : ", len(sentence))

    print("Split parts : ",sentence.split())

    print("Word Count : ", len(sentence.split()))

    print("Lower case : ",sentence.lower())

    print("Upper case : ",sentence.upper())

    print("Spaces in sentence : ", sentence.count(" "))

    for ch in sentence:

        if ch.lower() in "aeiou":
            vowelcount += 1
        
        if ch in "1234567890":
            numbercount += 1

    print("Vowels found in sentence : ", vowelcount)

    print("Numbers found in sentence : ", numbercount)
    return sentence

def findWords(sentence):
    print(sentence)
    wordfind = input("Enter word to search : ") #1 - all three

    if wordfind in sentence.split():
        print("Word found")

    else:
        print("Word not found!")

def findCharacters(sentence):

    characterfind = input("Type a single character to count : ") #2

    charactercount = 0

    for ch in sentence:
        
        if ch == characterfind:
            charactercount += 1

    print(characterfind, "Occured", charactercount, "times.")

userSentence = sentence_logic()

while True:
    userChoice = int(input("Enter choice, 1 - New sentence | 2 - Find a word in the sentence | 3 - Count a specific character in the sentence | 4 - End program : "))
    match userChoice:
        case 1:
            userSentence = sentence_logic()
        case 2:
            findWords(userSentence)
        case 3:
            findCharacters(userSentence)
        case 4:
            break
        case _:
            print("Invalid Input. Try again\n")

 
    

