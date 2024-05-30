import json
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            content = line.replace("'", '"')
            data.append(json.loads(content))
    return data

def lighten_color(color, amount=0.5):
    try:
        c = mcolors.cnames[color]
    except:
        c = color
    c = mcolors.to_rgb(c)
    return mcolors.to_hex((1 - amount) * np.array(c) + amount * np.array([1, 1, 1]))

def plot_data(scenario_data, scenario_names, scenario_title):
    fig, ax = plt.subplots(figsize=(6, 6))  # Adjusted width from 12 to 6
    ax.set_title(f'{scenario_title} Comparison')

    base_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    for i, (data, name) in enumerate(zip(scenario_data, scenario_names)):
        generations = [item['generation'] for item in data]
        data = [item['data'] for item in data]
        averages = [np.mean(gen_data) for gen_data in data]
        highest_scores = [np.max(gen_data) for gen_data in data]

        base_color = base_colors[i % len(base_colors)]
        light_color = lighten_color(base_color, 0.5)

        ax.plot(generations, averages, label=f'{name} Average Score',
                color=base_color, linestyle='-', alpha=0.7)

        # Plotting the highest scores with lightened color
        ax.plot(generations, highest_scores, label=f'{name} Highest Score',
                color=light_color, linestyle='--', alpha=0.7)

    ax.set_xlabel('Generation')
    ax.set_ylabel('Score')
    ax.set_xticks(range(0, max(generations)+1, 5))
    ax.set_xticklabels([str(gen) for gen in range(0, max(generations)+1, 5)])
    ax.legend()
    ax.grid(True)
    plt.tight_layout()
    plt.show()

def main():
    scenario_files = ['L', 'DONUT', 'PLUS']
    scenario_names = ['RUN1', 'RUN2']
    extension = ".txt"

    for scenario in scenario_files:
        scenario_data = []
        for scenario_name in scenario_names:
            file_path = f"DATA/{scenario}{scenario_name}{extension}"
            scenario_data.append(load_data(file_path))
        plot_data(scenario_data, scenario_names, scenario)

main()
