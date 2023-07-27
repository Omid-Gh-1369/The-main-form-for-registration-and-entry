from tkinter import *

N_P=Tk()
N_P.title("Notepad_by_Omid-Gh")
N_P.geometry("800x600")
N_P.resizable(width=False, height=True)
menubar=Menu(N_P)
    
file=Menu(menubar,tearoff=0,background="white",bd=-15)  
file.add_command(label="New tab                    Ctrl+N") 
file.add_command(label="New window            Ctrl+Shift+N")  
file.add_command(label="Open                         Ctrl+O")  
file.add_command(label="Save                           Ctrl+S")  
file.add_command(label="Save as...                   Ctrl+Shift+S") 
file.add_command(label="Save all                      Ctrl+Alt+S")
file.add_separator()
file.add_command(label="Page setup")  
file.add_command(label="Print                           Ctrl+P")
file.add_separator()
file.add_command(label="Close tab                   Ctrl+W") 
file.add_command(label="Close window           Ctrl+Shift+W") 
file.add_command(label="Exit")
menubar.add_cascade(label="File",menu=file)

edit=Menu(menubar,tearoff=0,background="white",bd=-15)
edit.add_command(label="Undo                   Ctrl+Z")
edit.add_separator()
edit.add_command(label="Cut                       Ctrl+X")  
edit.add_command(label="Copy                    Ctrl+C")  
edit.add_command(label="Paste                    Ctrl+V")  
edit.add_command(label="Delete                   Del")
edit.add_separator()
edit.add_command(label="Find                      Ctrl+F")
edit.add_command(label="Find next              F3")
edit.add_command(label="Find previous       Shift+F3")
edit.add_command(label="Replace                 Ctrl+H")
edit.add_command(label="Go to                     Ctrl+G")
edit.add_separator()
edit.add_command(label="Select all               Ctrl+A")
edit.add_command(label="Time/Date            F5")
edit.add_separator()
edit.add_command(label="Font")
menubar.add_cascade(label="Edit",menu=edit)

view=Menu(menubar,tearoff=0,background="white",bd=-15)
zoom=Menu(view,tearoff=0,bg="gray25",background="white",)
zoom.add_command(label="Zoom in                                     Ctrl+Plus")
zoom.add_command(label="Zoom out                                  Ctrl+Minus")
zoom.add_command(label="Restore default zoom               Ctrl+0")
view.add_cascade(label="Zoom",menu=zoom)
view.add_checkbutton(label="Status bar")
view.add_checkbutton(label="Word warp")
menubar.add_cascade(label="View",menu=view)

N_P.config(menu=menubar)
scroll_bar=Scrollbar(N_P)
scroll_bar.pack(side="right",fill="both")
text=Text(N_P,background="white",yscrollcommand=scroll_bar.set,foreground="black",font=("Consolas",11))
text.pack(side="left",expand=True,fill="both")
scroll_bar.config(command=text.yview_moveto)

N_P.mainloop()
