{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7638c374-753a-4e41-86ca-3ea9cbd3dbe4",
   "metadata": {},
   "source": [
    "Environment – Tic-Tac-Toe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "783f3011-6c50-4f57-823b-f0a32abfef75",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 1: Environment\n",
    "import random\n",
    "\n",
    "class TicTacToeEnv:\n",
    "    def __init__(self, seed=42):\n",
    "        self.rng = random.Random(seed)\n",
    "        self.reset()\n",
    "\n",
    "    def reset(self):\n",
    "        self.board = [0]*9\n",
    "        self.current_player = 1\n",
    "        self.done = False\n",
    "        self.winner = 0\n",
    "        return tuple(self.board)\n",
    "\n",
    "    def state(self):\n",
    "        return tuple(self.board)\n",
    "\n",
    "    def available_actions(self):\n",
    "        return [i for i,v in enumerate(self.board) if v==0]\n",
    "\n",
    "    @staticmethod\n",
    "    def _lines():\n",
    "        return [\n",
    "            (0,1,2),(3,4,5),(6,7,8),\n",
    "            (0,3,6),(1,4,7),(2,5,8),\n",
    "            (0,4,8),(2,4,6)\n",
    "        ]\n",
    "\n",
    "    def _check_winner(self):\n",
    "        for a,b,c in self._lines():\n",
    "            s = self.board[a] + self.board[b] + self.board[c]\n",
    "            if s == 3: return 1\n",
    "            if s == -3: return -1\n",
    "        if 0 not in self.board: return 0  # draw\n",
    "        return None  # ongoing\n",
    "\n",
    "    def step(self, action, player):\n",
    "        if self.done: raise ValueError(\"Game over\")\n",
    "        if self.board[action] != 0:\n",
    "            self.done = True\n",
    "            self.winner = -player\n",
    "            reward = -1 if player==1 else +1\n",
    "            return self.state(), reward, True, {\"illegal\": True}\n",
    "\n",
    "        self.board[action] = player\n",
    "        status = self._check_winner()\n",
    "        if status is not None:\n",
    "            self.done = True\n",
    "            self.winner = status\n",
    "            reward = 1 if status==1 else (-1 if status==-1 else 0.2)\n",
    "            return self.state(), reward, True, {}\n",
    "        return self.state(), 0, False, {}\n",
    "\n",
    "    def render(self):\n",
    "        symbols = {1:'X', -1:'O', 0:'.'}\n",
    "        for r in range(3):\n",
    "            print(' '.join(symbols[self.board[r*3+c]] for c in range(3)))\n",
    "        print()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fb8991fb-1826-46ac-a208-e63b467e669a",
   "metadata": {},
   "source": [
    "✅ Test Environment:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "eb0aa8da-00bc-4378-9696-d09f7e51f01c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ". . .\n",
      ". . .\n",
      ". . .\n",
      "\n",
      "X . .\n",
      ". . .\n",
      ". . .\n",
      "\n"
     ]
    }
   ],
   "source": [
    "env = TicTacToeEnv()\n",
    "env.render()\n",
    "state, reward, done, info = env.step(0,1)\n",
    "env.render()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "e80b47f0-c6f4-4f61-ac34-f23b1e93325a",
   "metadata": {},
   "source": [
    "Opponents"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "2dbc8897-1905-427c-83dd-a40076f615ef",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Step 2: Opponents\n",
    "import random\n",
    "\n",
    "def opponent_random(env):\n",
    "    return random.choice(env.available_actions())\n",
    "\n",
    "def opponent_rule_based(env):\n",
    "    board = env.board\n",
    "    avail = env.available_actions()\n",
    "\n",
    "    def would_win(action, mark):\n",
    "        tmp = board.copy()\n",
    "        tmp[action] = mark\n",
    "        for a,b,c in TicTacToeEnv._lines():\n",
    "            if tmp[a]+tmp[b]+tmp[c]==3*mark: return True\n",
    "        return False\n",
    "\n",
    "    # 1) Win if possible\n",
    "    for a in avail:\n",
    "        if would_win(a, -1): return a\n",
    "    # 2) Block X\n",
    "    for a in avail:\n",
    "        if would_win(a, 1): return a\n",
    "    # 3) Choose center/corners/sides\n",
    "    for p in [4,0,2,6,8,1,3,5,7]:\n",
    "        if p in avail: return p\n",
    "    return random.choice(avail)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "489f0e56-b2b3-4410-a479-f6d43c5706a9",
   "metadata": {},
   "source": [
    "✅ Test Opponent:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "3057794c-0485-4a4e-a3bb-061a1768210a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "7\n",
      "4\n"
     ]
    }
   ],
   "source": [
    "env = TicTacToeEnv()\n",
    "print(opponent_random(env))\n",
    "print(opponent_rule_based(env))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "696e0b72-8e7e-4b84-b7a1-0bbc94fca5f7",
   "metadata": {},
   "source": [
    "Step 4: Training Loop"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "5218e82f-22b6-4b16-bdd3-af7d462147f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "def play_episode(env, agent, opponent_fn=opponent_random, agent_starts=True):\n",
    "    s = env.reset()\n",
    "    env.current_player = 1 if agent_starts else -1\n",
    "    done = False\n",
    "    while not done:\n",
    "        if env.current_player == 1:\n",
    "            legal = env.available_actions()\n",
    "            a = agent.select_action(s, legal)\n",
    "            s_next, r, done, _ = env.step(a, 1)\n",
    "            legal_next = env.available_actions() if not done else []\n",
    "            agent.update(s, a, r, s_next, legal_next, done)\n",
    "            s = s_next\n",
    "            env.current_player = -1\n",
    "        else:\n",
    "            a_op = opponent_fn(env)\n",
    "            s, r, done, _ = env.step(a_op, -1)\n",
    "            env.current_player = 1\n",
    "    return env.winner\n",
    "\n",
    "def train(agent, episodes=5000, eval_every=500):\n",
    "    env = TicTacToeEnv()\n",
    "    log = []\n",
    "    for ep in range(1, episodes+1):\n",
    "        agent_starts = (ep%2==0)\n",
    "        opp = opponent_random if ep%4 !=0 else opponent_rule_based\n",
    "        winner = play_episode(env, agent, opponent_fn=opp, agent_starts=agent_starts)\n",
    "        agent.decay_epsilon()\n",
    "        if ep % eval_every == 0:\n",
    "            log.append((ep, winner, agent.epsilon))\n",
    "            print(f\"Episode {ep} | Last winner: {winner} | ε={agent.epsilon:.3f}\")\n",
    "    return log\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4413913a-b413-4eea-a8d8-9ab9ebc24daf",
   "metadata": {},
   "source": [
    "✅ Test Agent:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "07184735-56be-495e-bdee-840d820c841c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Episode 500 | Last winner: -1 | ε=0.779\n",
      "Episode 1000 | Last winner: -1 | ε=0.606\n",
      "Episode 1500 | Last winner: -1 | ε=0.472\n",
      "Episode 2000 | Last winner: 0 | ε=0.368\n",
      "Episode 2500 | Last winner: -1 | ε=0.286\n",
      "Episode 3000 | Last winner: -1 | ε=0.223\n"
     ]
    }
   ],
   "source": [
    "agent = QAgent()\n",
    "log = train(agent, episodes=3000, eval_every=500)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "471b0678-57f6-4257-a7ec-06329169aeb2",
   "metadata": {},
   "source": [
    "Step 5: Evaluation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "681cbc8f-524e-44c5-94ea-904d5e7375da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vs Random: {1: 369, -1: 111, 0: 20}\n",
      "Vs Rule-Based: {1: 0, -1: 500, 0: 0}\n"
     ]
    }
   ],
   "source": [
    "# Step 5: Evaluation\n",
    "def evaluate(agent, n_games=500, opponent_fn=opponent_rule_based):\n",
    "    env = TicTacToeEnv()\n",
    "    results = {1:0, -1:0, 0:0}\n",
    "    for i in range(n_games):\n",
    "        s = env.reset()\n",
    "        env.current_player = 1 if i%2==0 else -1\n",
    "        done = False\n",
    "        while not done:\n",
    "            if env.current_player == 1:\n",
    "                legal = env.available_actions()\n",
    "                if legal:\n",
    "                    q_vals = [agent.Q[(s,a)] for a in legal]\n",
    "                    a = legal[int(np.argmax(q_vals))]\n",
    "                    s, r, done, _ = env.step(a, 1)\n",
    "                env.current_player = -1\n",
    "            else:\n",
    "                a_op = opponent_fn(env)\n",
    "                s, r, done, _ = env.step(a_op, -1)\n",
    "                env.current_player = 1\n",
    "        results[env.winner] += 1\n",
    "    return results\n",
    "\n",
    "# Evaluate\n",
    "res_rand = evaluate(agent, 500, opponent_random)\n",
    "res_rule = evaluate(agent, 500, opponent_rule_based)\n",
    "print(\"Vs Random:\", res_rand)\n",
    "print(\"Vs Rule-Based:\", res_rule)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "27a59728-8591-4fcb-916f-5670a9a3215e",
   "metadata": {},
   "source": [
    "Demo Game"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c3e31128-aafc-49df-80dd-c7c953c4458e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      ". . .\n",
      ". . .\n",
      ". . .\n",
      "\n",
      "X . .\n",
      ". . .\n",
      ". . .\n",
      "\n",
      "X . .\n",
      ". O .\n",
      ". . .\n",
      "\n",
      "X X .\n",
      ". O .\n",
      ". . .\n",
      "\n",
      "X X O\n",
      ". O .\n",
      ". . .\n",
      "\n",
      "X X O\n",
      "X O .\n",
      ". . .\n",
      "\n",
      "X X O\n",
      "X O .\n",
      "O . .\n",
      "\n",
      "Winner: Opponent\n"
     ]
    }
   ],
   "source": [
    "# Step 6: Demo\n",
    "env_demo = TicTacToeEnv()\n",
    "s = env_demo.reset()\n",
    "env_demo.current_player = 1\n",
    "env_demo.render()\n",
    "\n",
    "while not env_demo.done:\n",
    "    if env_demo.current_player == 1:\n",
    "        legal = env_demo.available_actions()\n",
    "        if legal:\n",
    "            q_vals = [agent.Q[(s,a)] for a in legal]\n",
    "            a = legal[int(np.argmax(q_vals))]\n",
    "            s, r, done, _ = env_demo.step(a, 1)\n",
    "        env_demo.render()\n",
    "        env_demo.current_player = -1\n",
    "    else:\n",
    "        a_op = opponent_rule_based(env_demo)\n",
    "        s, r, done, _ = env_demo.step(a_op, -1)\n",
    "        env_demo.render()\n",
    "        env_demo.current_player = 1\n",
    "\n",
    "print(\"Winner:\", {1:\"Agent\", -1:\"Opponent\", 0:\"Draw\"}[env_demo.winner])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f198ffeb-fb57-402d-8c37-a5d3968b06b1",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:venv]",
   "language": "python",
   "name": "conda-env-venv-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
