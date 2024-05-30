import json
import numpy as np
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            content = line.replace("'", '"')

            data.append(json.loads(content))
    return data

def plot_data(scenario_data, scenario_name):
    generations = [item['generation'] for item in scenario_data]
    data = [item['data'] for item in scenario_data]
    
    averages = [np.mean(gen_data) for gen_data in data]
    highest_scores = [np.max(gen_data) for gen_data in data]
    
    plt.figure(figsize=(12, 6))

    for i, gen_data in enumerate(data):
        plt.plot([i+1] * len(gen_data), gen_data, 'o', alpha=0.5, label=f'Gen {i+1}' if i == 0 else "")
    
    plt.plot(generations, averages, 'r--', label='Average Score')
    
    plt.plot(generations, highest_scores, 'g-', label='Highest Score')

    for i, (avg, high) in enumerate(zip(averages, highest_scores)):
        plt.text(i+1, avg, f'{avg:.2f}', color='red', fontsize=8, ha='center', va='bottom')
        plt.text(i+1, high, f'{high}', color='green', fontsize=8, ha='center', va='bottom')

    plt.xlabel('Generation')
    plt.ylabel('Score')
    plt.title(f'Scenario: {scenario_name}')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    scenario_files = ['L', 'ROAD', 'PLUS']
    scenario_names = ['RUN1','RUN2']
    extention = ".txt"
    for file_path, scenario_name in zip(scenario_files, scenario_names):
        scenario_data = load_data("DATA/"+file_path+scenario_name + extention)
        plot_data(scenario_data, scenario_name)

main()
