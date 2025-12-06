# gui.py
import customtkinter as ctk


class AIApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("jade")
        self.geometry("900x600")
        self.configure(fg_color="black")  # Full black background

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.build_ui()

    def build_ui(self):

        # ========== CENTER FRAME ==========
        center_frame = ctk.CTkFrame(self, fg_color="black")
        center_frame.pack(expand=True)  # perfectly center

        # ========== GREETING TEXT ==========
        greeting = ctk.CTkLabel(
            center_frame,
            text="Hi User",
            font=("Segoe UI", 36, "bold"),
            text_color="white"
        )
        greeting.pack(pady=(0, 40))

        # ========== SEARCH BOX ==========
        search_frame = ctk.CTkFrame(
            center_frame,
            width=700,
            height=90,
            fg_color="#1F1F1F",
            corner_radius=40   
        )
        search_frame.pack()

        # To make CTkFrame respect custom size
        search_frame.pack_propagate(False)

        # Inside search area
        row = ctk.CTkFrame(search_frame, fg_color="transparent")
        row.pack(fill="x", padx=25, pady=20)

        # Placeholder prompt text
        entry_label = ctk.CTkLabel(
            row,
            text="Ask AI...",
            font=("Segoe UI", 18),
            text_color="#9E9E9E"
        )
        entry_label.pack(side="left")

        # Spacer so icons align right
        row_spacer = ctk.CTkLabel(row, text="", fg_color="transparent")
        row_spacer.pack(side="left", expand=True)




# Run GUI only
if __name__ == "__main__":
    app = AIApp()
    app.mainloop()
