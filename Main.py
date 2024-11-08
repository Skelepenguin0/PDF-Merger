#pip install pypdf2
import os
from tkinter import Tk, filedialog, messagebox
from PyPDF2 import PdfMerger

def merge_pdfs_in_folder(folder_path, output_filename='merged_output.pdf'):
    merger = PdfMerger()

    for root, _, files in os.walk(folder_path):
        pdf_files = [file for file in files if file.endswith('.pdf')]
        if not pdf_files:
            messagebox.showwarning("No PDFs found", "No PDF files found in the selected folder.")
            return

        pdf_files.sort()  

        for pdf in pdf_files:
            pdf_path = os.path.join(root, pdf)
            merger.append(pdf_path)

    output_path = os.path.join(folder_path, output_filename)
    merger.write(output_path)
    merger.close()
    messagebox.showinfo("Success", f"PDFs merged successfully into {output_path}")

def select_folder():
    root = Tk()
    root.withdraw() 
    folder_path = filedialog.askdirectory(title="Select Folder Containing PDFs")

    if folder_path:
        merge_pdfs_in_folder(folder_path)
    else:
        messagebox.showwarning("No Folder Selected", "Please select a folder to proceed.")

if __name__ == "__main__":
    select_folder()
