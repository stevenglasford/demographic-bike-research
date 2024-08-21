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
youth_count = df['info 1'].str.contains('young', case=False, na=False).sum()
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
print(f'Number of stray cars: {empty_info_2_and_3}')
print(f'Number of persons: {filled_info_2_and_3}')
print(f'Number of adults: {adult_count}')
print(f'Number of children: {youth_count}')
print(f'Number of seniors: {senior_count}')
print(f'Number of disabled persons: {disabled_count}')
print(f'Number of white persons: {white_count}')
print(f'Number of black persons: {black_count}')
print(f'Number of asian persons {asian_count}')
print(f'Number of other race persons: {other_count}')
print(f'Number of people walking: {general_count}')
print(f'Number of persons waiting for bus or train {transit_count}')
print(f'Number of bikes: {bike_count}')
