import customtkinter

customtkinter.set_appearance_mode("dark") #system
customtkinter.set_default_color_theme("dark-blue")

root=customtkinter.CTk()
root.geometry("500x350")

def encrypt():
    print("works")

frame=customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label=customtkinter.CTkLabel(master=frame, text="Enter text to encrypt: ")
label.pack(pady=12, padx=10)

entry1=customtkinter.CTkEntry(master=frame, placeholder_text="Text")
entry1.pack(pady=12, padx=10)

button=customtkinter.CTkButton(master=frame, text="Encrypt", command=encrypt)
button.pack(pady=12, padx=10)

root.mainloop()