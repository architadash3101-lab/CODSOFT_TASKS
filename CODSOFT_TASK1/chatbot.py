import tkinter as tk
from tkinter import scrolledtext, filedialog, messagebox
import re
import random
import datetime
import ast
import operator



# =========================================================
# CODBOT - RULE-BASED CHATBOT
# CodSoft AI Internship - Task 1
# =========================================================


# ---------------------------------------------------------
# Predefined Responses
# ---------------------------------------------------------

responses = {
    "greeting": [
        "Hello! 👋 How can I help you today?",
        "Hi there! 😊 What's on your mind?",
        "Hey! Nice to see you. How can I assist?"
    ],

    "goodbye": [
        "Goodbye! Have a great day! 👋",
        "See you later! Take care!",
        "Bye! Feel free to come back anytime."
    ],

    "name": [
        "I'm CodBot, your rule-based assistant built for CodSoft Task 1! 🤖",
        "My name is CodBot. Nice to meet you!"
    ],

    "how_are_you": [
        "I'm just code, but I'm running perfectly! 😄",
        "Doing great! Thanks for asking! 😊"
    ],

    "user_fine": [
        "Glad to hear that! 😊",
        "Awesome! Let's keep the good vibes going!"
    ],

    "help": [
        "I can greet you, tell the time/date, tell jokes, "
        "answer basic questions, and perform calculations."
    ],

    "creator": [
        "I was created as part of the CodSoft Artificial Intelligence Internship - Task 1."
    ],

    "weather": [
        "I can't check live weather yet, but I hope it's sunny where you are! ☀️"
    ],

    "joke": [
        "Why don't programmers like nature? It has too many bugs! 🐛",
        "Why did the computer go to the doctor? Because it had a virus! 😷",
        "There are 10 kinds of people: those who understand binary and those who don't. 😂"
    ],

    "python": [
        "Python is a popular programming language widely used in AI, "
        "web development, automation, and data science. 🐍"
    ],

    "ai": [
        "Artificial Intelligence is the simulation of human intelligence "
        "by machines. 🤖"
    ],

    "thanks": [
        "You're welcome! 😊",
        "Happy to help! 👍",
        "Anytime! 🤖"
    ],

    "fallback": [
        "I'm not sure I understand. Could you rephrase that? 🤔",
        "I don't have a rule for that yet. Try typing 'help'!",
        "Interesting... but that's outside my rules. Ask me something else!"
    ]
}


# ---------------------------------------------------------
# Regex Pattern Matching Rules
# ---------------------------------------------------------

rules = [

    (r"\b(hi|hello|hey|hola|namaste|good morning|good evening)\b",
     "greeting"),

    (r"\b(bye|goodbye|see you|exit|quit)\b",
     "goodbye"),

    (r"\bwhat('s| is) your name\b",
     "name"),

    (r"\bwho are you\b",
     "name"),

    (r"\bhow are you\b",
     "how_are_you"),

    (r"\b(i am|i'm) (fine|good|great|okay|ok)\b",
     "user_fine"),

    (r"\b(help|what can you do|options)\b",
     "help"),

    (r"\bwho (created|made) you\b",
     "creator"),

    (r"\bweather\b",
     "weather"),

    (r"\b(joke|make me laugh|funny)\b",
     "joke"),

    (r"\bpython\b",
     "python"),

    (r"\b(ai|artificial intelligence|machine learning)\b",
     "ai"),

    (r"\b(thanks|thank you|thx)\b",
     "thanks"),

    (r"\btime\b",
     "TIME"),

    (r"\b(date|today|day)\b",
     "DATE")
]


# =========================================================
# SAFE MATHEMATICAL CALCULATOR
# =========================================================

operators = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg
}


def safe_calculate(expression):
    """
    Safely calculate basic mathematical expressions.
    """

    def evaluate(node):

        if isinstance(node, ast.Constant):

            if isinstance(node.value, (int, float)):
                return node.value

            raise ValueError("Invalid number")

        if isinstance(node, ast.BinOp):

            if type(node.op) not in operators:
                raise ValueError("Unsupported operator")

            left = evaluate(node.left)
            right = evaluate(node.right)

            return operators[type(node.op)](left, right)

        if isinstance(node, ast.UnaryOp):

            if type(node.op) not in operators:
                raise ValueError("Unsupported operator")

            return operators[type(node.op)](
                evaluate(node.operand)
            )

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")

    return evaluate(tree.body)


# =========================================================
# DETECT MATHEMATICAL EXPRESSIONS
# =========================================================

def extract_math_expression(text):

    text = text.lower().strip()

    patterns = [
        r"calculate\s+(.+)",
        r"what is\s+(.+)",
        r"solve\s+(.+)",
        r"compute\s+(.+)"
    ]

    for pattern in patterns:

        match = re.search(pattern, text)

        if match:

            expression = match.group(1)

            if re.fullmatch(
                r"[0-9+\-*/().%\s]+",
                expression
            ):
                return expression

    # Direct calculation
    if re.fullmatch(
        r"[0-9+\-*/().%\s]+",
        text
    ):
        return text

    return None


# =========================================================
# CHATBOT RESPONSE
# =========================================================

def get_response(user_input):

    text = user_input.lower().strip()

    # Check mathematics first
    expression = extract_math_expression(text)

    if expression:

        try:

            result = safe_calculate(expression)

            # Display integers without .0
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            return f"The answer is {result} 🧮"

        except ZeroDivisionError:

            return "You cannot divide by zero! ❌"

        except Exception:

            return "Sorry, I couldn't calculate that. 🤔"

    # Check normal rules
    for pattern, key in rules:

        if re.search(pattern, text):

            if key == "TIME":

                current_time = datetime.datetime.now().strftime(
                    "%I:%M %p"
                )

                return f"The current time is {current_time} 🕒"

            if key == "DATE":

                current_date = datetime.datetime.now().strftime(
                    "%A, %d %B %Y"
                )

                return f"Today's date is {current_date} 📅"

            return random.choice(responses[key])

    return random.choice(responses["fallback"])


# =========================================================
# SEND MESSAGE
# =========================================================

def send_message(event=None):

    user_input = entry.get().strip()

    if not user_input:
        return

    # Show user message
    chat_area.config(state=tk.NORMAL)

    chat_area.insert(
        tk.END,
        "You\n",
        "user_name"
    )

    chat_area.insert(
        tk.END,
        user_input + "\n\n",
        "user_message"
    )

    # Get response
    response = get_response(user_input)

    # Show bot message
    chat_area.insert(
        tk.END,
        "CodBot\n",
        "bot_name"
    )

    chat_area.insert(
        tk.END,
        response + "\n\n",
        "bot_message"
    )

    chat_area.config(state=tk.DISABLED)

    entry.delete(0, tk.END)

    chat_area.see(tk.END)

    # Exit
    if re.search(
        r"\b(bye|goodbye|exit|quit)\b",
        user_input.lower()
    ):

        root.after(
            1200,
            root.destroy
        )


# =========================================================
# CLEAR CHAT
# =========================================================

# =========================================================
# DARK / LIGHT MODE
# =========================================================

dark_mode = True


def toggle_theme():
    global dark_mode

    if dark_mode:
        # Light mode
        dark_mode = False

        root.configure(bg="#f3f4f6")
        header.configure(bg="#ffffff")
        status_frame.configure(bg="#f3f4f6")
        input_frame.configure(bg="#f3f4f6")
        button_frame.configure(bg="#f3f4f6")

        title.configure(
            bg="#ffffff",
            fg="#2563eb"
        )

        subtitle.configure(
            bg="#ffffff",
            fg="#4b5563"
        )

        status_dot.configure(
            bg="#f3f4f6"
        )

        status_label.configure(
            bg="#f3f4f6",
            fg="#4b5563"
        )

        chat_area.configure(
            bg="#ffffff",
            fg="#111827"
        )

        entry.configure(
            bg="#ffffff",
            fg="#111827",
            insertbackground="#111827"
        )

        theme_button.configure(
            text="🌙 Dark Mode",
            bg="#4b5563"
        )

    else:
        # Dark mode
        dark_mode = True

        root.configure(bg="#111827")
        header.configure(bg="#1f2937")
        status_frame.configure(bg="#111827")
        input_frame.configure(bg="#111827")
        button_frame.configure(bg="#111827")

        title.configure(
            bg="#1f2937",
            fg="#00f5d4"
        )

        subtitle.configure(
            bg="#1f2937",
            fg="#d1d5db"
        )

        status_dot.configure(
            bg="#111827"
        )

        status_label.configure(
            bg="#111827",
            fg="#9ca3af"
        )

        chat_area.configure(
            bg="#1f2937",
            fg="white"
        )

        entry.configure(
            bg="#374151",
            fg="white",
            insertbackground="white"
        )

        theme_button.configure(
            text="☀️ Light Mode",
            bg="#f59e0b"
        )


def save_chat():
    """Save the current conversation to a text file."""

    chat_content = chat_area.get("1.0", tk.END).strip()

    if not chat_content:
        messagebox.showwarning(
            "Save Chat",
            "There is no conversation to save."
        )
        return

    filename = filedialog.asksaveasfilename(
        title="Save Chat History",
        defaultextension=".txt",
        filetypes=[
            ("Text Files", "*.txt"),
            ("All Files", "*.*")
        ]
    )

    if filename:

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            file.write(chat_content)

        messagebox.showinfo(
            "Chat Saved",
            "Conversation saved successfully! 💾"
        )


def clear_chat():

    chat_area.config(state=tk.NORMAL)

    chat_area.delete(
        "1.0",
        tk.END
    )

    chat_area.insert(
        tk.END,
        "CodBot\n",
        "bot_name"
    )

    chat_area.insert(
        tk.END,
        "Chat cleared! How can I help you? 🤖\n\n",
        "bot_message"
    )

    chat_area.config(state=tk.DISABLED)

    entry.focus()


# =========================================================
# SHOW HELP
# =========================================================

def show_examples():

    examples = (
        "Try asking me:\n\n"
        "👋 hello\n"
        "🤖 what is your name?\n"
        "😊 how are you?\n"
        "😂 tell me a joke\n"
        "🕒 what time is it?\n"
        "📅 what is today's date?\n"
        "🐍 what is Python?\n"
        "🧠 what is AI?\n"
        "🧮 calculate 25 * 4\n"
        "🧮 (10 + 5) * 2\n"
        "👋 bye"
    )

    chat_area.config(state=tk.NORMAL)

    chat_area.insert(
        tk.END,
        "CodBot\n",
        "bot_name"
    )

    chat_area.insert(
        tk.END,
        examples + "\n\n",
        "bot_message"
    )

    chat_area.config(state=tk.DISABLED)

    chat_area.see(tk.END)


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "CodBot - Rule-Based AI Chatbot"
)

root.geometry(
    "760x650"
)

root.minsize(
    650,
    550
)

root.configure(
    bg="#111827"
)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg="#1f2937",
    height=90
)

header.pack(
    fill=tk.X
)

header.pack_propagate(False)


title = tk.Label(
    header,
    text="🤖 CodBot",
    font=("Arial", 24, "bold"),
    bg="#1f2937",
    fg="#00f5d4"
)

title.pack(
    pady=(12, 0)
)


subtitle = tk.Label(
    header,
    text="Rule-Based Chatbot • CodSoft AI Internship • Task 1",
    font=("Arial", 10),
    bg="#1f2937",
    fg="#d1d5db"
)

subtitle.pack()


# =========================================================
# STATUS
# =========================================================

status_frame = tk.Frame(
    root,
    bg="#111827"
)

status_frame.pack(
    fill=tk.X,
    padx=20,
    pady=(10, 0)
)


status_dot = tk.Label(
    status_frame,
    text="●",
    font=("Arial", 10),
    bg="#111827",
    fg="#22c55e"
)

status_dot.pack(
    side=tk.LEFT
)


status_label = tk.Label(
    status_frame,
    text=" Online • Ready to chat",
    font=("Arial", 10),
    bg="#111827",
    fg="#9ca3af"
)

status_label.pack(
    side=tk.LEFT
)


# =========================================================
# CHAT AREA
# =========================================================

chat_area = scrolledtext.ScrolledText(

    root,

    wrap=tk.WORD,

    font=("Arial", 11),

    bg="#1f2937",

    fg="white",

    insertbackground="white",

    relief=tk.FLAT,

    borderwidth=0,

    padx=15,

    pady=15
)

chat_area.pack(
    padx=20,
    pady=10,
    fill=tk.BOTH,
    expand=True
)


# =========================================================
# CHAT COLORS
# =========================================================

chat_area.tag_config(
    "user_name",
    foreground="#00f5d4",
    font=("Arial", 10, "bold")
)

chat_area.tag_config(
    "user_message",
    foreground="#e5e7eb",
    font=("Arial", 11)
)

chat_area.tag_config(
    "bot_name",
    foreground="#60a5fa",
    font=("Arial", 10, "bold")
)

chat_area.tag_config(
    "bot_message",
    foreground="#f3f4f6",
    font=("Arial", 11)
)


# =========================================================
# WELCOME MESSAGE
# =========================================================

chat_area.insert(
    tk.END,
    "CodBot\n",
    "bot_name"
)

chat_area.insert(
    tk.END,
    "Hello! 👋 Welcome to CodBot.\n"
    "I'm a rule-based chatbot created for CodSoft Task 1.\n"
    "Click 'Examples' to see what I can do.\n\n",
    "bot_message"
)

chat_area.config(
    state=tk.DISABLED
)


# =========================================================
# INPUT AREA
# =========================================================

input_frame = tk.Frame(
    root,
    bg="#111827"
)

input_frame.pack(
    fill=tk.X,
    padx=20,
    pady=(0, 10)
)


entry = tk.Entry(
    input_frame,
    font=("Arial", 12),
    bg="#374151",
    fg="white",
    insertbackground="white",
    relief=tk.FLAT
)

entry.pack(
    side=tk.LEFT,
    fill=tk.X,
    expand=True,
    ipady=11,
    padx=(0, 10)
)


# =========================================================
# SEND BUTTON
# =========================================================

send_button = tk.Button(
    input_frame,
    text="Send ➤",
    font=("Arial", 10, "bold"),
    bg="#00b894",
    fg="white",
    activebackground="#00a383",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=send_message
)

send_button.pack(
    side=tk.LEFT,
    ipadx=12,
    ipady=7
)


# =========================================================
# BOTTOM BUTTONS
# =========================================================

button_frame = tk.Frame(
    root,
    bg="#111827"
)

button_frame.pack(
    fill=tk.X,
    padx=20,
    pady=(0, 15)
)

save_button = tk.Button(
    button_frame,
    text="💾 Save Chat",
    font=("Arial", 10, "bold"),
    bg="#16a34a",
    fg="white",
    activebackground="#15803d",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=save_chat
)

save_button.pack(
    side=tk.LEFT,
    padx=(10, 0),
    ipadx=10,
    ipady=6
)

theme_button = tk.Button(
    button_frame,
    text="☀️ Light Mode",
    font=("Arial", 10, "bold"),
    bg="#f59e0b",
    fg="white",
    activebackground="#d97706",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=toggle_theme
)

theme_button.pack(
    side=tk.LEFT,
    padx=(10, 0),
    ipadx=10,
    ipady=6
)


examples_button = tk.Button(
    button_frame,
    text="💡 Examples",
    font=("Arial", 10, "bold"),
    bg="#2563eb",
    fg="white",
    activebackground="#1d4ed8",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=show_examples
)

examples_button.pack(
    side=tk.LEFT,
    ipadx=10,
    ipady=6
)


clear_button = tk.Button(
    button_frame,
    text="🗑 Clear Chat",
    font=("Arial", 10, "bold"),
    bg="#dc2626",
    fg="white",
    activebackground="#b91c1c",
    activeforeground="white",
    relief=tk.FLAT,
    cursor="hand2",
    command=clear_chat
)

clear_button.pack(
    side=tk.RIGHT,
    ipadx=10,
    ipady=6
)


# =========================================================
# KEYBOARD SHORTCUT
# =========================================================

entry.bind(
    "<Return>",
    send_message
)


# Put cursor in input box
entry.focus()


# =========================================================
# START APPLICATION
# =========================================================

root.mainloop()