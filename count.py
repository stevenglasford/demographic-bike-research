import pandas as pd

# Load the CSV file into a pandas DataFrame
csv_file = 'combined_file.csv'  # Replace with your actual file path
df = pd.read_csv(csv_file)

# 1. Count the number of rows with nothing in info 2 and info 3
empty_info_2_and_3 = df[(df['info 2'].isna()) & (df['info 3'].isna())].shape[0]

# 2. Count the number of rows with info 2 and info 3 filled
filled_info_2_and_3 = df[(df['info 2'].notna()) & (df['info 3'].notna())].shape[0]

# 3. Count occurrences of specific words in info 1
adult_count = df['info 1'].str.contains('adult', case=False, na=False).sum()
youth_count = df['info 1'].str.contains('youth', case=False, na=False).sum()
senior_count = df['info 1'].str.contains('senior', case=False, na=False).sum()
disabled_count = df['info 1'].str.contains('disabled', case=False, na=False).sum()

# 4. Count occurrences of specific words in info 2
white_count = df['info 2'].str.contains('white', case=False, na=False).sum()
black_count = df['info 2'].str.contains('black', case=False, na=False).sum()
asian_count = df['info 2'].str.contains('asian', case=False, na=False).sum()
other_count = df['info 2'].str.contains('other', case=False, na=False).sum()

# 5. Count occurrences of specific words in info 3
general_count = df['info 3'].str.contains('general', case=False, na=False).sum()
transit_count = df['info 3'].str.contains('transit', case=False, na=False).sum()
bike_count = df['info 3'].str.contains('bike', case=False, na=False).sum()

# Display the results
print(f'Number of rows with nothing in info 2 and 3: {empty_info_2_and_3}')
print(f'Number of rows with info 2 and 3 filled: {filled_info_2_and_3}')
print(f'Number of times "adult" is found in info 1: {adult_count}')
print(f'Number of times "youth" is found in info 1: {youth_count}')
print(f'Number of times "senior" is found in info 1: {senior_count}')
print(f'Number of times "disabled" is found in info 1: {disabled_count}')
print(f'Number of times "white" is found in info 2: {white_count}')
print(f'Number of times "black" is found in info 2: {black_count}')
print(f'Number of times "asian" is found in info 2: {asian_count}')
print(f'Number of times "other" is found in info 2: {other_count}')
print(f'Number of times "general" is found in info 3: {general_count}')
print(f'Number of times "transit" is found in info 3: {transit_count}')
print(f'Number of times "bike" is found in info 3: {bike_count}')
