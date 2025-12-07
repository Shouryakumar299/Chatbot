# gui.py
import customtkinter as ctk
import tkinter as tk


class AIApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("jade")
        self.geometry("900x600")
        self.configure(fg_color="black")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.build_ui()

    def build_ui(self):
        # ===================== CENTER FRAME =====================
        center_frame = ctk.CTkFrame(self, fg_color="black")
        center_frame.pack(expand=True)

        # ===================== GREETING TEXT =====================
        self.greeting = ctk.CTkLabel(
            center_frame,
            text="Hi User",
            font=("Segoe UI", 36, "bold"),
            text_color="white"
        )
        self.greeting.pack(pady=(0, 25))

        # ===================== GRADIENT ICON (NO IMAGES) =====================
        self.icon_size = 70
        icon_canvas = tk.Canvas(center_frame,
                                width=self.icon_size,
                                height=self.icon_size,
                                bg="black",
                                highlightthickness=0)
        icon_canvas.pack(pady=(0, 20))
        self.draw_gradient_diamond(icon_canvas, self.icon_size)

        # ===================== DROP SHADOW =====================
        shadow = ctk.CTkFrame(center_frame, width=710, height=100, fg_color="#070707", corner_radius=40)
        shadow.place(relx=0.5, rely=0.46, anchor="center", y=6)
        shadow.pack_propagate(False)

        # ===================== SEARCH BOX =====================
        search_frame = ctk.CTkFrame(
            center_frame,
            width=700,
            height=90,
            fg_color="#1F1F1F",
            corner_radius=40
        )
        search_frame.pack()
        search_frame.pack_propagate(False)

        # ===================== INNER SEARCH ROW =====================
        row = ctk.CTkFrame(search_frame, fg_color="transparent")
        row.pack(fill="x", padx=25, pady=20)

        entry_label = ctk.CTkLabel(
            row,
            text="Ask AI...",
            font=("Segoe UI", 18),
            text_color="#9E9E9E"
        )
        entry_label.pack(side="left")

        row_spacer = ctk.CTkLabel(row, text="", fg_color="transparent")
        row_spacer.pack(side="left", expand=True)

        # ===================== MODE SWITCHER =====================
        self.mode_var = ctk.StringVar(value="Balanced")
        mode_switch = ctk.CTkSegmentedButton(
            row,
            values=["Fast", "Balanced", "Detailed"],
            variable=self.mode_var,
            fg_color="#2A2A2A"
        )
        mode_switch.pack(side="right", padx=10)

        # ===================== MICROPHONE BUTTON =====================
        mic_btn = ctk.CTkButton(
            row,
            width=40,
            height=40,
            corner_radius=20,
            fg_color="#2E2E2E",
            text="🎤",
            command=self.on_mic_click
        )
        mic_btn.pack(side="right")

        # ===================== CHAT WINDOW =====================
        chat_frame = ctk.CTkFrame(self, fg_color="black")
        chat_frame.pack(fill="both", expand=True, pady=20)

        self.chatbox = ctk.CTkTextbox(
            chat_frame, fg_color="#0E0E0E", text_color="white",
            font=("Segoe UI", 15)
        )
        self.chatbox.pack(fill="both", expand=True, padx=30, pady=10)

        # ===================== USER INPUT BAR =====================
        input_frame = ctk.CTkFrame(self, fg_color="black")
        input_frame.pack(fill="x", padx=20, pady=10)

        self.user_entry = ctk.CTkEntry(
            input_frame,
            placeholder_text="Type your message...",
            height=45,
            font=("Segoe UI", 16),
            fg_color="#1A1A1A"
        )
        self.user_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))

        send_btn = ctk.CTkButton(
            input_frame,
            text="Send",
            width=90,
            command=self.send_message
        )
        send_btn.pack(side="right")

    # ===================== GRADIENT ICON DRAW =====================
    def draw_gradient_diamond(self, canvas, size):
        cx = cy = size / 2
        corners = [(cx, 0), (size, cy), (cx, size), (0, cy)]
        colors = [(56, 189, 248), (168, 85, 247), (245, 158, 11)]
        steps = 28

        for i in range(steps, 0, -1):
            t = i / steps
            pts = []
            for (x, y) in corners:
                pts.extend([cx + (x - cx) * t, cy + (y - cy) * t])

            color = self.interpolate_colors(colors, t)
            color_hex = "#%02x%02x%02x" % color
            canvas.create_polygon(pts, fill=color_hex, outline="")

    def interpolate_colors(self, stops, t):
        t = max(0.0, min(1.0, t))
        n = len(stops) - 1
        pos = t * n
        idx = int(pos)
        frac = pos - idx
        if idx >= n:
            return stops[-1]
        c1, c2 = stops[idx], stops[idx + 1]
        return (
            int(c1[0] + (c2[0] - c1[0]) * frac),
            int(c1[1] + (c2[1] - c1[1]) * frac),
            int(c1[2] + (c2[2] - c1[2]) * frac)
        )

    # ===================== SEND MESSAGE FUNCTION =====================
    def send_message(self):
        user_text = self.user_entry.get().strip()
        if not user_text:
            return

        # Hide greeting when first message is sent
        if self.greeting.winfo_ismapped():
            self.greeting.pack_forget()

        # Show user's message in chat
        self.add_message("You", user_text)

        self.user_entry.delete(0, "end")

        # Temporary AI reply (replace later with real API)
        self.add_message("AI", "Thinking...")

    # ===================== CHATBOX HELPER =====================
    def add_message(self, sender, text):
        self.chatbox.insert("end", f"{sender}: ", "sender")
        self.chatbox.insert("end", f"{text}\n\n")

        self.chatbox.tag_config(
            "sender",
            foreground="#00A8FF",
            font=("Segoe UI", 15, "bold")
        )

    # ===================== MIC CLICK =====================
    def on_mic_click(self):
        print("Mic clicked — add speech later!")


# ===================== RUN =====================
if __name__ == "__main__":
    app = AIApp()
    app.mainloop()
