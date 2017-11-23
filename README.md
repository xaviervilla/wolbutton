# wolbutton
Wake remote computer with a single button click [Uses SSH and Raspberry Pi]

![Alt text](Preview.png?raw=true)

Difficulty: 
- If you already have a Raspberry Pi WOL server set up: Easy
- If you do not: Easy/Moderate

# Prerequisites
This tiny program utilizes Python and SSH to send a command to a Raspberry Pi or other remote server.

The command that wolbutton sends, runs a batch file that wakes the target PC.

For wolbutton to work, the Raspberry Pi Server must already be set up to send the 'Wake On LAN' (WOL) or 'Magic Packets'.

The PC must also already be configured to wake up when it recieves these packets.

There are many tutorials online on how to do both, but this tutorial is exactly what you need:
- http://www.instructables.com/id/Raspberry-Pi-As-Wake-on-LAN-Server/

# How to set up wolbutton
Download this repository, and extract 'wolbutton-master'.

Move the folder that contains 'powericon.ico', 'wol.py', and 'wol-hidden.vbs' to 
- C:\ProgramData\Microsoft\Windows\Start Menu\Programs

If done correctly, you should have 4 items like this:
- C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\powericon.ico
- C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\Wake PC.lnk
- C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\wol.py
- C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\wol-hidden.vbs

Now that you moved the file, it should appear in your start menu programs.

Hit 'Start', and scroll all the way down to 'W' for 'wolbutton-master'.

Click on the folder, and then right click on 'Wake PC', then click 'Pin to Start'.
- Optionally, if you want to add a keyboard shortcut to wake your computer, you can right click on 'Wake PC',
- then go to 'More', then 'Open File Location'. 
- Look for the 'Wake PC' shortcut in the file explorer, right click on it and hit 'Properties'.
- Under 'Shortcut Key', click the box, and then add your button combo that you want. Ex: "Ctrl + Shift + P".

Now we will add your server info to the python script that will wake your PC.

Navigate back into the 'wolbutton-master' file that we moved earlier.
- C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\

Inside this file, open wol.py in any text editor. 

Everything inside the quotes, '', must be replaced with your Raspberry Pi server info. 

Read the #comments in the python file for more help with this.

Now we are almost done. We just need to make sure that we have the following installed, and if not, quickly install them.
- Python
- Paramiko

Python is a lightweight programming language, and for your computer to understand and compute python code, you need to install it.

Paramiko is a small package that implements SSH in Python. Without Paramiko, you can't SSH your Pi in Python. 

To check if Python is installed, open CMD, and type 'python --version'. 
- if it is installed, it will say 'Python X.X.XX' Where the X's are the version number. Ex: Python 2.7.14
- If it is installed, then move on. 
- If Python is not recognized by CMD as a command, then install Python from here: https://www.python.org/downloads/release
- Installing Python is quick and easy.

By now, you should have Python installed. Lets now make sure you have Paramiko installed.
- In a CMD window, type 'pip install paramiko'
- This will install Paramiko if you do not already have it. This should be quick, as it is a small package.

# Done!
The button in your start menu should now wake your computer if everything was done correctly.

If you run into any problems that you cannot resolve on your own, please let me know.
















