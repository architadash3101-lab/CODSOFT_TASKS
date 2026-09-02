import tkinter as tk
from tkinter import scrolledtext
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

    (r"\btime\b",
     "TIME"),

    (r"\b(date|today|day)\b",
     "DATE")
]


# ---------------------------------------------------------
# Safe Mathematical Calculator
# ---------------------------------------------------------

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

    Supported:
    + addition
    - subtraction
    * multiplication
    / division
    % modulus
    ** power
    () brackets
    """

    def evaluate(node):

        # Numbers
        if isinstance(node, ast.Constant):

            if isinstance(node.value, (int, float)):
                return node.value

            raise ValueError("Invalid number")

        # Binary operations
        if isinstance(node, ast.BinOp):

            if type(node.op) not in operators:
                raise ValueError("Unsupported operator")

            left = evaluate(node.left)
            right = evaluate(node.right)

            return operators[type(node.op)](left, right)

        # Negative numbers
        if isinstance(node, ast.UnaryOp):

            if type(node.op) not in operators:
                raise ValueError("Unsupported operator")

            return operators[type(node.op)](
                evaluate(node.operand)
            )

        raise ValueError("Invalid expression")

    tree = ast.parse(expression, mode="eval")

    return evaluate(tree.body)


# ---------------------------------------------------------
# Detect Mathematical Expressions
# ---------------------------------------------------------

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

            # Only allow mathematical characters
            if re.fullmatch(
                r"[0-9+\-*/().%\s]+",
                expression
            ):

                return expression

    # Direct mathematical expression
    if re.fullmatch(
        r"[0-9+\-*/().%\s]+",
        text
    ):

        return text

    return None


# ---------------------------------------------------------
# Generate Chatbot Response
# ---------------------------------------------------------

def get_response(user_input):

    text = user_input.lower().strip()

    # Check for mathematical expressions
    expression = extract_math_expression(text)

    if expression:

        try:

            result = safe_calculate(expression)

            return f"The answer is {result} 🧮"

        except ZeroDivisionError:

            return "You cannot divide by zero! ❌"

        except Exception:

            return "Sorry, I couldn't calculate that. 🤔"

    # Check normal chatbot rules
    for pattern, key in rules:

        if re.search(pattern, text):

            # Dynamic time response
            if key == "TIME":

                current_time = datetime.datetime.now().strftime(
                    "%I:%M %p"
                )

                return f"The current time is {current_time} 🕒"

            # Dynamic date response
            if key == "DATE":

                current_date = datetime.datetime.now().strftime(
                    "%A, %d %B %Y"
                )

                return f"Today's date is {current_date} 📅"

            return random.choice(responses[key])

    # Fallback response
    return random.choice(responses["fallback"])


# =========================================================
# GUI FUNCTIONS
# =========================================================


def send_message(event=None):

    user_input = entry.get().strip()

    # Don't send empty messages
    if not user_input:
        return

    # Enable chat area
    chat_area.config(state=tk.NORMAL)

    # Display user's message
    chat_area.insert(
        tk.END,
        "You: " + user_input + "\n",
        "user"
    )

    # Get chatbot response
    response = get_response(user_input)

    # Display chatbot response
    chat_area.insert(
        tk.END,
        "CodBot: " + response + "\n\n",
        "bot"
    )

    # Disable editing
    chat_area.config(state=tk.DISABLED)

    # Clear input box
    entry.delete(0, tk.END)

    # Scroll to latest message
    chat_area.see(tk.END)

    # Exit chatbot
    if re.search(
        r"\b(bye|goodbye|exit|quit)\b",
        user_input.lower()
    ):

        root.after(
            1000,
            root.destroy
        )


def clear_chat():

    chat_area.config(state=tk.NORMAL)

    chat_area.delete(
        "1.0",
        tk.END
    )

    chat_area.insert(
        tk.END,
        "CodBot: Chat cleared! How can I help you? 🤖\n\n",
        "bot"
    )

    chat_area.config(state=tk.DISABLED)


# =========================================================
# CREATE GUI WINDOW
# =========================================================


root = tk.Tk()

root.title(
    "CodBot - Rule-Based Chatbot"
)

root.geometry(
    "700x600"
)

root.configure(
    bg="#1e1e2f"
)


# ---------------------------------------------------------
# Title
# ---------------------------------------------------------

title_label = tk.Label(

    root,

    text="🤖 CodBot",

    font=(
        "Arial",
        24,
        "bold"
    ),

    bg="#1e1e2f",

    fg="#00ffcc"
)

title_label.pack(
    pady=(15, 5)
)


# ---------------------------------------------------------
# Subtitle
# ---------------------------------------------------------

subtitle_label = tk.Label(

    root,

    text="Rule-Based Chatbot | CodSoft AI Internship Task 1",

    font=(
        "Arial",
        11
    ),

    bg="#1e1e2f",

    fg="white"
)

subtitle_label.pack(
    pady=(0, 10)
)


# ---------------------------------------------------------
# Chat Area
# ---------------------------------------------------------

chat_area = scrolledtext.ScrolledText(

    root,

    wrap=tk.WORD,

    font=(
        "Arial",
        12
    ),

    bg="#252538",

    fg="white",

    insertbackground="white",

    height=20
)

chat_area.pack(

    padx=20,

    pady=10,

    fill=tk.BOTH,

    expand=True
)


# ---------------------------------------------------------
# Message Colors
# ---------------------------------------------------------

chat_area.tag_config(

    "user",

    foreground="#00ffcc"
)


chat_area.tag_config(

    "bot",

    foreground="#ffffff"
)


# ---------------------------------------------------------
# Welcome Message
# ---------------------------------------------------------

chat_area.insert(

    tk.END,

    "CodBot: Hello! 👋 I'm CodBot.\n"
    "Type 'help' to see what I can do.\n\n",

    "bot"
)


chat_area.config(
    state=tk.DISABLED
)


# =========================================================
# INPUT SECTION
# =========================================================


input_frame = tk.Frame(

    root,

    bg="#1e1e2f"
)

input_frame.pack(

    fill=tk.X,

    padx=20,

    pady=10
)


# ---------------------------------------------------------
# Input Box
# ---------------------------------------------------------

entry = tk.Entry(

    input_frame,

    font=(
        "Arial",
        13
    ),

    bg="white",

    fg="black"
)

entry.pack(

    side=tk.LEFT,

    fill=tk.X,

    expand=True,

    ipady=10
)


# ---------------------------------------------------------
# Send Button
# ---------------------------------------------------------

send_button = tk.Button(

    input_frame,

    text="Send",

    font=(
        "Arial",
        11,
        "bold"
    ),

    bg="#00b894",

    fg="white",

    command=send_message
)

send_button.pack(

    side=tk.LEFT,

    padx=(10, 0),

    ipadx=15,

    ipady=7
)


# ---------------------------------------------------------
# Clear Button
# ---------------------------------------------------------

clear_button = tk.Button(

    input_frame,

    text="Clear",

    font=(
        "Arial",
        11,
        "bold"
    ),

    bg="#d63031",

    fg="white",

    command=clear_chat
)

clear_button.pack(

    side=tk.LEFT,

    padx=(10, 0),

    ipadx=15,

    ipady=7
)


# ---------------------------------------------------------
# Press Enter to Send
# ---------------------------------------------------------

entry.bind(
    "<Return>",
    send_message
)


# =========================================================
# START CHATBOT
# =========================================================

root.mainloop()
