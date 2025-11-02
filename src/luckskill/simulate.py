import numpy as np
import pandas as pd

def simulate_round_robin(n_players=8, skill_std=1.0, luck_std=1.0, seed=42):
    """
    Simulate a round-robin tournament.
    Returns a DataFrame with columns: player, skill, wins, rank.
    """
    rng = np.random.default_rng(seed)
    skills = rng.normal(0.0, skill_std, size=n_players)
    wins = np.zeros(n_players)

    for i in range(n_players):
        for j in range(i + 1, n_players):
            perf_i = skills[i] + rng.normal(0.0, luck_std)
            perf_j = skills[j] + rng.normal(0.0, luck_std)
            if perf_i > perf_j:
                wins[i] += 1
            else:
                wins[j] += 1

    df = pd.DataFrame({"player": np.arange(n_players),
                       "skill": skills,
                       "wins": wins})
    df["rank"] = df["wins"].rank(ascending=False, method="min")
    return df

