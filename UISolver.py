from tkinter import *
from tkinter import messagebox




attempt_number = 0
words = []

with open ("AllWords.txt") as f:
    for line in f:
        words.append(line.strip())

print("Words are loaded and ready")


def solver():
    while (attempt_number <= 6):
        print()
        user_guess = e1.get()
        print()
        print("g for green, y for yellow, and b for grey")
        from_user = e2.get()
        
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





root = Tk()
root.title("Wordle Solver")
root.geometry("300x200")

global e1
global e2

Label(root,text="Word: ").place(x=10, y=10)
Label(root,text="Outcome: ").place(x=10, y=40)

e1 = Entry(root)
e1.place(x=140, y=10)

e2 = Entry(root)
e2.place(x=140, y=40)

Button(root, text="Submit!", command=solver, height= 3, width=13).place(x=10, y=100) 


root.mainloop()
