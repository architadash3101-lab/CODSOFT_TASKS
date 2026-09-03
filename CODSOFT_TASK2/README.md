🎮 Tic-Tac-Toe — Unbeatable AI

An interactive Tic-Tac-Toe web game where a human player competes against an AI powered by the Minimax algorithm with Alpha-Beta Pruning.

This project was developed as Task 2 of my Artificial Intelligence Internship at CodSoft.

📌 Project Overview

This project demonstrates how Artificial Intelligence can be used to make optimal decisions in a two-player game.

The player can choose to play as X or O, while the AI analyzes possible future game states and selects the best available move.

The AI uses:

Minimax Algorithm
Alpha-Beta Pruning
Game-tree search
Optimal move selection
Win and draw detection

The objective is to create an AI opponent that plays optimally and does not lose when the player makes optimal decisions.

✨ Features
🎮 Human vs AI gameplay
🤖 Unbeatable AI
🧠 Minimax algorithm
✂️ Alpha-Beta Pruning
❌ Play as X
⭕ Play as O
🔄 New Game button
🏆 Win detection
🤝 Draw detection
📊 Score tracking
📈 AI search-node counter
⚡ Move-ordering optimization
📱 Responsive design
🌙 Modern dark-themed interface
🧠 AI Algorithm
Minimax

Minimax is a recursive decision-making algorithm commonly used in two-player games.

The AI explores possible future moves and assigns a score to each game state.

The scoring system is:

Result	Score
AI wins	Positive
Human wins	Negative
Draw	0

The AI selects the move with the highest possible score while assuming that the human player will make the best possible move.

Alpha-Beta Pruning

Alpha-Beta Pruning improves the efficiency of the Minimax algorithm by eliminating branches that cannot affect the final decision.

It uses two values:

Alpha (α) — the best value currently achievable by the maximizing player.
Beta (β) — the best value currently achievable by the minimizing player.

When:

β ≤ α


the remaining branches can be skipped because they cannot improve the result.

🔍 How It Works
Player makes a move
        ↓
AI examines possible moves
        ↓
Minimax explores future game states
        ↓
Alpha-Beta Pruning removes unnecessary branches
        ↓
Moves are evaluated
        ↓
AI selects the best move
        ↓
AI makes its move


The AI also uses move ordering by checking the center, corners, and edges in a preferred order. This can improve the effectiveness of Alpha-Beta Pruning.

🛠️ Technologies Used
HTML5
CSS3
JavaScript
Minimax Algorithm
Alpha-Beta Pruning
SVG
📂 Project Structure
CODSOFT_TASKSNO/
│
├── Task1/
│   └── ...
│
├── Task2/
│   ├── index.html
│   └── README.md
│
└── Task3/
    └── ...

▶️ How to Run

No additional libraries or installations are required.

Step 1

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Step 2

Open the Task2 folder.

Step 3

Open:

index.html


in any modern web browser.

You can also use VS Code Live Server to run the project.

🎮 How to Play
Play as X
Select Play as X.
You make the first move.
Click any empty square.
The AI calculates its best response.
Continue until the game ends.
Play as O
Select Play as O.
The AI makes the first move.
Click an empty square to respond.
Continue playing against the AI.
📊 Game Statistics

The application displays:

You — Number of games won by the player.
Draws — Number of tied games.
AI — Number of games won by the AI.
Nodes evaluated — Number of game states evaluated during the latest AI search.
Total nodes — Total number of game states evaluated during the session.


🎯 Learning Outcomes

Through this project, I learned about:

Artificial Intelligence fundamentals
Game theory
Minimax search
Alpha-Beta Pruning
Recursive algorithms
Game-state evaluation
AI decision-making
JavaScript programming
DOM manipulation
Responsive web development
🚀 Future Improvements

Possible future improvements include:

Multiple difficulty levels
Sound effects
Game animations
Dark/light theme
Player name customization
Game history
AI thinking visualization
Persistent score storage
Advanced AI statistics
🏢 Internship

This project was completed as Task 2 of the CodSoft Artificial Intelligence Internship.

The project demonstrates the practical application of Artificial Intelligence and game-search algorithms.

👨‍💻 Author

Archita Priya Darshin Dash

GitHub: https://github.com/architadash3101-lab

LinkedIn: https://www.linkedin.com/in/archita-dash-6b07b3400

⭐ Acknowledgment

Thanks to CodSoft for providing the opportunity to work on practical Artificial Intelligence projects and improve my understanding of AI algorithms.

#codsoft #internship #artificialintelligence #AI #JavaScript #HTML #CSS #Minimax #AlphaBetaPruning #GitHub