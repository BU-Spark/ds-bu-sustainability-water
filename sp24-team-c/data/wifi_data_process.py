import pandas as pd

# READ CSV FILE
df = pd.read_csv('updated_densitymap_hourly_cleaned.csv')
df['building_type'] = df['building_type'].str.strip()

# exclude 'building_type' 列中为 'Residential', 'Parking', 'Housing' 'Commercial' 
filtered_df = df[~df['building_type'].isin(['Residential', 'Parking', 'Housing', 'Commercial'])]


# calculate max and mean density cnt based on same building floor and building desc
# cnt refers to the number of people in the space at a given point in time
grouped_values = filtered_df.groupby(['building_floor', 'building_desc'], as_index=False).agg(
    mean_density_cnt=('density_cnt', 'mean'),
    max_density_cnt=('density_cnt', 'max')
)

#only record first column for each same building floor + building description
first_row_flags = filtered_df.groupby(['building_floor', 'building_desc']).cumcount() == 0
representative_rows = filtered_df[first_row_flags]

# add mean and max density into file
final_representative_rows = pd.merge(representative_rows, grouped_values, on=['building_floor', 'building_desc'], how='left')

# delete 'date'  'hour' 'density_cnt''dc_ratio'
final_representative_rows_cleaned = final_representative_rows.drop(columns=['date', 'hour','density_cnt','dc_ratio'], errors='ignore')

# add  'average_dc_ratio' and max dc ratio
final_representative_rows_cleaned['average_dc_ratio'] = final_representative_rows_cleaned['mean_density_cnt'] / final_representative_rows_cleaned['capacity']
 
final_representative_rows_cleaned['max_dc_ratio'] = final_representative_rows_cleaned['max_density_cnt'] / final_representative_rows_cleaned['capacity']

# create processed file
final_representative_rows_cleaned.to_csv('wifi_update.csv', index=False)

