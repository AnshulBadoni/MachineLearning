import itertools
import csv

# Define the column names and their corresponding data
column_data = {
    'zone': [
        'Bhaniyawala',
        'Bhauwala',
        'Dakpatthar',
        'Doiwala',
        'Herbertpur',
        'Laltapper-Majri Grant',
        'Ranipokhri',
        'Sahaspur',
        'Selaqui',
        'Thano',
        'Vikasnagar'
    ],
    'town/village': [
        'yes',
        'no'
    ],
    'area_type': [
        # Add the data for 'area_type' here
        'residential',
        'commercial'
    ],
    'agriculture': [
        # Add the data for 'agriculture' here
        'yes',
        'no'
    ],
    'services(transport,hospital,water supply,education,market)': [
        # Add the data for 'services(transport,hospital,water supply,education,market)' here
        '1',
        '5',
        '4',
        '3',
        '2',
        '1',
        '0'
    ]
}

# Prompt the user to enter the filename to save the permutations
filename = input("Enter the filename to save the permutations (e.g., output.csv): ")

# Generate all permutations of the columns
permutations = list(itertools.product(*column_data.values()))

# Save permutations to a CSV file
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(column_data.keys())
    writer.writerows(permutations)

print("Permutations saved to", filename)
