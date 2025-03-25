
import tkinter
from tkinter import ttk
import sv_ttk
import darkdetect
import sys
import pywinstyles
import webbrowser  # Import webbrowser module
from tkinter import Tk, PhotoImage

root = tkinter.Tk()

# Set window title 
root.title("Daily Launchpad")

# Use a PNG file as the window icon
icon_path = r"C:\Users\cchri\OneDrive\Documents\python_Scripts\Applications\DailyLaunchpad\Stocks2-icon.png"
icon_image = PhotoImage(file=icon_path)
root.iconphoto(False, icon_image)  # Set the PNG as the window icon

# Set the theme (light or dark) based on the OS setting
sv_ttk.set_theme(darkdetect.theme())

# Set window dimensions
root.geometry("600x350")  # Set the initial window size

# Configure grid for the root window
root.grid_rowconfigure(0, weight=1)  # Allow vertical expansion
root.grid_columnconfigure(0, weight=1)  # Allow main_frame to expand

# Create the main frame for layout (fills the entire window)
main_frame = ttk.Frame(root)
main_frame.grid(row=0, column=0, sticky="nsew")
main_frame.grid_columnconfigure(0, weight=1)  # Sidebar takes 1/3 of the space
main_frame.grid_columnconfigure(1, weight=2)  # Right content takes 2/3 of the space
main_frame.grid_rowconfigure(0, weight=1)  # Ensures full vertical expansion

# Create the left sidebar frame (adjusts dynamically)
left_sidebar = ttk.Frame(main_frame, relief="solid", borderwidth=2)
left_sidebar.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)  # Fill both axes

# Function to open Google in the default browser
def open_google():
    webbrowser.open("https://www.google.com")

# Add content to the left sidebar
sidebar_label = ttk.Label(left_sidebar, text="Links")
sidebar_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

# Button that opens Google
sidebar_button = ttk.Button(left_sidebar, text="Google", command=open_google)
sidebar_button.grid(row=1, column=0, padx=5, pady=10, sticky="w")

# Create the right main content area (this will hold the two vertically stacked sections)
right_content = ttk.Frame(main_frame)
right_content.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
right_content.grid_rowconfigure(0, weight=1)  # Top section expands
right_content.grid_rowconfigure(1, weight=1)  # Bottom section expands
right_content.grid_columnconfigure(0, weight=1)  # Ensure full width usage

# Create the first vertically stacked section (top section)
top_section = ttk.Frame(right_content, relief="solid", borderwidth=2)
top_section.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

# Add content to the top section
top_section_label = ttk.Label(top_section, text="Today")
top_section_label.grid(row=0, column=0, padx=5, pady=5)

# Create the second vertically stacked section (bottom section)
bottom_section = ttk.Frame(right_content, relief="solid", borderwidth=2)
bottom_section.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

# Add content to the bottom section
bottom_section_label = ttk.Label(bottom_section, text="Of Interest")
bottom_section_label.grid(row=0, column=0, padx=5, pady=5)

# Apply the theme to the title bar
def apply_theme_to_titlebar(root):
    version = sys.getwindowsversion()
    if version.major == 10 and version.build >= 22000:
        pywinstyles.change_header_color(root, "#1c1c1c" if sv_ttk.get_theme() == "dark" else "#fafafa")
    elif version.major == 10:
        pywinstyles.apply_style(root, "dark" if sv_ttk.get_theme() == "dark" else "normal")

apply_theme_to_titlebar(root)

root.mainloop()
