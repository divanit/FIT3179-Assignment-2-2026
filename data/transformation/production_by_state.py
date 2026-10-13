import pandas as pd

# Skip the first junk row (,,,) so 'state' becomes the actual header
df = pd.read_csv('data/production_by_state(tonnes).csv', header=1).dropna(subset=['state'])

# Melt wide columns to long format
df_long = df.melt(id_vars=['state'], 
                  value_vars=['prod2005', 'prod2010', 'prod2015', 'prod2020'],
                  var_name='Year_Str', value_name='Production')

# Extract numeric year
df_long['Year'] = df_long['Year_Str'].str.replace('prod', '').astype(int)

# Clean production values (remove any commas if present as strings) and convert to numeric
df_long['Production'] = pd.to_numeric(df_long['Production'].astype(str).str.replace(',', ''), errors='coerce')

# Calculate total national production per year and state percentage
total_prod = df_long.groupby('Year')['Production'].transform('sum')
df_long['Percentage'] = (df_long['Production'] / total_prod) * 100

# Map abbreviations to TopoJSON full names
state_mapping = {
    'SA': 'South Australia',
    'NSW': 'New South Wales',
    'Vic': 'Victoria',
    'WA': 'Western Australia',
    'Tas': 'Tasmania',
    'Qld': 'Queensland'
}
df_long['StateName'] = df_long['state'].map(state_mapping)

# Save the processed file into your data folder
df_long[['StateName', 'Year', 'Production', 'Percentage']].to_csv('data/production_by_state_processed.csv', index=False)

print("Successfully generated data/production_by_state_processed.csv!")