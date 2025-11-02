# Luck vs Skill Simulator 🎲🏀

A Python simulation to explore how much outcomes in competitions are driven by **skill** vs **luck**.

## Overview
This project simulates a round-robin tournament where each player has a hidden "skill" value, but match results also depend on randomness ("luck").  
It calculates how strongly skill explains results, using a Spearman correlation.

## Run the simulation
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install numpy pandas matplotlib scipy pytest
PYTHONPATH=. python -m src.luckskill.cli
