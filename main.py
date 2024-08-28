import tkinter as tk
from tkinter import filedialog, messagebox
from tkinterdnd2 import TkinterDnD, DND_FILES
from docx import Document
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def select_word_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word files", "*.docx")])
    if file_path:
        add_file_to_list(file_path)

def add_file_to_list(file_path):
    if file_path.endswith(".docx"):
        listbox.insert(tk.END, os.path.basename(file_path))
        listbox.file_paths.append(file_path)

def drop(event):
    file_paths = app.tk.splitlist(event.data)
    for file_path in file_paths:
        if file_path.lower().endswith(".docx"):
            add_file_to_list(file_path)

def convert_to_pdf():
    if not listbox.file_paths:
        messagebox.showerror("Error", "No Word file selecteds")
        return

    for word_file_path in listbox.file_paths:
        try:
            doc = Document(word_file_path)
            pdf_file_name = os.path.splitext(os.path.basename(word_file_path))[0] + ".pdf"
            pdf_file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")], initialfile=pdf_file_name)
            if not pdf_file_path:
                return
            
            pdf = canvas.Canvas(pdf_file_path, pagesize=letter)
            width, height = letter
            
            y_position = height - 40  # Start position for text
            for para in doc.paragraphs:
                if y_position < 40:  # Add new page if needed
                    pdf.showPage()
                    y_position = height - 40
                
                text = para.text
                pdf.drawString(40, y_position, text)
                y_position -= 20
            
            pdf.save()
            pdf_file_name = os.path.basename(pdf_file_path)  # Extract the file name for the message
            messagebox.showinfo("Success", f"Converted to PDF: {pdf_file_name}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert {os.path.basename(word_file_path)} to PDF: {e}")

app = TkinterDnD.Tk()
app.title("Word to PDF Converter")

frame = tk.Frame(app)
frame.pack(pady=10, padx=10)

label_instruction = tk.Label(frame, text="Drag and drop Word files here or use 'Browse' button:")
label_instruction.grid(row=0, column=0, pady=5, columnspan=3)

listbox = tk.Listbox(frame, selectmode=tk.SINGLE, width=50, height=10)
listbox.grid(row=1, column=0, pady=5, columnspan=3)
listbox.file_paths = []

app.drop_target_register(DND_FILES)
app.dnd_bind('<<Drop>>', drop)

button_browse = tk.Button(frame, text="Browse", command=select_word_file)
button_browse.grid(row=2, column=0, pady=5, columnspan=3)

button_convert = tk.Button(app, text="Convert to PDF", command=convert_to_pdf)
button_convert.pack(pady=20)

app.mainloop()
