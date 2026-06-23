import tkinter as tk
import tkinter.font as font

# Create window
root = tk.Tk()
root.title("Font Samples")

# Get font list and sort
font_list = sorted(font.families())

# Display a few font samples (you can increase the limit if you want)
# for i, fname in enumerate(font_list[:40]):  # Showing only first 20 for readability
#     sample_font = font.Font(family=fname, size=10)
#     tk.Label(root, text=f"This is {fname}", font=sample_font).pack(anchor='w')

# Display in two columns
for i, fname in enumerate(font_list[:180]):  # Show first 40 fonts
    sample_font = font.Font(family=fname, size=10)
    col = i % 7     # 0 for left column, 1 for right column
    row = i // 7    # Row number (increases every two fonts)
    tk.Label(root, text=f"{fname}", font=sample_font).grid(row=row, column=col)

root.mainloop()
