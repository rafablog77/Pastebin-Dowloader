import tkinter as tk
from tkinter import filedialog

import requests

import gettext
import os

# Set up translation
locales_dir = os.path.join(os.path.dirname(__file__), 'locales')
lang = gettext.translation('tkinter', localedir=locales_dir, languages=['en'], fallback=True)
lang.install()
_ = lang.gettext  # Alias for convenience

root = tk.Tk()
key = "?"

# This is the section of code which creates the main window
root.geometry('455x219')
root.configure(background='#F5F5F5')
root.title(_('Pastebin Downloader'))

# this is a function to get the user input from the text input box
def getInputBoxValue():
  userInput = pasteKeyInput.get()
  return userInput

# this is the function called when the button is clicked
def down():
  global key
  key = getInputBoxValue()
  save_file()

# This is a function which creates a file download prompt
def save_file():
    global key
    types = [(_("Text files"), "*.txt"),
             (_("All files"), "*.*")]
    file = filedialog.asksaveasfile(title = _("Save File"),
                                    initialdir = ".", 
                                    defaultextension=".txt",
                                    filetypes=types)
    if file:
        file.write(requests.get(f"https://pastebin.com/raw/{key}").text)
        file.close()

# This is the section of code which creates a label
label1 = tk.Label(root, text=_('Paste Key:'), bg='#F5F5F5', font=('arial', 12, 'normal'))
label1.place(x=165, y=11)

# This is the section of code which creates a text input box
pasteKeyInput=tk.Entry(root)
pasteKeyInput.place(x=134, y=45)

# This is the section of code which creates a button
c = tk.Button(root,text=_('download'),bg='#F5F5F5',font=('arial',12,'normal'),command=down)
c.place(x=157, y=96)

root.mainloop()
