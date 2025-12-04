from tkinter import ttk
import tkinter as tk

# Color Palette
# Replaced PASTEL_GREEN with PASTEL_YELLOW
PASTEL_YELLOW_BG = "#FFF9C4"      # Light yellow background
PASTEL_YELLOW_ACCENT = "#FFF176"  # Stronger yellow for headers/active
PASTEL_YELLOW_FG = "#333333"      # Dark gray text for better contrast on yellow (originally was dark green)

PASTEL_ORANGE_BG = "#FFF3E0"      # Light orange background (Inventory)
PASTEL_ORANGE_ACCENT = "#FFCC80"  # Stronger orange
PASTEL_ORANGE_FG = "#E65100"      # Dark orange text

DEFAULT_FONT = ("Segoe UI", 10)
LARGE_FONT = ("Segoe UI", 14)
TOUCH_PADDING = 10
NORMAL_PADDING = 2

class StyleManager:
    def __init__(self, root, touch_mode=False):
        self.root = root
        self.touch_mode = touch_mode
        self.style = ttk.Style(root)
        self.apply_theme()

    def set_touch_mode(self, enabled):
        self.touch_mode = enabled
        self.apply_theme()

    def apply_theme(self):
        self.style.theme_use('clam')

        # Dimensions based on touch mode
        base_font_size = 14 if self.touch_mode else 10
        base_padding = TOUCH_PADDING if self.touch_mode else NORMAL_PADDING
        row_height = 40 if self.touch_mode else 25

        base_font = ("Segoe UI", base_font_size)
        bold_font = ("Segoe UI", base_font_size, "bold")

        # --- GENERAL STYLES (Yellow Theme) ---
        self.style.configure(".",
                             background=PASTEL_YELLOW_BG,
                             foreground=PASTEL_YELLOW_FG,
                             font=base_font)

        self.style.configure("TLabel", background=PASTEL_YELLOW_BG, foreground=PASTEL_YELLOW_FG)
        self.style.configure("TButton", background=PASTEL_YELLOW_ACCENT, padding=base_padding)
        self.style.configure("TEntry", fieldbackground="white", padding=base_padding)
        self.style.configure("TCombobox", padding=base_padding)

        # Notebook
        self.style.configure("TNotebook", background=PASTEL_YELLOW_BG)
        self.style.configure("TNotebook.Tab",
                             padding=[base_padding*2, base_padding],
                             font=bold_font,
                             background=PASTEL_YELLOW_ACCENT)
        self.style.map("TNotebook.Tab", background=[("selected", PASTEL_YELLOW_BG)])

        # Treeview
        self.style.configure("Treeview",
                             background="white",
                             fieldbackground="white",
                             foreground="black",
                             rowheight=row_height,
                             font=base_font)
        self.style.configure("Treeview.Heading",
                             background=PASTEL_YELLOW_ACCENT,
                             font=bold_font,
                             padding=base_padding)

        # LabelFrame
        self.style.configure("TLabelframe", background=PASTEL_YELLOW_BG, foreground=PASTEL_YELLOW_FG)
        self.style.configure("TLabelframe.Label", background=PASTEL_YELLOW_BG, foreground=PASTEL_YELLOW_FG, font=bold_font)

        # --- SPECIAL STYLES ---

        # Inventory (Orange Theme)
        self.style.configure("Inventory.TFrame", background=PASTEL_ORANGE_BG)
        self.style.configure("Inventory.TLabel", background=PASTEL_ORANGE_BG, foreground=PASTEL_ORANGE_FG)
        self.style.configure("Inventory.TLabelframe", background=PASTEL_ORANGE_BG, foreground=PASTEL_ORANGE_FG)
        self.style.configure("Inventory.TLabelframe.Label", background=PASTEL_ORANGE_BG, foreground=PASTEL_ORANGE_FG, font=bold_font)

        # Sales (Yellow Theme - Default, but explicit)
        self.style.configure("Sales.TFrame", background=PASTEL_YELLOW_BG)

        # Buttons
        # Adjusted colors to fit yellow theme, using slightly darker yellow/orange for accent buttons to stand out
        self.style.configure("Accent.TButton", background="#FDD835", foreground="#333", font=bold_font) # Yellow 600
        self.style.map("Accent.TButton", background=[("active", "#FBC02D")]) # Yellow 700

        self.style.configure("Danger.TButton", background="#EF5350", foreground="white", font=bold_font)
        self.style.map("Danger.TButton", background=[("active", "#D32F2F")])
