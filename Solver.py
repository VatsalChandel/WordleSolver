# Always a five letter word
# Words can be green, yellow, or black 
# Only have six tries 


attempt_number = 0
words = []

with open ("AllWords.txt") as f:
    for line in f:
        words.append(line.strip())

print("Words are loaded and ready")
    
while (attempt_number <= 6):
    print()
    user_guess = input("\nword: ").lower()
    print()
    print("g for green, y for yellow, and b for grey")
    from_user = input("\nWhat was the outcome: ").lower()
    if from_user == "ggggg":
        print("Great guess, tries: ", attempt_number+1)
        break
    
    temp_tuple = tuple(words)
    for word in temp_tuple:
        for i in range(5):
            
            if from_user[i] == 'b' and user_guess[i] in word:
                words.remove(word)
                break
            elif from_user[i] == 'g' and user_guess[i] != word[i]:
                words.remove(word)
                break
            elif from_user[i] == 'y' and user_guess[i] not in word:
                words.remove(word)
                break
            elif from_user[i] == 'y' and user_guess[i] == word[i]:
                words.remove(word)
                break
            
    counter = 0
    for word in words:
        print(word, end=", ")
        counter += 1
        if counter == 8:
            print("")
            counter = 0
