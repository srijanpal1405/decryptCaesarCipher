import tkinter
import tkinter.messagebox
import customtkinter
import random
import os
from langdetect import detect_langs

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Caesar Cipher")
        self.geometry(f"{700}x{350}")

        #grid 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        #making navigation frame on the left
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(7, weight=1)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Caesar Cipher v1.0",
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.button1 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Standard Encryption [3]",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     anchor="w", command=self.button1_event)
        self.button1.grid(row=1, column=0, sticky="ew")
        self.button2 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Encryption with random key [0-25]",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     anchor="w", command=self.button2_event)
        self.button2.grid(row=2, column=0, sticky="ew")
        self.button3 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Encryption with user key",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     anchor="w", command=self.button3_event)
        self.button3.grid(row=3, column=0, sticky="ew")
        self.button4 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Standard Decryption [3]",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     anchor="w", command=self.button4_event)
        self.button4.grid(row=4, column=0, sticky="ew")
        self.button5 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Decryption table [0-25]",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     anchor="w", command=self.button5_event)
        self.button5.grid(row=5, column=0, sticky="ew")
        self.button6 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Decryption with user key",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     anchor="w", command=self.button6_event)
        self.button6.grid(row=6, column=0, sticky="ew")
        self.button7 = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="SMART Decryption",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                     anchor="w", command=self.button7_event)
        self.button7.grid(row=7, column=0, sticky="ew")

        #Standard Encryption Frame
        self.button1_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.button1_frame.grid_columnconfigure((0,1), weight=1)
        self.button1_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.button1_frame_title = customtkinter.CTkLabel(self.button1_frame, text="Standard Encryption",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button1_frame_title.grid(row=0, column=0, padx=20, pady=15, columnspan=2)
        self.button1_frame_label = customtkinter.CTkLabel(self.button1_frame, text="Enter text to encrpyt: ",compound="left")
        self.button1_frame_label.grid(row=1, column=0, sticky="e")
        self.button1_frame_entry = customtkinter.CTkEntry(self.button1_frame, placeholder_text="Text Here", width=285, height=50, corner_radius=10)
        self.button1_frame_entry.grid(row=1, column=1, padx=10)
        self.button1_frame_keylabel = customtkinter.CTkLabel(self.button1_frame, text="Key : 3",compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.button1_frame_keylabel.grid(row=2, column=0, columnspan=2)
        self.button1_frame_submitbutton = customtkinter.CTkButton(self.button1_frame, text="Encrpyt",width=425, height=40, command=self.standardenc)
        self.button1_frame_submitbutton.grid(row=3, column=0, columnspan=2)
        self.button1_frame_textbox = customtkinter.CTkTextbox(self.button1_frame, height=80, width=425, corner_radius=10)
        self.button1_frame_textbox.grid(row=4, column=0, columnspan=2, pady=10)

        #Random Encryption Frame
        self.button2_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.button2_frame.grid_columnconfigure((0,1), weight=1)
        self.button2_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.button2_frame_title = customtkinter.CTkLabel(self.button2_frame, text="Random Key Encryption",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button2_frame_title.grid(row=0, column=0, padx=20, pady=15, columnspan=2)
        self.button2_frame_label = customtkinter.CTkLabel(self.button2_frame, text="Enter text to encrpyt: ",compound="left")
        self.button2_frame_label.grid(row=1, column=0, sticky="e")
        self.button2_frame_entry = customtkinter.CTkEntry(self.button2_frame, placeholder_text="Text Here", width=285, height=50, corner_radius=10)
        self.button2_frame_entry.grid(row=1, column=1, padx=10)
        self.key=random.randint(1,25)
        self.button2_frame_keylabel = customtkinter.CTkLabel(self.button2_frame, text=f"Key : {self.key}",font=customtkinter.CTkFont(size=15, weight="bold"))
        self.button2_frame_keylabel.grid(row=2, column=0, sticky="e")
        self.button2_frame_randombutton = customtkinter.CTkButton(self.button2_frame, text="Randomize Key", command=self.randomize)
        self.button2_frame_randombutton.grid(row=2, column=1)
        # self.button2_frame_keyentry = customtkinter.CTkEntry(self.button2_frame, placeholder_text="0-25", width=50 ,corner_radius=10)
        # self.button2_frame_keyentry.grid(row=2, column=1)
        self.button2_frame_submitbutton = customtkinter.CTkButton(self.button2_frame, text="Encrpyt",width=425, height=40,  command=lambda:self.randomenc(self.key))
        self.button2_frame_submitbutton.grid(row=3, column=0, columnspan=2)
        self.button2_frame_textbox = customtkinter.CTkTextbox(self.button2_frame, height=80, width=425, corner_radius=10)
        self.button2_frame_textbox.grid(row=4, column=0, columnspan=2, pady=10)

        #Encrytion User Key Frame
        self.button3_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.button3_frame.grid_columnconfigure((0,1), weight=1)
        self.button3_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.button3_frame_title = customtkinter.CTkLabel(self.button3_frame, text="User Key Encryption",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button3_frame_title.grid(row=0, column=0, padx=20, pady=15, columnspan=2)
        self.button3_frame_label = customtkinter.CTkLabel(self.button3_frame, text="Enter text to encrpyt: ",compound="left")
        self.button3_frame_label.grid(row=1, column=0, sticky="e")
        self.button3_frame_entry = customtkinter.CTkEntry(self.button3_frame, placeholder_text="Text Here", width=285, height=50, corner_radius=10)
        self.button3_frame_entry.grid(row=1, column=1, padx=10)
        self.button3_frame_keylabel = customtkinter.CTkLabel(self.button3_frame, text=f"Key :",font=customtkinter.CTkFont(size=15, weight="bold"))
        self.button3_frame_keylabel.grid(row=2, column=0, sticky="e")
        self.button3_frame_keyentry = customtkinter.CTkEntry(self.button3_frame, placeholder_text="Enter a valid key in range 0-25 (default: 0)", width=285 ,corner_radius=10)
        self.button3_frame_keyentry.grid(row=2, column=1)
        self.button3_frame_submitbutton = customtkinter.CTkButton(self.button3_frame, width=425, height=40, text="Encrpyt",compound="left", command=self.userenc)
        self.button3_frame_submitbutton.grid(row=3, column=0, columnspan=2)
        self.button3_frame_textbox = customtkinter.CTkTextbox(self.button3_frame, height=80, width=425, corner_radius=10)
        self.button3_frame_textbox.grid(row=4, column=0, columnspan=2, pady=10)

        #Standard Decryption
        self.button4_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.button4_frame.grid_columnconfigure((0,1), weight=1)
        self.button4_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.button4_frame_title = customtkinter.CTkLabel(self.button4_frame, text="Standard Decryption",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button4_frame_title.grid(row=0, column=0, padx=20, pady=15, columnspan=2)
        self.button4_frame_label = customtkinter.CTkLabel(self.button4_frame, text="Enter text to decrpyt: ",compound="left")
        self.button4_frame_label.grid(row=1, column=0, sticky="e")
        self.button4_frame_entry = customtkinter.CTkEntry(self.button4_frame, placeholder_text="Text Here", width=285, height=50, corner_radius=10)
        self.button4_frame_entry.grid(row=1, column=1, padx=10)
        self.button4_frame_keylabel = customtkinter.CTkLabel(self.button4_frame, text="Key : 3",compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.button4_frame_keylabel.grid(row=2, column=0, columnspan=2)
        self.button4_frame_submitbutton = customtkinter.CTkButton(self.button4_frame, text="Decrpyt",width=425, height=40, command=self.standarddec)
        self.button4_frame_submitbutton.grid(row=3, column=0, columnspan=2)
        self.button4_frame_textbox = customtkinter.CTkTextbox(self.button4_frame, height=80, width=425, corner_radius=10)
        self.button4_frame_textbox.grid(row=4, column=0, columnspan=2, pady=10)

        #Decryption Table
        self.button5_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.button5_frame.grid_columnconfigure((0,1), weight=1)
        self.button5_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.button5_frame_title = customtkinter.CTkLabel(self.button5_frame, text="Decryption Table",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button5_frame_title.grid(row=0, column=0, padx=20, pady=15, columnspan=2)
        self.button5_frame_label = customtkinter.CTkLabel(self.button5_frame, text="Enter text to decrpyt: ",compound="left")
        self.button5_frame_label.grid(row=1, column=0, sticky="e")
        self.button5_frame_entry = customtkinter.CTkEntry(self.button5_frame, placeholder_text="Text Here", width=285, height=50, corner_radius=10)
        self.button5_frame_entry.grid(row=1, column=1, padx=10)
        self.button5_frame_submitbutton = customtkinter.CTkButton(self.button5_frame, text="Decrpyt",width=425, height=40, command=self.decrypttable)
        self.button5_frame_submitbutton.grid(row=2, column=0, columnspan=2)
        self.button5_frame_statuslabel = customtkinter.CTkLabel(self.button5_frame, text="Decryption Table will be created in a txt file.")
        self.button5_frame_statuslabel.grid(row=3, column=0, columnspan=2)

        #User Key Decryption
        self.button6_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.button6_frame.grid_columnconfigure((0,1), weight=1)
        self.button6_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.button6_frame_title = customtkinter.CTkLabel(self.button6_frame, text="User Key Decryption",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button6_frame_title.grid(row=0, column=0, padx=20, pady=15, columnspan=2)
        self.button6_frame_label = customtkinter.CTkLabel(self.button6_frame, text="Enter text to decrpyt: ",compound="left")
        self.button6_frame_label.grid(row=1, column=0, sticky="e")
        self.button6_frame_entry = customtkinter.CTkEntry(self.button6_frame, placeholder_text="Text Here", width=285, height=50, corner_radius=10)
        self.button6_frame_entry.grid(row=1, column=1, padx=10)
        self.button6_frame_keylabel = customtkinter.CTkLabel(self.button6_frame, text=f"Key :",font=customtkinter.CTkFont(size=15, weight="bold"))
        self.button6_frame_keylabel.grid(row=2, column=0, sticky="e")
        self.button6_frame_keyentry = customtkinter.CTkEntry(self.button6_frame, placeholder_text="Enter a valid key in range 0-25 (default: 0)", width=285 ,corner_radius=10)
        self.button6_frame_keyentry.grid(row=2, column=1)
        self.button6_frame_submitbutton = customtkinter.CTkButton(self.button6_frame, width=425, height=40, text="Decrpyt",compound="left", command=self.userdec)
        self.button6_frame_submitbutton.grid(row=3, column=0, columnspan=2)
        self.button6_frame_textbox = customtkinter.CTkTextbox(self.button6_frame, height=80, width=425, corner_radius=10)
        self.button6_frame_textbox.grid(row=4, column=0, columnspan=2, pady=10)

        self.button7_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.button7_frame.grid_columnconfigure((0,1), weight=1)
        self.button7_frame.grid_rowconfigure((0,1,2,3,4,5), weight=1)
        self.button7_frame_title = customtkinter.CTkLabel(self.button7_frame, text="SMART Decryption",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button7_frame_title.grid(row=0, column=0, padx=20, pady=15, columnspan=2)
        self.button7_frame_label = customtkinter.CTkLabel(self.button7_frame, text="Enter text to decrpyt: ",compound="left")
        self.button7_frame_label.grid(row=1, column=0, sticky="e")
        self.button7_frame_entry = customtkinter.CTkEntry(self.button7_frame, placeholder_text="Text Here", width=285, height=50, corner_radius=10)
        self.button7_frame_entry.grid(row=1, column=1, padx=10)
        self.button7_frame_submitbutton = customtkinter.CTkButton(self.button7_frame, text="Decrpyt",width=425, height=40, command=self.smartdec)
        self.button7_frame_submitbutton.grid(row=2, column=0, columnspan=2)
        self.button7_frame_statuslabel = customtkinter.CTkLabel(self.button7_frame, text="SMART Decryption will find the most probable set of keys for the encrypted text.")
        self.button7_frame_statuslabel.grid(row=3, column=0, columnspan=2)

        self.select_frame_by_name("button1")


    def select_frame_by_name(self, name):
        # set button color for selected button
        self.button1.configure(fg_color=("gray75", "gray25") if name == "button1" else "transparent")
        self.button2.configure(fg_color=("gray75", "gray25") if name == "button2" else "transparent")
        self.button3.configure(fg_color=("gray75", "gray25") if name == "button3" else "transparent")
        self.button4.configure(fg_color=("gray75", "gray25") if name == "button4" else "transparent")
        self.button5.configure(fg_color=("gray75", "gray25") if name == "button5" else "transparent")
        self.button6.configure(fg_color=("gray75", "gray25") if name == "button6" else "transparent")
        self.button7.configure(fg_color=("gray75", "gray25") if name == "button7" else "transparent")

        # show selected frame
        if name == "button1":
            self.button1_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.button1_frame.grid_forget()
        if name == "button2":
            self.button2_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.button2_frame.grid_forget()
        if name == "button3":
            self.button3_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.button3_frame.grid_forget()
        if name == "button4":
            self.button4_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.button4_frame.grid_forget()
        if name == "button5":
            self.button5_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.button5_frame.grid_forget()
        if name == "button6":
            self.button6_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.button6_frame.grid_forget()
        if name == "button7":
            self.button7_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.button7_frame.grid_forget()

    def button1_event(self):
        self.select_frame_by_name("button1")  

    def button2_event(self):
        self.select_frame_by_name("button2")

    def button3_event(self):
        self.select_frame_by_name("button3") 

    def button4_event(self):
        self.select_frame_by_name("button4")
    
    def button5_event(self):
        self.select_frame_by_name("button5")

    def button6_event(self):
        self.select_frame_by_name("button6")

    def button7_event(self):
        self.select_frame_by_name("button7")

    def standardenc(self):
        self.button1_frame_textbox.delete("1.0","end")
        text=self.button1_frame_entry.get() 
        result=self.encryption(text,3)
        print(result)
        self.button1_frame_textbox.insert("0.0", result)
        r = tkinter.Tk()
        r.clipboard_append(result)
        r.destroy()

    def randomenc(self, key):
        self.button2_frame_textbox.delete("1.0","end")
        text=self.button2_frame_entry.get() 
        result=self.encryption(text,key)
        print(result)
        self.button2_frame_textbox.insert("0.0", result)
        r = tkinter.Tk()
        r.clipboard_append(result)
        r.destroy()

    def randomize(self):
        self.key=random.randint(1,25)
        self.button2_frame_keylabel.configure(text=f"Key : {self.key}")

    def userenc(self):
        self.button3_frame_textbox.delete("1.0","end")
        text=self.button3_frame_entry.get() 
        key=int(self.button3_frame_keyentry.get())
        result=self.encryption(text,key)
        print(result)
        self.button3_frame_textbox.insert("0.0", result)
        r = tkinter.Tk()
        r.clipboard_append(result)
        r.destroy()

    def standarddec(self):
        self.button4_frame_textbox.delete("1.0","end")
        text=self.button4_frame_entry.get() 
        result=self.decryption(text,3)
        print(result)
        self.button4_frame_textbox.insert("0.0", result)
        r = tkinter.Tk()
        r.clipboard_append(result)
        r.destroy()

    def decrypttable(self):
        text=self.button5_frame_entry.get() 
        with open("DecryptionTable.txt", "w") as f:
            f.write("Key\tText\n")
            f.write("=============================\n")
            for i in range(0,26):
                result=self.decryption(text,i)
                f.write(f"{i}\t{result}\n")
        self.button5_frame_statuslabel.configure(text="File created DecryptionTable.txt!")
        self.button5_frame_openbutton = customtkinter.CTkButton(self.button5_frame, text="Open File", command=self.openfile)
        self.button5_frame_openbutton.grid(row=4, column=0, columnspan=2)
        
    def openfile(self):
        os.startfile('DecryptionTable.txt')

    def smartdec(self):
        text=self.button7_frame_entry.get() 
        # DetectorFactory.seed = 0
        self.keys=[]
        for i in range(0,26):
            result=self.decryption(text,i)
            langtest=detect_langs(result)
            # print(f"{i} {result} {langtest}")
            lang_conf=str(langtest[0])
            lang=lang_conf.split(":")[0]
            conf=float(lang_conf.split(":")[1])
            if(lang=="en" and conf>0.7):
                self.keys.append(i)
                with open(f"Decrypted_Key{i}.txt", "w") as f:
                    f.write(f"{result}")
        self.button7_frame_statuslabel.configure(text=f"Possible keys: {self.keys}",font=customtkinter.CTkFont(size=15, weight="bold"))
        self.button7_frame_openbutton = customtkinter.CTkButton(self.button7_frame, text="Open Decrypted Files", command=self.openfiles)
        self.button7_frame_openbutton.grid(row=4, column=0, columnspan=2)

    def openfiles(self):
        for key in self.keys:
            os.startfile(f'Decrypted_Key{key}.txt')
        
    def userdec(self):
        self.button6_frame_textbox.delete("1.0","end")
        text=self.button6_frame_entry.get() 
        key=int(self.button6_frame_keyentry.get())
        result=self.decryption(text,key)
        print(result)
        self.button6_frame_textbox.insert("0.0", result)
        r = tkinter.Tk()
        r.clipboard_append(result)
        r.destroy()

    def encryption(self, text, key):
        enc=""
        for ch in text:
            if (ch.isupper()):
                enc+=chr((ord(ch)+key-65)%26+65)
            elif (ch.islower()):
                enc+=chr((ord(ch)+key-97)%26+97)
            else:
                enc+=ch
        return enc
    
    def decryption(self, text, key):
        dec=""
        for ch in text:
            if (ch.isupper()):
                dec+=chr((ord(ch)-key-65)%26+65)
            elif (ch.islower()):
                dec+=chr((ord(ch)-key-97)%26+97)
            else:
                dec+=ch
        return dec
    


if __name__ == "__main__":
    app = App()
    app.mainloop()