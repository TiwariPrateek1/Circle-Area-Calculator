from tkinter import *

def calculate_area():
    """Calculates and displays the area of a circle based on user input."""
    try:
        radius_str = radius_entry.get()
        diameter_str = diameter_entry.get()

        if radius_str:
            radius = float(radius_str)
            area = (22 / 7) * radius * radius
            result_label.config(text=f"Area with radius: {area:.2f}") 
        elif diameter_str:
            diameter = float(diameter_str)
            radius = diameter / 2
            area = (22 / 7) * radius * radius
            result_label.config(text=f"Area with diameter: {area:.2f}")
        else:
            result_label.config(text="Please provide either radius or diameter.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")

# Create the main window
window = Tk()
window.title("Circle Area Calculator")

# Create labels and entry fields
radius_label = Label(window, text="Enter Radius:")
radius_label.pack()
radius_entry = Entry(window)
radius_entry.pack()

diameter_label = Label(window, text="Enter Diameter:")
diameter_label.pack()
diameter_entry = Entry(window)
diameter_entry.pack()

# Create a button to trigger calculation
calculate_button = Button(window, text="Calculate Area", command=calculate_area)
calculate_button.pack()

# Create a label to display the result
result_label = Label(window, text="")
result_label.pack()

# Run the application
window.mainloop()