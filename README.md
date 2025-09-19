\# AI GameBot – Tic-Tac-Toe (Reinforcement Learning)



\## Project Overview

This project implements an \*\*AI agent that learns to play Tic-Tac-Toe\*\* using \*\*Q-Learning\*\*, a popular \*\*reinforcement learning\*\* algorithm.  

The AI improves its strategy by interacting with the game environment over thousands of self-play episodes, learning which moves maximize its chances of winning.



The project demonstrates \*\*core AI concepts\*\* such as states, actions, rewards, exploration vs. exploitation, and Q-value updates, making it a great hands-on example for reinforcement learning.



---



\## Features

\- \*\*Environment Modeling:\*\*  

&nbsp; - The Tic-Tac-Toe board is represented as \*\*states\*\* (board positions).  

&nbsp; - The agent can take \*\*actions\*\* (valid moves).  

&nbsp; - Rewards are given for \*\*win (+1), loss (-1), draw (+0.2)\*\*.  



\- \*\*Q-Learning Agent:\*\*  

&nbsp; - Implements \*\*ε-greedy exploration\*\* to balance exploration and exploitation.  

&nbsp; - Updates \*\*Q-values\*\* iteratively using the \*\*Bellman equation\*\*.  



\- \*\*Training:\*\*  

&nbsp; - Agent trains against both \*\*random and rule-based opponents\*\*.  

&nbsp; - Thousands of episodes (30,000+) are used to ensure \*\*optimal gameplay\*\*.  



\- \*\*Evaluation:\*\*  

&nbsp; - Measures \*\*win, loss, and draw rates\*\* against different opponents.  

&nbsp; - Demonstrates the agent’s performance improvements over time.  



\- \*\*Visualization:\*\*  

&nbsp; - Plots the \*\*learning curve\*\* showing how the AI’s performance improves with training.  



\- \*\*Demo Gameplay:\*\*  

&nbsp; - Step-by-step demonstration of the agent playing against a rule-based opponent.  

&nbsp; - Shows the AI making optimal moves \*\*without randomness\*\*.  



---



\## Project Structure



