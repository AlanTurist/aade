import pyautogui # type: ignore
import time
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

class FileProcessorApp:
    def __init__(self, root):
        self.root = root
        self.root.title(" Georgios Koliou - Casa Cook Rhodes IT Manager ")
        
        self.name_label = tk.Label(root, text=" Ανέβασμα αρχείων ΑΑΔΕ ", font=("Helvetica", 16))
        self.name_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        
        self.folder_label = tk.Label(root, text=" Διαδρομή Φακέλου: ")
        self.folder_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.folder_entry = tk.Entry(root, width=50)
        self.folder_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.browse_button = tk.Button(root, text=" Περιήγηση ", command=self.browse_folder)
        self.browse_button.grid(row=1, column=2, padx=10, pady=10)
        
        self.num_files_label = tk.Label(root, text=" Αριθμός Αρχείων: ")
        self.num_files_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.num_files_entry = tk.Entry(root, width=10)
        self.num_files_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.set_position_button = tk.Button(root, text=" Θέση Ποντικιού ", command=self.set_mouse_position)
        self.set_position_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        
        self.start_button = tk.Button(root, text=" Έναρξη Επεξεργασίας ", command=self.start_processing)
        self.start_button.grid(row=4, column=0, columnspan=3, padx=10, pady=10)
        
        self.first_file_position = None

    def browse_folder(self):
        folder_path = filedialog.askdirectory()
        self.folder_entry.delete(0, tk.END)
        self.folder_entry.insert(0, folder_path)

    def set_mouse_position(self):
        messagebox.showinfo("Πληροφορία", "Παρακαλώ τοποθετήστε το ποντίκι στο πρώτο αρχείο και πατήστε Enter...")
        self.root.bind('<Return>', self.save_mouse_position)

    def save_mouse_position(self, event):
        self.first_file_position = pyautogui.position()
        messagebox.showinfo("Πληροφορία", f"Η θέση του ποντικιού αποθηκεύτηκε: {self.first_file_position}")
        self.root.unbind('<Return>')

    def right_click_and_select_third_option(self):
        pyautogui.rightClick()
        time.sleep(0.5)
        pyautogui.press('down')
        pyautogui.press('down')
        #pyautogui.press('down')
        pyautogui.press('enter')

    def process_files_in_folder(self, folder_path, num_files):
        files = os.listdir(folder_path)
        files.sort()
        
        if not files:
            messagebox.showinfo("Πληροφορία", "Ο φάκελος είναι άδειος.")
            return

        if self.first_file_position is None:
            messagebox.showwarning("Προειδοποίηση", "Η θέση του ποντικιού δεν έχει οριστεί.")
            return

        for i in range(num_files):
            if i < len(files):
                file_path = os.path.join(folder_path, files[i])
                print(f"Processing file: {file_path}")
                pyautogui.moveTo(self.first_file_position)
                time.sleep(0.5)
                self.right_click_and_select_third_option()
                time.sleep(5)
            else:
                messagebox.showinfo("Πληροφορία", "Δεν υπάρχουν τόσα αρχεία στον φάκελο.")
                break

    def start_processing(self):
        folder_path = self.folder_entry.get()
        num_files = int(self.num_files_entry.get())
        if folder_path and num_files > 0:
            self.process_files_in_folder(folder_path, num_files)
        else:
            messagebox.showwarning("Προειδοποίηση", "Παρακαλώ εισάγετε έγκυρα στοιχεία.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FileProcessorApp(root)
    root.mainloop()