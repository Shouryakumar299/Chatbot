# ===================== USER INPUT AREA =====================
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
