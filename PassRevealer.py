from tkinter import *

import subprocess





class Reveal():

	
	def getpass(self):
		# Getting the meta-data
	    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

	    # Decoding the meta-data
	    data = meta_data.decode('utf-8', errors="backslashreplace")

	    # Split the  meta-data into separate lines
	    data = data.split('\n')

	    # Create a list/directory of the wireless networks
	    profiles = []

	    for i in data:
	        # find "All User Profile"
	        if "All User Profile" in i :

	            # if found, split the item
	            i = i.split(":")

	            i = i[1]

	            i = i[1:-1]
	            # Appending the wifi name in the list
	            profiles.append(i)

	    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
	    print("----------------------------------------------")

	    for i in profiles:
	        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile' ,i,'key=clear'])

	        results = results.decode('utf-8', errors="backslashreplace")
	        results = results.split('\n')

	        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

	        try:
	            print("{:<30}| {:<}".format(i, results[0]))

	        # else it will print blank in front of pass word
	        except IndexError:
	            print("{:<30}| {:<}".format(i, ""))

	        # called when this process get failed
	        except subprocess.CalledProcessError:
	            print("Encoding Error Occured")

	def __init__(self,rev):

			self.lbl1 = Label(rev, text=" ")	
			self.lbl1.place(x=0, y=40)
			# config getpass as text

			

			self.btn1 = Button(rev,text="Get Passwords",command=self.getpass)
			
			self.btn1.place(x=400, y=40)



























# Create window
window=Tk()
 #Add Icon on the application window
# icon = PhotoImage(file = 'C:/USERS/USER/Documents/D/PYTHON/Projects/SMS/static/front-end/images/icon.png')
# window.iconphoto(False,icon)
# Window Title
window.title("Pass Revealer")
mywin=Reveal(window)

lbl=Label(window, text="Pass-Revealer", fg='black', font=("Arial Black", 16))
lbl.place(x=0,y=0)
# Specifies the size of the Dat Entry Window
window.geometry("700x500+10+20")
# Executes window Tkinter code in an infinite loop to create the window
window.mainloop()