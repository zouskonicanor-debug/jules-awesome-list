import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("SmartFarm C2")
root.geometry("1200x800")

# --- Configure the main window's grid layout ---
root.rowconfigure(0, weight=3)
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=3)
root.columnconfigure(1, weight=1)

# --- Create the main frames for the layout ---
map_frame = tk.Frame(root, bg="darkgrey")
right_panel_frame = tk.Frame(root, bg="#333333")
log_frame = tk.Frame(root, bg="black")

# --- Place the main frames in the root window's grid ---
map_frame.grid(row=0, column=0, sticky="nsew")
right_panel_frame.grid(row=0, column=1, sticky="nsew")
log_frame.grid(row=1, column=0, columnspan=2, sticky="nsew")

# --- Subdivide the right panel frame ---
right_panel_frame.rowconfigure(0, weight=1)
right_panel_frame.rowconfigure(1, weight=1)
right_panel_frame.columnconfigure(0, weight=1)

status_frame = tk.Frame(right_panel_frame, bg="#222222", highlightbackground="grey", highlightthickness=1)
mission_frame = tk.Frame(right_panel_frame, bg="#222222", highlightbackground="grey", highlightthickness=1)

status_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=5)
mission_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=5)

# --- Populate Widgets ---

# 1. Map Frame
map_label = tk.Label(map_frame, text="Map / Video Feed Placeholder", fg="white", bg=map_frame.cget("bg"), font=("TkDefaultFont", 16))
map_label.pack(expand=True)

# 2. Status Frame
status_title = tk.Label(status_frame, text="--- DRONE STATUS ---", fg="cyan", bg=status_frame.cget("bg"), font=("TkDefaultFont", 14, "bold"))
status_title.pack(pady=10)

status_grid = tk.Frame(status_frame, bg=status_frame.cget("bg"))
status_grid.pack(padx=10, pady=10, fill="x")
status_grid.columnconfigure(1, weight=1)

status_data = {"BATTERY:": "98%", "GPS:": "3D FIX", "ALTITUDE:": "15m", "SPEED:": "5 m/s"}
for i, (key, value) in enumerate(status_data.items()):
    label = tk.Label(status_grid, text=key, fg="white", bg=status_grid.cget("bg"), font=("TkDefaultFont", 10))
    label.grid(row=i, column=0, sticky="w", padx=5, pady=3)
    data_label = tk.Label(status_grid, text=value, fg="lime", bg=status_grid.cget("bg"), font=("TkDefaultFont", 10, "bold"))
    data_label.grid(row=i, column=1, sticky="e", padx=5, pady=3)

# 3. Mission Frame
mission_title = tk.Label(mission_frame, text="--- MISSION INFO ---", fg="orange", bg=mission_frame.cget("bg"), font=("TkDefaultFont", 14, "bold"))
mission_title.pack(pady=10)

mission_grid = tk.Frame(mission_frame, bg=mission_frame.cget("bg"))
mission_grid.pack(padx=10, pady=10, fill="x")
mission_grid.columnconfigure(1, weight=1)

mission_data = {"TASK:": "Spraying Sector 4B", "AREA:": "1.2 / 5.8 Ha", "SPRAYER:": "78%"}
for i, (key, value) in enumerate(mission_data.items()):
    label = tk.Label(mission_grid, text=key, fg="white", bg=mission_grid.cget("bg"), font=("TkDefaultFont", 10))
    label.grid(row=i, column=0, sticky="w", padx=5, pady=3)
    data_label = tk.Label(mission_grid, text=value, fg="lime", bg=mission_grid.cget("bg"), font=("TkDefaultFont", 10, "bold"))
    data_label.grid(row=i, column=1, sticky="e", padx=5, pady=3)

# 4. Log Frame
log_widget = tk.Text(log_frame, height=10, bg="black", fg="#00FF00", relief="flat", font=("Monospace", 9))
log_widget.pack(expand=True, fill="both", padx=5, pady=5)
log_widget.insert(tk.END, "15:32:01 - System Initialized\n")
log_widget.insert(tk.END, "15:32:05 - GPS Lock Acquired\n")
log_widget.insert(tk.END, "15:32:10 - Ready for mission start.\n")
log_widget.config(state="disabled")

# Start the main event loop
root.mainloop()
