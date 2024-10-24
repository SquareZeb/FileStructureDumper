import os
import tkinter as tk
from tkinter import filedialog

def go(directory):
    name = "FilelistDump"
    with open(f"{name}.txt", "w") as file:
        for dirpath, dirnames, filenames in os.walk(directory):
            parts = dirpath.split(os.sep)
            if len(parts) > 3:
                trimmed_path = os.path.join(*parts[3:])
                for filename in filenames:
                    file.write(os.path.join(trimmed_path, filename) + "\n")

def select_directory():
    print("Select the hunter export directory")
    root = tk.Tk()
    root.withdraw()
    directory = filedialog.askdirectory()
    print("Parsing...")
    go(directory)

select_directory()
print("Done!")
ddirectory = os.path.dirname(os.path.abspath(__file__))
print(f"Dumping the file in {ddirectory}!")
                    