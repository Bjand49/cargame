import csv
import pygame

# Parse CSV File
def parse_csv(filename):
    data = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Load Data into Pygame (Example)
def load_data_into_pygame(data):
    # Your Pygame code to load entities from the data
    pass

# Retrieve Entities with a Value
def get_entities_with_value(data):
    indices = []
    for i, row in enumerate(data):
        for j, cell in enumerate(row):
            if cell is not None:
                indices.append((i, j))
    return indices

# Example usage
filename = 'road.csv'
loaded_data = parse_csv(filename)
load_data_into_pygame(loaded_data)
entities_with_value = get_entities_with_value(loaded_data)
print("Entities with value:", entities_with_value)
