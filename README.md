# AI GameBot – Tic-Tac-Toe (Reinforcement Learning)

## Project Overview
This project implements an **AI agent that learns to play Tic-Tac-Toe** using **Q-Learning**, a popular **reinforcement learning** algorithm.  
The AI improves its strategy by interacting with the game environment over thousands of self-play episodes, learning which moves maximize its chances of winning.

The project demonstrates **core AI concepts** such as states, actions, rewards, exploration vs. exploitation, and Q-value updates, making it a great hands-on example for reinforcement learning.

---

## Features
- **Environment Modeling:**  
  - The Tic-Tac-Toe board is represented as **states** (board positions).  
  - The agent can take **actions** (valid moves).  
  - Rewards are given for **win (+1), loss (-1), draw (+0.2)**.  

- **Q-Learning Agent:**  
  - Implements **ε-greedy exploration** to balance exploration and exploitation.  
  - Updates **Q-values** iteratively using the **Bellman equation**.  

- **Training:**  
  - Agent trains against both **random and rule-based opponents**.  
  - Thousands of episodes (30,000+) are used to ensure **optimal gameplay**.  

- **Evaluation:**  
  - Measures **win, loss, and draw rates** against different opponents.  
  - Demonstrates the agent’s performance improvements over time.  

- **Visualization:**  
  - Plots the **learning curve** showing how the AI’s performance improves with training.  

- **Demo Gameplay:**  
  - Step-by-step demonstration of the agent playing against a rule-based opponent.  
  - Shows the AI making optimal moves **without randomness**.  


## Project Structure

AI_GameBot/
│
├─ ai_gamebot.ipynb       # Jupyter notebook with code and explanations
├─ ai_gamebot.py          # Python script version for direct execution
├─ README.md              # Project description
├─ requirements.txt       # Dependencies (NumPy, Matplotlib)
└─ demo_images/           # Optional: screenshots or learning curve plots

## Installation & Usage

Clone the repository:
```bash
git clone https://github.com/YourUsername/AI_GameBot.git
cd AI_GameBot

## Install dependencies:

pip install -r requirements.txt

## Run the notebook or Python script:

Jupyter Notebook: Open ai_gamebot.ipynb and run cells step by step.


Python Script: python ai_gamebot.py

----------------------------------------------------------------------------------------------------------------------------------------

Learning Outcomes

Understand reinforcement learning concepts: states, actions, rewards, Q-values, ε-greedy policy.

Train and evaluate an AI agent in a simulated environment.

Gain experience with Python programming and object-oriented design.

Visualize AI learning progress using Matplotlib.

Learn proper project structuring and documentation for GitHub.

Optional Enhancements

Implement more sophisticated opponents (e.g., minimax algorithm).

Add a GUI for interactive gameplay using Tkinter or Pygame.

Extend Q-Learning to other simple board games.

Tech Stack

Python

NumPy

Matplotlib

Q-Learning (Reinforcement Learning)

Git & GitHub

Author

Vignesh S – MSc Data Science Student
GitHub: https://github.com/vigneshs007