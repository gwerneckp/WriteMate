import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from writemate import WriteMate
from threading import Thread
from time import sleep


class WriteMateGUI:
    def __init__(self, master):
        self.master = master
        master.title("WriteMate GUI")

        # Create a label and text box for the text to be typed
        self.text_label = tk.Label(master, text="Text:")
        self.text_label.pack()

        self.text_scroll = tk.Scrollbar(master)
        self.text_box = tk.Text(
            master, width=40, height=10, wrap="word", yscrollcommand=self.text_scroll.set)
        self.text_scroll.config(command=self.text_box.yview)
        self.text_scroll.pack(side="right", fill="y")
        self.text_box.pack(side="left", fill="both", expand=True)

        # Create a label and slider for the typing speed
        self.speed_label = tk.Label(
            master, text="Typing speed: (base delay per letter)")
        self.speed_label.pack()
        self.speed_slider = tk.Scale(
            master, from_=0.01, to=2.0, resolution=0.1, length=300, orient=tk.HORIZONTAL)
        self.speed_slider.set(0.5)

        def update_speed(e):
            self.wm.speed = e.widget.get()
        self.speed_slider.bind("<ButtonRelease-1>", lambda e: update_speed(e))
        self.speed_slider.pack()

        # Create a label and slider for the typo rate
        self.typo_label = tk.Label(master, text="Typo rate:")
        self.typo_label.pack()
        self.typo_slider = tk.Scale(
            master, from_=0.1, to=1.0, resolution=0.05, length=300, orient=tk.HORIZONTAL)
        self.typo_slider.set(0.05)

        def update_typo_rate(e):
            self.wm.typo_rate = e.widget.get()
        self.typo_slider.bind("<ButtonRelease-1>", lambda e: update_typo_rate)
        self.typo_slider.pack()

        # Create a label and slider for the pause rate
        self.pause_label = tk.Label(master, text="Pause rate:")
        self.pause_label.pack()
        self.pause_slider = tk.Scale(
            master, from_=0.0, to=1.0, resolution=0.05, length=300, orient=tk.HORIZONTAL)
        self.pause_slider.set(0.05)

        def update_pause_rate(e):
            self.wm.pause_rate = e.widget.get()
        self.pause_slider.bind("<ButtonRelease-1>",
                               lambda e: update_pause_rate)

        self.pause_slider.pack()

        # Create a button to start typing
        def start_typing():
            # Create a function to wait 3 seconds and then start typing
            def wait_and_start():
                sleep(3)
                self.type_text()

            # Create a thread to run the typing process and give it a name
            self.thread = Thread(target=wait_and_start, name="type_text")
            self.thread.start()

        self.type_button = tk.Button(
            # start a thread to run the typing process
            master, text="Type", command=start_typing)
        self.type_button.pack()

        # Create a button to copy the output_text to the main text box
        def move():
            self.text_box.delete("1.0", tk.END)
            self.text_box.insert(tk.END, self.output_text.get("1.0", tk.END))
        self.copy_button = tk.Button(
            master, text="Move to main", command=move)
        self.copy_button.pack()

        # Create a scrolling text area to display the typing output
        self.output_text = scrolledtext.ScrolledText(
            master, width=40, height=10)
        self.output_text.pack()

        # Create a thread to run the typing process
        self.thread = None
        self.running = False

    def type_text(self):
        # Get the text from the text box
        text = self.text_box.get("1.0", tk.END).strip()

        # Get the values from the sliders
        speed = self.speed_slider.get()
        typo_rate = self.typo_slider.get()
        pause_rate = self.pause_slider.get()

        # Create a WriteMate instance and type the text
        self.wm = WriteMate(text=text, speed=speed,
                            typo_rate=typo_rate, pause_rate=pause_rate)
        # Update output_text to ' '.join(wm.words)

        def update_output_text():
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, ' '.join(self.wm.words))
        self.wm.set_before_typing_word(update_output_text)
        self.wm.type_text()

        # Display the typing output in the scrolling text area
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, self.wm.original_text)
        self.output_text.insert(tk.END, "\n\n")
        self.output_text.insert(tk.END, self.wm.output_text)


root = tk.Tk()
# Set the theme
root.tk.call('source', 'style/azure.tcl')
root.tk.call('set_theme', 'dark')
app = WriteMateGUI(root)
root.mainloop()
