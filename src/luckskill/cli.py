import matplotlib.pyplot as plt
from src.luckskill.simulate import simulate_round_robin
from src.luckskill.metrics import rank_skill_correlation

def run_demo():
    print("→ Running Luck vs Skill demo...")
    df = simulate_round_robin(n_players=10, skill_std=1.0, luck_std=1.0)
    corr = rank_skill_correlation(df)
    print(df)
    print(f"Correlation between skill and wins: {corr:.2f}")

    plt.scatter(df["skill"], df["wins"])
    plt.xlabel("True Skill")
    plt.ylabel("Wins")
    plt.title("Luck vs Skill Simulation")
    plt.grid(True)
    plt.savefig("results/demo_plot.png")
    print("✅ Saved plot to results/demo_plot.png")

if __name__ == "__main__":
    run_demo()

