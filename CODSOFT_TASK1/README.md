🤖 CodBot — Rule-Based Chatbot
📌 CodSoft Artificial Intelligence Internship — Task 1

CodBot is a rule-based chatbot developed in Python as part of the CodSoft Artificial Intelligence Internship.

The chatbot uses regular expressions (Regex), predefined responses, conditional logic, and pattern matching to understand user input and provide appropriate responses.

The project also includes a Tkinter graphical user interface (GUI) and a safe mathematical calculator.

✨ Features
🤖 Rule-based conversational chatbot
🔎 Regex-based pattern matching
💬 Predefined conversational responses
🎲 Randomized responses
🕒 Current time
📅 Current date
😂 Random programming jokes
🐍 Basic Python information
🧠 Basic Artificial Intelligence information
🧮 Mathematical calculations
🖥️ Tkinter graphical user interface
💡 Example questions button
💾 Save conversation history
🗑️ Clear chat button
🌙 Dark mode
☀️ Light mode
⌨️ Enter key support
❓ Fallback responses for unknown questions
🛠️ Technologies Used
Python 3
Tkinter — Graphical User Interface
Regular Expressions (re) — Pattern matching
Random (random) — Randomized responses
Datetime (datetime) — Time and date
AST (ast) — Safe mathematical expression parsing
Operator (operator) — Mathematical operations
🧠 How It Works

The chatbot follows a simple rule-based approach.

Step 1 — User Input

The user enters a message through the Tkinter interface.

Step 2 — Text Processing

The chatbot converts the input to lowercase and removes unnecessary spaces.

Step 3 — Pattern Matching

Regular expressions are used to compare the user's message with predefined patterns.

For example:

r"\b(hi|hello|hey)\b"


This pattern can recognize greetings such as:

hi
hello
hey
Step 4 — Response Selection

If a pattern matches, the chatbot selects an appropriate response.

Some responses are selected randomly using:

random.choice()


This prevents the chatbot from giving exactly the same response every time.

Step 5 — Dynamic Responses

The chatbot can generate the current time and date using Python's datetime module.

Step 6 — Mathematical Calculations

The chatbot can recognize expressions such as:

25 * 4


or:

calculate (10 + 5) * 2


and return the result.

Step 7 — Fallback

If no predefined rule matches the user's input, CodBot provides a fallback response.

🖥️ Example Conversation
You: hello

CodBot: Hello! 👋 How can I help you today?

You: what is your name?

CodBot: I'm CodBot, your rule-based assistant built for CodSoft Task 1! 🤖

You: calculate 25 * 4

CodBot: The answer is 100 🧮

You: tell me a joke

CodBot: Why don't programmers like nature? It has too many bugs! 🐛

You: what time is it?

CodBot: The current time is 04:32 PM 🕒

📂 Project Structure
CODSOFT_TASK1/
│
├── chatbot.py
├── chatbot_backup.py
└── README.md

File Description
File	Description
chatbot.py	Main GUI chatbot application
chatbot_backup.py	Backup copy of the working chatbot
README.md	Project documentation
⚙️ Requirements

You need:

Python 3.x
VS Code or another Python IDE

Tkinter is included with standard Python installations on Windows.

▶️ How to Run
1. Open the project folder

Open the CODSOFT_TASK1 folder in VS Code.

2. Open the terminal

In VS Code, select:

Terminal → New Terminal

3. Run the chatbot
python chatbot.py


The CodBot graphical interface will open.

🧮 Supported Calculations

Examples:

25 + 75

100 / 4

20 * 5

50 - 15

calculate (10 + 5) * 2


The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, division, modulus, and powers.

💬 Example Questions

Try asking:

hello

what is your name?

how are you?

tell me a joke

what time is it?

what is today's date?

what is Python?

what is AI?

calculate 25 * 4

help

bye

🎯 Learning Objectives

This project demonstrates:

Python programming
Conditional logic
Regular expressions
Pattern matching
Functions
Lists and dictionaries
Randomization
Date and time handling
Mathematical expression processing
GUI development with Tkinter
Basic Natural Language Processing concepts
🚀 Future Improvements

Possible future enhancements include:

Voice input and output
Integration with an online weather API
More conversational patterns
Database-based conversation history
More advanced Natural Language Processing
Machine-learning-based responses
👨‍💻 Internship Project

Program: CodSoft Artificial Intelligence Internship

Task: Task 1 — Rule-Based Chatbot

Project: CodBot

Language: Python

📜 License

This project was created for educational and internship purposes.