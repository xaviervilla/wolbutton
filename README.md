# wolbutton
Wake remote computer with a single button click [Uses SSH and Raspberry Pi]

# Prerequisites
This tiny program utilizes Python and SSH to send a command to a Raspberry Pi or other remote server.
The command that wolbutton sends, runs a batch file that wakes the target PC.
For wolbutton to work, the Raspberry Pi Server must already be set up to send the 'Wake On LAN' (WOL) or 'Magic Packets'.
The PC must also already be configured to wake up when it recieves these packets.
There are many tutorials online on how to do both, but this tutorial is exactly what you need:
http://www.instructables.com/id/Raspberry-Pi-As-Wake-on-LAN-Server/

# How to set up wolbutton
Download this repository, and extract 'wolbutton-master'.
Move the folder that contains 'powericon.ico', 'wol.py', and 'wol-hidden.vbs' to 
C:\ProgramData\Microsoft\Windows\Start Menu\Programs
If done correctly, you should have 4 items like this:
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\powericon.ico
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\Wake PC.lnk
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\wol.py
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\wolbutton-master\wol-hidden.vbs
Now that you moved the file, it should appear in your start menu programs.
Hit 'Start', and scroll all the way down to 'W' for 'wolbutton-master'.
Click on the folder, and then right click on 'Wake PC', then click 'Pin to Start'.
Optionally, if you want to add a keyboard shortcut to wake your computer, you can right click on 'Wake PC',
then go to 'More', then 'Open File Location'. 
Look for the 'Wake PC' shortcut in the file explorer, right click on it and hit 'Properties'.
Under 'Shortcut Key', click the box, and then add your button combo that you want. Ex: "Ctrl + Shift + P".

