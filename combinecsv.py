import pandas as pd
import os

# Specify the directory where your CSV files are located
csv_directory = 'path_to_your_csv_files'

# List all CSV files in the directory
csv_files = [file for file in os.listdir(csv_directory) if file.endswith('.csv')]

# Initialize an empty list to store dataframes
df_list = []

# Loop through each CSV file, read it into a dataframe, and append it to the list
for file in csv_files:
    file_path = os.path.join(csv_directory, file)
    df = pd.read_csv(file_path)
    df_list.append(df)

# Concatenate all dataframes in the list into a single dataframe
combined_df = pd.concat(df_list, ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_df.to_csv('combined_file.csv', index=False)

print("CSV files have been successfully combined!")
