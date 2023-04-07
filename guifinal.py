import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


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
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="Caesar Cipher",
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
        self.button1_frame.grid_columnconfigure(0, weight=1)
        self.button1_frame.grid_rowconfigure((0,1,2), weight=1)
        self.button1_frame_button_1 = customtkinter.CTkLabel(self.button1_frame, text="Standard Encryption",compound="left", font=customtkinter.CTkFont(size=22, weight="bold"))
        self.button1_frame_button_1.grid(row=0, column=0, padx=20)

        self.button2_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.button3_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.button4_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.button5_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.button6_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.button7_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

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
        print("Encryption successful!1")
        self.select_frame_by_name("button1")   

    def button2_event(self):
        print("Encryption successful!2")
        self.select_frame_by_name("button2")

    def button3_event(self):
        print("Encryption successful!3")
        self.select_frame_by_name("button3") 

    def button4_event(self):
        print("Encryption successful!4")
        self.select_frame_by_name("button4")
    
    def button5_event(self):
        print("Encryption successful!5")
        self.select_frame_by_name("button5")

    def button6_event(self):
        print("Encryption successful!6")
        self.select_frame_by_name("button6")

    def button7_event(self):
        print("Encryption successful!7")
        self.select_frame_by_name("button7")

if __name__ == "__main__":
    app = App()
    app.mainloop()