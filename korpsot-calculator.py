import random
import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style

# This is the main class for the Linear Equation Solver GUI
class KorpsotLinearEquationSolver:
    def __init__(self, root):
        # Set up custom theme
        self.style = Style(theme='cyborg')
        self.primary_color = "#22C55E"

        # Customize button style
        self.style.configure('primary.TButton', background=self.primary_color, foreground="#fafafa",
                             focuscolor=[('!focus', 'none')],
                             bordercolor=[('focus', self.primary_color), ('!focus', self.primary_color)])
        # Customize label style
        self.style.configure('primary.TLabel', foreground=self.primary_color)
        # Button color when hovered or clicked
        self.style.map('primary.TButton', background=[('active', '#16A085')])

        # Set up main window
        self.root = root
        self.root.title("Korpsot Linear Equation Solver")
        self.root.geometry("650x1080")

        # Graph canvas setup
        self.canvas_width = 600
        self.canvas_height = 500
        self.scale = 20  # 1 unit = 20 pixels
        self.center_x = self.canvas_width // 2
        self.center_y = self.canvas_height // 2

        # Layout frames
        main_frame = ttk.Frame(self.root, padding=20)
        main_frame.pack(expand=True)

        # Title text
        title_label = ttk.Label(main_frame, text="Linear Equation Solver",
                                font=('Arial', 18, 'bold'), style='primary.TLabel')
        title_label.pack(pady=(0, 10))

        # Input section for the equation
        input_frame = ttk.Frame(main_frame)
        input_frame.pack(pady=(0, 30))

        # Equation input: y = mx + c
        eq_frame = ttk.Frame(input_frame)
        eq_frame.pack(pady=(0, 20))

        eq_label = ttk.Label(eq_frame, text="y =", font=('Arial', 16))
        eq_label.pack(side="left", padx=(0, 10))

        self.m_var = tk.StringVar(value="2")
        m_entry = ttk.Entry(eq_frame, textvariable=self.m_var, width=8, font=('Arial', 14), justify="center")
        m_entry.pack(side="left", padx=2)

        x_label = ttk.Label(eq_frame, text="x +", font=('Arial', 16))
        x_label.pack(side="left", padx=(5, 10))

        self.c_var = tk.StringVar(value="3")
        c_entry = ttk.Entry(eq_frame, textvariable=self.c_var, width=8, font=('Arial', 14), justify="center")
        c_entry.pack(side="left", padx=2)

        # Input for target y value
        y_frame = ttk.Frame(input_frame)
        y_frame.pack(pady=(10, 0))

        y_label = ttk.Label(y_frame, text="Solve for x when y =", font=('Arial', 14))
        y_label.pack(side="left", padx=(0, 10))

        self.y_var = tk.StringVar(value="7")
        y_entry = ttk.Entry(y_frame, textvariable=self.y_var, width=10, font=('Arial', 14), justify="center")
        y_entry.pack(side="left", padx=5)

        # Buttons: solve, load example, clear
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(pady=(20, 30))

        solve_btn = ttk.Button(button_frame, text="Solve for x", command=self.solve_equation,
                               style='primary.TButton', width=12)
        solve_btn.pack(side="left", padx=(0, 10))

        example_btn = ttk.Button(button_frame, text="Example", command=self.load_example, width=12)
        example_btn.pack(side="left", padx=(0, 10))

        clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_all, width=12, bootstyle="danger-outline")
        clear_btn.pack(side="left")

        # Result box
        results_frame = ttk.LabelFrame(main_frame, text="Solution", padding=5)
        results_frame.pack(fill="both", expand=True, pady=(10, 0))

        self.results_text = tk.Text(results_frame, height=5, width=70, font=('Courier', 11),
                                    wrap="word", bg='#2a2d3a', fg='#ffffff', insertbackground='#ffffff',
                                    state="disabled")
        self.results_text.pack(fill="both", expand=True)

        # Graph section
        graph_title = ttk.Label(main_frame, text="Display Graph",
                                font=('Arial', 14, 'bold'), style='primary.TLabel')
        graph_title.pack(pady=(5, 10))

        self.graph_canvas = tk.Canvas(main_frame, width=self.canvas_width, height=self.canvas_height,
                                      bg="#333333", relief="sunken", borderwidth=2)
        self.graph_canvas.pack(pady=(0, 10))

        self.draw_x_y_lines()
        self.solve_equation()

    def solve_equation(self):
        try:
            # Read values from input
            m = float(self.m_var.get())
            c = float(self.c_var.get())
            y = float(self.y_var.get())

            # Just a sanity check for slope, not really necessary
            if abs(m) < 0:
                self.display_error("Error: Slope (m) cannot be zero!\nThe equation would not be linear in x.")
                return

            # Basic math to get x from y
            x = (y - c) / m
            self.display_results(m, c, y, x)

        except ValueError:
            # If inputs aren't valid numbers
            self.display_error("Error! Please enter valid numbers for all fields.")
        except Exception as e:
            # Any other error
            self.display_error(f"Error! {str(e)}.")

    def display_results(self, m, c, y, x):
        # Show solution in the text box
        self.results_text.config(state="normal")
        self.results_text.delete(1.0, tk.END)

        self.results_text.insert(tk.END, "Solving for x:\n")
        self.results_text.insert(tk.END, f"Given: y = {y:g}\n")
        self.results_text.insert(tk.END, "-" * 40 + "\n")
        self.results_text.insert(tk.END, "Solution:\n")
        self.results_text.insert(tk.END, f"x = {x:0.2f}\n\n")

        # Quick error check (should be 0)
        y_check = m * x + c
        error = abs(y_check - y)
        self.results_text.insert(tk.END, f"Error: {error:0.2f}\n")
        self.results_text.config(state="disabled")

        # Draw line from two far y-values to get a full line in view
        y0 = -self.canvas_height
        x0 = (y0 - c) / m
        y1 = self.canvas_height
        x1 = (y1 - c) / m

        self.draw_display_line(x0, y0, x1, y1)

    def display_error(self, message):
        # Show error in results box and popup
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, message)
        messagebox.showerror("Input Error", message)

    def clear_all(self):
        # Clear input fields and output box
        self.m_var.set("")
        self.c_var.set("")
        self.y_var.set("")
        self.results_text.delete(1.0, tk.END)

    def draw_x_y_lines(self):
        # Draw x and y axis lines
        self.graph_canvas.create_line(0, self.center_y, self.canvas_width, self.center_y,
                                      fill="gray", width=1)
        self.graph_canvas.create_line(self.center_x, 0, self.center_x, self.canvas_height,
                                      fill="gray", width=1)

        # Label x and y axis
        self.graph_canvas.create_text(self.canvas_width - 15, self.center_y + 15, text="X",
                                      font=("Arial", 12, "bold"))
        self.graph_canvas.create_text(self.center_x - 15, 15, text="Y",
                                      font=("Arial", 12, "bold"))

    def draw_display_line(self, x0, y0, x1, y1):
        # Clear previous drawings
        self.graph_canvas.delete("all")

        # Redraw axis
        self.draw_x_y_lines()

        # Draw the calculated line
        self.graph_canvas.create_line(self.math_to_canvas(x0, y0), self.math_to_canvas(x1, y1),
                                      fill="#22C55E", width=3)

    def math_to_canvas(self, math_x, math_y):
        # Convert math coordinates to canvas pixels
        canvas_x = self.center_x + (math_x * self.scale)
        canvas_y = self.center_y - (math_y * self.scale)
        return canvas_x, canvas_y

    def load_example(self):
        # Fill in random values for testing
        random_m = random.randint(1, 20)
        random_c = random.randint(1, 20)
        random_y = random.randint(1, 20)
        self.m_var.set(f"{random_m}")
        self.c_var.set(f"{random_c}")
        self.y_var.set(f"{random_y}")
        self.solve_equation()


# Start the app
root = ttk.Window(themename='cyborg')
mainApp = KorpsotLinearEquationSolver(root)
root.mainloop()
