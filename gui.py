import tkinter as tk
from tkinter import messagebox
from os_info import OSInfo
from csv_handler import CSVHandler

class Application(tk.Frame):  # Die Klasse Application erbt von tk.Frame
    def __init__(self, master=None):  # Der Konstruktor hat das optionale Argument master=None
        super().__init__(master)  # Der Konstruktor von tk.Frame wird aufgerufen, wobei master übergeben wird
        self.master = master  # Das master-Widget wird der Instanzvariable self.master zugewiesen
        self.master.title("OS Informations App")  # Titel des Hauptfensters wird gesetzt
        self.master.geometry("400x300")  # Größe des Hauptfensters wird gesetzt
        self.create_widgets()  # Methode zum Erstellen der Widgets wird aufgerufen
        self.os_info = OSInfo()  # Instanz der Klasse OSInfo wird erstellt
        self.csv_handler = CSVHandler('os_data.csv')  # Instanz der Klasse CSVHandler wird erstellt

    def create_widgets(self):
        # Überschriften Frame und Formatierung
        self.header_frame = tk.Frame(self.master, bg="#2c3e50", pady=10)
        self.header_frame.pack(fill=tk.X)
        # Label Überschrift Formatierung
        self.header_label = tk.Label(self.header_frame, text="OS Information", font=("Helvetica", 16), fg="white", bg="#2c3e50")
        self.header_label.pack()
        # Infoauswahl Frame
        self.info_frame = tk.Frame(self.master, padx=20, pady=10)
        self.info_frame.pack()
        # um den Zustand von Checkboxen zu speichern
        self.platform_var = tk.BooleanVar() # speichert Referenz auf ein Boolean Var Objekt
        self.platform_check = tk.Checkbutton(self.info_frame, text="Platform Info", variable=self.platform_var, font=("Helvetica", 12))
        self.platform_check.pack(anchor=tk.W) # positionierung des Check-Buttons

        self.python_version_var = tk.BooleanVar()
        self.python_version_check = tk.Checkbutton(self.info_frame, text="Python Version", variable=self.python_version_var, font=("Helvetica", 12))
        self.python_version_check.pack(anchor=tk.W)

        self.platform_machine_var = tk.BooleanVar()
        self.platform_machine_check = tk.Checkbutton(self.info_frame, text="Platform Machine", variable=self.platform_machine_var, font=("Helvetica", 12))
        self.platform_machine_check.pack(anchor=tk.W)

        # Button Frame für speichern und laden Button
        self.button_frame = tk.Frame(self.master, pady=10)
        self.button_frame.pack()
        #Speicher Button
        self.save_button = tk.Button(self.button_frame, text="Save to CSV", font=("Helvetica", 12), command=self.save_to_csv)
        self.save_button.pack(side=tk.LEFT, padx=10)
        # Laden Button
        self.load_button = tk.Button(self.button_frame, text="Load from CSV", font=("Helvetica", 12), command=self.load_from_csv)
        self.load_button.pack(side=tk.LEFT, padx=10)

    def save_to_csv(self):
        try:
            selected_data = []

            # Überprüft, ob die Checkbox für "Platform Info" aktiviert ist
            if self.platform_var.get():
                selected_data.append(['Platform Info', self.os_info.get_platform_info()])

            # Überprüft, ob die Checkbox für "Python Version" aktiviert ist
            if self.python_version_var.get():
                selected_data.append(['Python Version', self.os_info.get_python_version()])

            # Überprüft, ob die Checkbox für "Platform Machine" aktiviert ist
            if self.platform_machine_var.get():
                selected_data.append(['Platform Machine', self.os_info.get_platform_machine()])

            # Fügt den aktuellen Zeitstempel hinzu
            selected_data.append(['Timestamp', self.os_info.get_timestamp()])

            # Speichert die gesammelten Daten in eine CSV-Datei
            self.csv_handler.save_to_csv(selected_data)

            # Zeigt eine Informationsbox an, die den Benutzer darüber informiert, dass die Daten erfolgreich gespeichert wurden
            messagebox.showinfo("Gespeichert", "Daten wurden in die CSV Datei gespeichert")

        # Fangt alle möglichen Ausnahmen ab und zeigt eine Fehlermeldung an
        except Exception as e:
            messagebox.showerror("Fehler", f"Speichern fehlgeschlagen: {e}")

    def load_from_csv(self):
        try:
            # Liest die Daten aus der CSV-Datei
            data = self.csv_handler.read_from_csv()

            # Überprüft, ob Daten aus der Datei gelesen wurden
            if data:
                message = ""

                # Erstellt eine Nachricht aus den gelesenen Daten
                for row in data:
                    message += f"{row[0]}: {row[1]}\n"

                # Zeigt eine Informationsbox mit den Daten an
                messagebox.showinfo("Daten von CSV", message)

            # Falls die Datei leer ist oder nicht existiert, zeigt eine Warnung an
            else:
                messagebox.showwarning("Keine Datei", "CSV Datei ist leer oder existiert nicht")

        # Fangt alle möglichen Ausnahmen ab und zeigt eine Fehlermeldung an
        except Exception as e:
            messagebox.showerror("Fehler", f"Speichern fehlgeschlagen: {e}")
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    root.mainloop()
