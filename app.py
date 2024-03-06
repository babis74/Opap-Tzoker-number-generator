import tkinter as tk
from tkinter import filedialog
from random import sample, randint

# List to store generated results
generated_results = []

def generate_numbers():
    global generated_results

    # Generate 5 random numbers from 1 to 45
    lotto_numbers = sample(range(1, 46), 5)
    
    # Generate 1 random number from 1 to 20
    extra_number = randint(1, 20)
    
    # Store only the generated numbers in the list
    current_result = {
        'lotto_numbers': lotto_numbers,
        'extra_number': extra_number
    }
    generated_results.append(current_result)

    # Display the generated numbers in the label vertically with margin
    result_text = result_label.cget("text")  # Get current text
    
    # Append the new result without line numbers
    result_text += f"Πάρε τα 5 τυχαία νούμερα: {current_result['lotto_numbers']}\nΠάρε και τον Tζόκερ: {current_result['extra_number']}\n{'-' * 30}\n"
    
    # Update the label text
    result_label.config(text=result_text, fg="white")

    # Disable the button after 5 results
    if len(generated_results) == 5:
        generate_button.config(state=tk.DISABLED)

def save_to_txt():
    # Save the results to a text file on the desktop
    desktop_path = filedialog.askdirectory(initialdir="~/Desktop", title="Select Desktop Folder")
    if desktop_path:
        file_path = f"{desktop_path}/τυχαία-νουμερα-τζοκερ.txt"
        with open(file_path, 'w') as file:
            for result in generated_results:
                file.write(f"Πάρε τα 5 τυχαία νούμερα: {result['lotto_numbers']}\nΠάρε και τον Tζόκερ: {result['extra_number']}\n{'-' * 30}\n")

# Create the main window
window = tk.Tk()
window.title("Γεννήτρια τυχαίων αριθμών ΤΖΟΚΕΡ")
window.configure(bg="#201658")  # Set background color

# Set the size of the window (width x height)
window.geometry("800x600")  # Change the values to your desired width and height

# Add text at the top
title_label = tk.Label(window, text="Παίξε τυχαίους αριθμούς στο ΤΖΟΚΕΡ!", font=("Helvetica", 16, "bold"), bg="#201658", fg="white")
title_label.pack(pady=10)

# Create and place widgets with background color and text color
generate_button = tk.Button(window, text="Πάρε τυχαίους αριθμούς", command=generate_numbers, bg="#54B435", fg="white")
generate_button.pack(pady=10)

save_button = tk.Button(window, text="Αποθήκευση σε αρχείο", command=save_to_txt, bg="#54B435", fg="white")
save_button.pack(pady=10)

result_label = tk.Label(window, text="", font=("Courier New", 12), wraplength=600, bg="#201658", fg="white")
result_label.pack(pady=10)

# Start the Tkinter event loop
window.mainloop()
