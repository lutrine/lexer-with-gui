import tkinter as tk
import lexer as lex

def run_lexer():
    code = code_text.get("1.0", tk.END)
    if code == "":
        return
    output_text.focus_set()
    output = lex.cut_one_line_tokens(code)  
    output_text.config(state=tk.NORMAL)  # Enable editing
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, output)
    output_text.config(state=tk.DISABLED)  # Disable editing


root = tk.Tk()
root.title("Lexer")
root.bind("<Control-Return>", lambda e: run_lexer())
root.bind("<Escape>", lambda e: root.quit())

# Code frame
code_frame = tk.Frame(root)
code_frame.pack()

code_label = tk.Label(code_frame, text="Enter Code Here:")
code_label.pack()

code_text = tk.Text(code_frame, height=10, width=50)
code_text.pack()

run_button = tk.Button(code_frame, text="Run Lexer", command=run_lexer)
run_button.pack()

# Output frame
output_frame = tk.Frame(root)
output_frame.pack()

output_label = tk.Label(output_frame, text="Output:")
output_label.pack()

output_text = tk.Text(output_frame, height=10, width=50)
output_text.pack()
output_text.config(state=tk.DISABLED)  # Set initial state to disabled

root.mainloop()
