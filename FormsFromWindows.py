#####################################################################################################
## The following script presents a graphical interface using python with a message that addresses  ##
## the user to fill out an online form when a button is executed, in addition to having            ##
## disabled the control of the window, preventing the user from not complying with the request     ##
## this will only be closed when the user is allowed to enter the link for the survey              ##
#####################################################################################################





#Import libraries
import tkinter as tk
import webbrowser
import sys
import os

#Define functions


#This function is the one assigned to Button1:

def linkclic():
    #Direct to the link within the attribute using the
    #preferred browser
   webbrowser.open("your-link-here")
   #the windows closes:
   ventana.destroy()

################################################################################
## The following function has the task of packing the referenced images       ##
## in a path, in order to be executed from the .exe without the need of       ##
## include them in a directory                                                ##
################################################################################

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

#This function helps us to disable the window controls:
def __Cancel(event=None): pass

   
#Define objects

#######################
#####///Window///######
#######################

ventana=tk.Tk()
ventana.geometry("600x450")
ventana.resizable(0, 0)
ventana.title("Aviso importante")
ventana.configure(background="#ffffff")
ventana.configure(highlightbackground="#ffffff")
ventana.configure(highlightcolor="black")
ventana.iconbitmap(resource_path("ico.ico"))
ventana.attributes("-toolwindow",-1)
ventana.protocol('WM_DELETE_WINDOW', __Cancel )


######################
######///LOGO///######
######################


img=tk.PhotoImage(file=resource_path("logo.png"))
lbl_img= tk.Label(ventana,image=img)
lbl_img.configure(background="#ffffff")
lbl_img.pack()


#########################
######///Message///######
#########################


Message1 = tk.Message(ventana)
Message1.place(relx=0.283, rely=0.40, relheight=0.153, relwidth=0.45)
Message1.configure(background="#ffffff")
Message1.configure(font="-family {Tahoma} -size 16")
Message1.configure(foreground="#000000")
Message1.configure(highlightbackground="#d9d9d9")
Message1.configure(highlightcolor="black")
Message1.configure(padx="1")
Message1.configure(pady="1")
Message1.configure(text='''Por favor diligenciar la encuesta que se relaciona en el siguiente enlace''')
Message1.configure(width=300)

#########################
#######///Button///######
#########################


Button1 = tk.Button(ventana,command=linkclic)
Button1.place(relx=0.367, rely=0.667, height=54, width=157)
Button1.configure(activebackground="beige")
Button1.configure(activeforeground="#7396f2")
Button1.configure(background="#7396f2")
Button1.configure(compound='left')
Button1.configure(disabledforeground="#a3a3a3")
Button1.configure(font="-family {Tahoma} -size 12")
Button1.configure(foreground="#000000")
Button1.configure(highlightbackground="#d9d9d9")
Button1.configure(highlightcolor="black")
Button1.configure(pady="0")
Button1.configure(text='''Presentar encuesta''')

ventana.mainloop()