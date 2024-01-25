import os
import shutil
import time
import time
import re
import os

class TypewriterPrint:
    def __init__(self, text, delay=0.05):
        self.text = text
        self.delay = delay

    def print_text(self):
        for char in self.text:
            print(char, end='', flush=True)
            time.sleep(self.delay)
        print()

current_directory = os.getcwd()
directory_name = os.path.basename(current_directory)
path = os.getcwd()


class PasscodeChecker:
    def __init__(self):
        self.passcode = "p_a_s_s_w_o_r_d_!_@_#_@_!_"
        # Check if the file exists and read the value from it
        try:
            with open('first_time.txt', 'r') as file:
                self.first_time = file.read() == 'True'
        except FileNotFoundError:
            # If the file doesn't exist, create it and write 'True' to it
            with open('first_time.txt', 'w') as file:
                file.write('True')
            self.first_time = True

    def check_passcode(self):
        password = 'anotsosafepasswordorisit?'
        typewriter_print = TypewriterPrint('Press enter to end script or type ''passcode'' to enter a password')
        typewriter_print.print_text()
        
        user_input = input()
        if user_input == '':
            typewriter_print = TypewriterPrint('Script ended')
            typewriter_print.print_text()
        

        if password == self.passcode:
            print('Correct passcode')
            with open('first_time.txt', 'w') as file:
                file.write('True')
            self.first_time = True
            if self.first_time:
                password = input('Enter passcode: ')
                if password == self.passcode:
                     typewriter_print = TypewriterPrint('wow you got it right, I dont have a cookie to give you but you can have this message instead, also your conmputer is now corrupted, have fun!')
                     typewriter_print.print_text()
                     for i in range(3, 0, -1):
                         print(i)
                     # Update the value in the file
                     with open('first_time.txt', 'w') as file:
                         file.write('True')
                     self.first_time = True
                     #IF YOUR CHECKING THIS SCRIPT BEFORE RUNNING IT AT ALL CONGRATS! YOU ARE A SMART COOKIE!
                     typewriter_print = TypewriterPrint('Ahh just kidding, cant believe you sat through that countdown. ')
                     typewriter_print.print_text()
                else:
                    typewriter_print = TypewriterPrint('wrong your computer is now corrupted, have fun, and shutdown will comence in: ')
                    typewriter_print.print_text()
                    for i in range(3, 0, -1):
                        print(i)
                        time.sleep(1)
                    #IF YOUR CHECKING THIS SCRIPT BEFORE RUNNING IT AT ALL CONGRATS! YOU ARE A SMART COOKIE!
                    typewriter_print = TypewriterPrint('Ahh just kidding, seriously who downloads random files from the internet without some precaution, anyways, have a nice day!')
                    typewriter_print.print_text()
                    with open('first_time.txt', 'w') as file:
                        file.write('False')
                    self.first_time = False
                    self.check_passcode()
            else:
                password = input('Enter passcode: ')
                if password == self.passcode:
                    print('Correct passcode')
                else:
                    print('Incorrect passcode')
                    self.check_passcode()

directory_name = os.path.basename(os.getcwd())


if directory_name == "my_file_system":
    typewriter_print = TypewriterPrint("Hello Welcome to the Maze!")
    typewriter_print.print_text()
    checker = PasscodeChecker()
    checker.check_passcode()
elif directory_name == "GoThrougHere":
    typewriter_print = TypewriterPrint("Ready?")
    typewriter_print.print_text()
    checker = PasscodeChecker()
    checker.check_passcode()
elif directory_name == "maze_KO":
    typewriter_print = TypewriterPrint("Whats wrong!!")
    typewriter_print.print_text()
elif directory_name == "Door5":
    typewriter_print = TypewriterPrint("wow you made it here, congrats, you learned how to use a python script in a terminal")
    typewriter_print.print_text()
    typewriter_print = TypewriterPrint('Press any key to continue...')
    typewriter_print.print_text()
    input()
elif directory_name == "Door3":
    typewriter_print = TypewriterPrint("wow you made it here, congrats, you learned how to use a python script in a terminal")
    typewriter_print.print_text()
    typewriter_print = TypewriterPrint('Press any key to continue...')
    typewriter_print.print_text()
    input()
elif directory_name == "yes":
    typewriter_print = TypewriterPrint("File made...")
    typewriter_print.print_text()
    try:
        with open('Answer', 'w', encoding='utf-8') as file: 
            file.write(" Here is the second part: ꜵꝶﺺ , Now if you move this file to Door10, you will have the last key to enter.")       
    except Exception as e:
        # If the file doesn't exist...
        with open('Answer', 'w', encoding='utf-8') as file:
            file.write(" Here is the second part: ꜵꝶﺺ , Now if you move this file to Door10, you will have the last key to enter.")


current_directory = os.getcwd()
script_path = os.path.join(current_directory, "ezskript.py")

for directory in os.listdir(current_directory):
    if os.path.isdir(directory):
        destination = os.path.join(current_directory, directory, "ezskript.py")
        shutil.copy(script_path, destination)

if directory_name == "Door10":
    
    try:
        with open('answer', 'w', encoding='utf-8') as file: 
            file.write("Sorry last thing. Delete Door10")
    except Exception as e:
        # If the file doesn't exist...
        with open('answer', 'w', encoding='utf-8') as file:
            file.write("Sorry last thing. Delete Door10")
current_directory = os.getcwd()
script_path = os.path.join(current_directory, "ezskript.py")

for directory in os.listdir(current_directory):
    if os.path.isdir(directory):
        destination = os.path.join(current_directory, directory, "ezskript.py")
        shutil.copy(script_path, destination)

current_directory = os.getcwd()
door10_path = os.path.join(current_directory, "Door10")

if not os.path.exists(door10_path):
    door11_path = os.path.join(current_directory, "Door11")
    os.mkdir(door11_path)
    
current_directory = os.getcwd()
door11_path = os.path.join(current_directory, "Door11")

if os.path.exists(door11_path):
    file_path = os.path.join(door11_path, "Actualanswer.txt")
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("hopefully you have your other keys ὢ")


    
current_directory = os.getcwd()
script_path = os.path.join(current_directory, "ezskript.py")

for directory in os.listdir(current_directory):
    if os.path.isdir(directory):
        destination = os.path.join(current_directory, directory, "ezskript.py")
        shutil.copy(script_path, destination)




