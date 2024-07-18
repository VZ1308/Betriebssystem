import csv

class CSVHandler:
    def __init__(self, filename):
        # Initialisiere den Dateinamen für die CSV-Datei
        self.filename = filename

    def save_to_csv(self, data):
        try:
            # Öffne die CSV-Datei im Schreibmodus
            with open(self.filename, 'w', newline='') as file:
                writer = csv.writer(file)
                # Schreibe jede Zeile der Daten in die CSV-Datei
                for row in data:
                    writer.writerow(row)
        except Exception as e:
            # Fehlerbehandlung: Gibt eine Fehlermeldung aus, falls ein Fehler auftritt
            print(f"Fehler: {e}")

    def read_from_csv(self):
        data = []
        try:
            # Öffne die CSV-Datei im Lesemodus
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                # Lese jede Zeile aus der CSV-Datei und füge sie der Datenliste hinzu
                for row in reader:
                    data.append(row)
        except FileNotFoundError:
            # Fehlerbehandlung: Gibt eine Meldung aus, falls die Datei nicht gefunden wurde
            print("CSV Datei nicht gefunden.")
        except Exception as e:
            # Fehlerbehandlung: Gibt eine allgemeine Fehlermeldung aus, falls ein Fehler auftritt
            print(f"Fehler: {e}")
        return data
