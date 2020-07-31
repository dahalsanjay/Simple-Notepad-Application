from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


class Notepad_GUI:
    current_open_file = "no_file"

    def _newFile(self):
        self.text_area.delete(1.0,END)
        self.current_open_file = "no_file"
    def _openFile(self):
        open_returns = filedialog.askopenfile(initialdir = "/", title = "Select File to Open", filetypes = (("text files","*.txt"),("all files","*.*")) )
        if open_returns != None:
            self.text_area.delete(1.0, END)
            for line in open_returns:
                self.text_area.insert(END, line)
            self.current_open_file = open_returns.name
            open_returns.close()

    def _saveasFile(self):
        saveas = filedialog.asksaveasfile(mode = "w", defaultextension = ".txt")
        if saveas is None:
            return
        text2save = self.text_area.get(1.0,END)
        self.current_open_file = saveas.name
        saveas.write(text2save)

        saveas.close()
    
    def _saveFile(self):
        if self.current_open_file == "no_file":
            self._saveasFile()
        else:
            save = open(self.current_open_file,"w+")
            save.write(self.text_area.get(1.0,END))
            save.close()
    def _cutFile(self):
        self._copyFile()
        self.text_area.delete("sel.first","sel.last")
    def _copyFile(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())
    def _pasteFile(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())
    def _commandFile(self):
        messagebox.showinfo("Notepad","No short commands can't work in this Notepad right now. We are working on it.\n Please stay tuned untill the newer version release")
    def _helpFile(self):
        messagebox.showinfo("About Notepad","This desktop version of Notepad is made by Sanjay Dahal.\n To know more about him please go to .\n www.facebook.com/dahalsanjay")

    

        

    def __init__(self,master):
       
        self.master = master
        master.title = "Notepad"
        self.text_area = Text(self.master, undo = True)
        self.text_area.focus()
        self.text_area.pack(fill = BOTH, expand = 1)

        # For Menu
        self.main_menu = Menu()
        self.master.config(menu = self.main_menu)
        self.file_menu = Menu(self.main_menu, tearoff = 0)
        self.main_menu.add_cascade(label = "File", menu = self.file_menu)
        self.edit_menu = Menu(self.main_menu, tearoff = 0)
        self.main_menu.add_cascade(label = "Edit", menu = self.edit_menu)
        self.command_menu = Menu(self.main_menu, tearoff = 0)
        self.main_menu.add_cascade(label = "Command", menu = self.command_menu)
        self.help_menu = Menu(self.main_menu, tearoff = 0)
        self.main_menu.add_cascade(label = "Help", menu = self.help_menu)

        self.file_menu.add_command(label = "New", command =  self._newFile)
        self.file_menu.add_command(label = "Open", command = self._openFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Save", command = self._saveFile)
        self.file_menu.add_command(label = "Save as", command = self._saveasFile)
        self.file_menu.add_separator()
        self.file_menu.add_command(label = "Exit", command = self.master.quit)

        self.edit_menu.add_command(label = "Undo", command = self.text_area.edit_undo)
        self.edit_menu.add_command(label = "Redo", command = self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label = "Cut", command = self._cutFile)
        self.edit_menu.add_command(label = "Copy", command = self._copyFile)
        self.edit_menu.add_command(label = "Paste", command = self._pasteFile)

        self.command_menu.add_command(label = "About Commands", command = self._commandFile)

        self.help_menu.add_command(label = "Help", command = self._helpFile)
        
root = Tk()
root.iconbitmap("notepad.ico")
root.title("Untitled - Notepad")
ng = Notepad_GUI(root)
root.mainloop()
