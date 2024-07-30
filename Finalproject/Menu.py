import tkinter as tk
import subprocess
import sys
from tkinter import messagebox

try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# List of projects with their names, file paths, descriptions, and image paths
apps = [
    ("Weather App", "/Users/trentonla4/Desktop/Finalproject/WeatherApp_GUI/weatherApp_GUI.py", "Shows weather forecasts.", "/path/to/weather_icon.png"),
    ("Snake Game", "/Users/trentonla4/Desktop/Finalproject/Freaky_snake/main.py", "Play the classic snake game.", "/path/to/snake_icon.png"),
    ("Chat Bot", "/Users/trentonla4/Desktop/Finalproject/Chatty/Chatty.py", "Talk with a simple chat bot.", "/path/to/chatbot_icon.png"),
    ("Generate AI", "/Users/trentonla4/Desktop/Finalproject/Genaretive AI/main.py", "Generate text using AI.", "/path/to/ai_icon.png"),
    ("Photo Recognition", "/Users/trentonla4/Desktop/Finalproject/AI Recognition/vision.py", "Recognize objects in photos.", "/path/to/recognition_icon.png")
]

def open_project(path):
    """Function to open a project"""
    if path:
        try:
            python_interpreter = sys.executable
            subprocess.Popen([python_interpreter, path])
        except Exception as e:
            messagebox.showerror("Error", f"Error opening project: {e}")
    else:
        messagebox.showwarning("Warning", "No path provided.")

def load_image(image_path):
    """Function to load an image using PIL or tk.PhotoImage"""
    if PIL_AVAILABLE:
        try:
            image = Image.open(image_path)
            return ImageTk.PhotoImage(image)
        except Exception as e:
            print(f"Failed to load image using PIL from {image_path}: {e}")
            return None
    else:
        try:
            return tk.PhotoImage(file=image_path)
        except tk.TclError as e:
            print(f"Failed to load image using tk.PhotoImage from {image_path}: {e}")
            return None

def create_menu(root):
    """Function to create the menu buttons with images and descriptions"""
    for name, path, description, image_path in apps:
        frame = tk.Frame(root, bg='#228B22')
        frame.pack(pady=10, padx=10, fill='x', anchor='w')  # Adjusted padding and alignment

        description_label = tk.Label(frame, text=description, bg='#228B22', fg='white', font=('Helvetica', 12))
        description_label.pack(pady=(0, 5))  # Add padding below the description

        # Load image
        image = load_image(image_path)
        if image:
            print(f"Loaded image for {name} from {image_path}")
        else:
            print(f"Failed to load image for {name} from {image_path}")

        # Create a button with an image
        button = tk.Button(frame, text=name, command=lambda p=path: open_project(p),
                           width=55, height=2, font=('Helvetica', 14), image=image, compound='left')
        button.pack()

        # Keep a reference to the image to prevent it from being garbage-collected
        if image:
            button.image = image

def main():
    # Set up the main window
    root = tk.Tk()
    root.title("Project Menu")
    
    # Set the background color to leaf green
    root.configure(bg='#228B22')  # Hex code for leaf green

    # Create a frame for the title and the exit button
    title_frame = tk.Frame(root, bg='#228B22')
    title_frame.pack(fill='x')

    # Create an exit button
    exit_button = tk.Button(title_frame, text="Exit", command=root.destroy, bg='#ff4c4c', fg='white', font=('Helvetica', 14, 'bold'))
    exit_button.pack(side='left', padx=(10, 0), pady=10)

    # Create a title label with a larger font size and a border
    title_label = tk.Label(title_frame, text="Trenton's Apps!", bg='#228B22', fg='white', font=('Helvetica', 24, 'bold'),
                          borderwidth=4, relief='solid', padx=10, pady=10)
    title_label.pack(pady=(20, 10), padx=(450, 0), side='left')  # Add padding around the title

    # Create a frame to hold the introduction and the buttons
    content_frame = tk.Frame(root, bg='#228B22')
    content_frame.pack(expand=True, fill='both', padx=10, pady=10)

    # Create a frame to hold the introduction on the right
    intro_frame = tk.Frame(content_frame, bg='#228B22')
    intro_frame.pack(side='right', padx=10, pady=10, fill='both', anchor='e')  # Position it to the left with padding

    # Create an introduction label
    intro_label = tk.Label(intro_frame, text="Welcome to the application menu. My Name is Trenton Gravely, part of the Hidden Genius Project. Choose an app below to see the amazing projects I made over the summer.",
                           bg='#228B22', fg='white', font=('Helvetica', 25), wraplength=450, justify='left', anchor='w')
    intro_label.pack(pady=(20), padx=(150), anchor='w')

    # Add photo under the introduction text
    photo_path = "/Users/trentonla4/Documents/GitHub/hgpfinalproject2024/Finalproject/IMG_20230706_131644_240.jpg"
    photo = load_image(photo_path)
    if photo:
        photo_label = tk.Label(intro_frame, image=photo, bg='#228B22')
        photo_label.pack(pady=(10, 20), padx=(150), anchor='nw')  # Add padding below the photo
        photo_label.image = photo  # Keep a reference to the image
    else:
        print(f"Failed to load photo image at {photo_path}")

    # Create a frame to hold the buttons on the left
    button_frame = tk.Frame(content_frame, bg='#228B22')
    button_frame.pack(side='left', expand=True, fill='both', padx=10, pady=10, anchor='w')  # Position it to the left with padding

    # Create the menu buttons with images and descriptions
    create_menu(button_frame)

    # Start the GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
