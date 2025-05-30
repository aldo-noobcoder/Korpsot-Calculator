# Installation Guide
If you dont have either Python, Tkinter, or Ttkbootstrap installed refer to the installation guide below:
### Windows 10/11 🪟
1. Install Python:
   - Download from https://www.python.org/downloads/windows/
   - Run the installer.
   - Check "Add Python to PATH".
   - Click "Install Now".

2. Verify Tkinter:
   - Open Command Prompt.
   - Run: `python -m tkinter`
   - A small window should appear.

3. Install ttkbootstrap:
   - Run: `pip install ttkbootstrap`

### MacOs 🍎

1. Install Python:
   - Download from https://www.python.org/downloads/macos/
   - Run the installer.

2. Verify Tkinter:
   - Open Terminal.
   - Run: `python3 -m tkinter`
   - A small window should appear.

3. Install ttkbootstrap:
   - Run: `pip3 install ttkbootstrap`

### Linux (Ubuntu/Debian) 🐧
1. Install Python:
   - Open Terminal.
   - Run:
				 sudo apt update
			    sudo apt install python3 python3-pip

2. Install Tkinter:
   - Run: `sudo apt install python3-tk`

3. Verify Tkinter:
   - Run: `python3 -m tkinter`
   - A small window should appear.

4. Install ttkbootstrap:
   - Run: `pip3 install ttkbootstrap`

### Test Installation

1. Create a file named test_gui.py with the following content:

		import ttkbootstrap as ttk

	   root = ttk.Window(themename="superhero")
	   ttk.Label(root, text="Hello, World!", bootstyle="info").pack(padx=10, pady=10)
	   root.mainloop()

2. Run the script:
   - On Windows: `python test_gui.py`
   - On macOS/Linux: `python3 test_gui.py`
   - A window with a styled label should appear.
  
# 🚀 About
This project was created by me as a school project. The Korpsot Calculator is a simple linear algebra calculator like for solving x against y = mx + c.

It also provides a intuitive visual way to see how the linear algebra function looks on a 
2d graph using the inbuilt Tkinter canvas 

# 📝 How To Build
	# Open a terminal (Command Prompt or PowerShell for Windows, Terminal for macOS or Linux)

    # Ensure Git is installed
    # Visit https://git-scm.com to download and install console Git if 		not already installed

	# Clone the repository
    git clone https://github.com/aldo-noobcoder/Korpsot-Calculator.git
    
    # Make sure python tkinter and ttkbootstrap are installed
    python korpsot-calculator.py
 
# 🛠️ Usage
This picture contains the full window of the Korpsot solver

![Korpsot Preview Picture](https://files.catbox.moe/mrj5ct.png)
to calculate your x when y is defined, input your y = mx + c in the first 2 inputs to define your m and c variables then solve x when y is inputted. Then, click the "Solve for x button" the solution for x should display in the "solution" display frame. 

Video preview available [here](https://files.catbox.moe/mfww5c.mp4)

### Reset Inputs
To reset your input just click the red button that says "Clear", it should empty every input.


### Randomize Input
To randomize random variables just click the blue button that says "Example" it should randomize the m, c, and y variables the min is 1 and the max is 20.

hi sir if u are reading this 
