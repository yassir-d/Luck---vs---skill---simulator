# Project Proposal — Luck vs Skill Simulator

## Category
🎯 Simulation & Statistical Analysis

## Problem Statement
In competitive environments like sports, esports, and even professional careers, results often depend on a mix of **skill** and **luck**.  
However, it’s hard to clearly measure how much each factor truly matters. This project aims to simulate tournaments to explore the relationship between skill and randomness, helping to answer the question: *how much of success is really skill, and how much is just luck?*

## Motivation
As someone passionate about sports—especially basketball—I’ve always been curious about how much luck influences performance.  
A player can work hard and still lose because of random factors like bad timing, referee calls, or simple variance in shots.  
This inspired me to design a simulator that lets users experiment with different levels of luck and skill, and see how the balance between them affects outcomes.  
Beyond sports, this concept connects to many real-world contexts, like investment decisions or career success, where outcomes often depend on chance as much as ability.

## Planned Approach
1. **Simulation Engine**  
   I’ll use Python with NumPy and pandas to simulate tournaments where players compete in a round-robin format.  
   Each player has a fixed skill score, and match results are influenced by both skill and a random “luck” component.  
2. **Analysis**  
   After each tournament, I’ll measure how strongly players’ final rankings correlate with their true skills using Spearman correlation.  
   Running the simulation multiple times under different levels of luck will reveal how predictability changes.  
3. **Visualization**  
   Using matplotlib, I’ll plot how the correlation between skill and success decreases as luck increases—a visual “Luck vs Skill” curve.

## Expected Challenges
- Managing randomness and ensuring reproducible results.  
- Structuring modular and clean code for scalability.  
- Creating clear and meaningful visualizations.

## Success Criteria
- A working, well-documented simulator that runs reproducibly.  
- Informative plots that clearly show how luck impacts fairness and predictability.  
- Clean, modular Python code with testing and documentation.

## Stretch Goals
- Add interactive command-line parameters (e.g., number of players, skill variance, luck intensity).  
- Simulate multiple sports or scoring systems.  
- Possibly compare simulated results with real basketball or esports data.

