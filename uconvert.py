from tkinter import Tk, Label, Button, StringVar, filedialog, OptionMenu
from tkinter import messagebox
from pydub import AudioSegment
import os

class AudioConverterGUI:
    def __init__(self, master):
        self.master = master
        master.title("Convertisseur Audio")

        self.label = Label(master, text="Convertisseur de format audio")
        self.label.pack()

        self.format_label = Label(master, text="Sélectionnez le format de sortie:")
        self.format_label.pack()

        self.format_var = StringVar(master)
        self.format_var.set("wav")
        self.format_option = OptionMenu(master, self.format_var, "wav", "mp3", "ogg", "flac", "m4a", "wma", "aac", "mkv", "mp4")
        self.format_option.pack()

        self.source_button = Button(master, text="Sélectionner le ou les fichiers", command=self.select_source_files)
        self.source_button.pack()

        self.target_button = Button(master, text="Sélectionner le dossier cible", command=self.select_target_folder)
        self.target_button.pack()

        self.convert_button = Button(master, text="Convertir", command=self.convert_files)
        self.convert_button.pack()

        self.close_button = Button(master, text="Fermer", command=master.quit)
        self.close_button.pack()

        self.files_selected = ""
        self.target_folder = os.getcwd()

    def select_source_files(self):
        self.files_selected = filedialog.askopenfilenames()

    def select_target_folder(self):
        self.target_folder = filedialog.askdirectory()
        if self.target_folder:
            messagebox.showinfo("Dossier cible sélectionné", f"Dossier cible: {self.target_folder}")

    def convert_files(self):
        if not self.files_selected:
            messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
            return

        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)

        for file in self.files_selected:
            sound = AudioSegment.from_file(file)
            new_format = self.format_var.get()
            new_file = os.path.join(self.target_folder, os.path.basename(file).split(".")[0] + f".{new_format}")
            sound.export(new_file, format=new_format)
            messagebox.showinfo("Succès", f"Conversion terminée pour {os.path.basename(file)}")

        messagebox.showinfo("Succès", "Conversion terminée pour tous les fichiers sélectionnés.")

root = Tk()
my_gui = AudioConverterGUI(root)
root.geometry("300x200")
root.mainloop()
