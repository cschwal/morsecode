# CJS Morse Code Translator
# currently has A-Z and space
list_morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."," "]
list_lett=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]

"""
# Display Morse Code Dictionary
for n in range(len(list_lett)):
    print(list_lett[n])
    print(list_morse[n])
"""

def texttomorse():
    # will have to be converted from raw_input() to input() for python3
    userin = raw_input("Enter message: ").upper()
    outp = []
    
    for i in range(len(userin)):
        for j in range(len(list_lett)):
            if userin[i] == list_lett[j]:
                outp.append(list_morse[j])

    # will have to change print statement to use end=' ' for python3    
    for k in range(len(outp)):
        print outp[k],

def morsetotext():
    userin = raw_input("Enter code: ").split()
    outp = []

    for i in range(len(userin)):
        for j in range(len(list_morse)):
            if userin[i] == list_morse[j]:
                outp.append(list_lett[j])

    for k in range(len(outp)):
        print outp[k],

def menu():
    print("==========================")
    print("Morse Code Translater v0.3")
    print("A = text to Morse code")
    print("B = Morse code to text")
    print("X = exit")
    print("==========================")
    mainmenu = raw_input("Select an option: ").upper()

    if mainmenu == "A":
        texttomorse()
    elif mainmenu == "B":
        morsetotext()
    elif mainmenu == "X":
        exit()
    else:
        print("what?!")
        return

menu()
    
