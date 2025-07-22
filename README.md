# 🐜 Ants Simulation – First University Project

> Final submission for our first programming assignment in the "Computational Thinking" course at Universidad de San Andrés.

## 🧠 Project Overview

This simulation models how ants collect food in a forest represented as a grid.  
Each cell in the grid can contain: food, an obstacle, an ant, or be empty or previously visited.

The behavior is randomized: ants move freely (unless blocked) and leave a visible trail. The simulation helps predict how efficiently ants can gather food under different conditions.

---

## 🗂️ Programs Included

1. **Ant Simulation Viewer:**  
   Animates the movement of ants across the grid in real-time over 200 steps.

2. **Food Collection Analysis:**  
   Runs 100 simulations and calculates how many steps ants need on average to gather at least half the food.

3. **Exploration Area Study:**  
   Simulates 10,000 runs to compute the average area explored by ants after 200 steps with no food present.

---

## 🎨 Grid Cell Colors (via `termcolor`)

- 🟩 `green`: empty cell  
- 🟥 `red`: ant  
- ⚪️ `white`: food  
- ⬛ `grey`: obstacle  
- 🟨 `yellow`: visited cell  

---

## 🛠️ Technologies Used

- Python 3.10  
- `termcolor` for terminal color output  
- Randomized simulation logic  
- Matrix manipulation

---

## 🧪 What I Learned

This was my **first real programming project**. I learned how to:
- Work with matrices in Python
- Simulate random movement
- Write clean code across multiple files
- Analyze data using averages and extrema
- Animate terminal output step-by-step

---
