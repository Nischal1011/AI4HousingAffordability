import pandas as pd
import numpy as np

def process_hud_data(df):
    """
    Process HUD data into clean format for analysis
    """
    print(f"Initial DataFrame shape: {df.shape}")
    
    # Clean column names (strip whitespace, handle special characters)
    df.columns = df.columns.str.strip().str.lower().str.replace('[^a-z0-9_]+', '_', regex=True)
    print("Cleaned columns:", df.columns.tolist())
    
    processed_df = df.copy()
    print(f"Processed DataFrame shape after copy: {processed_df.shape}")
    
    # Clean the 'code' column
    processed_df['code'] = processed_df['code'].str.replace(r'[=""]', '', regex=True)
    print("Unique values in 'code' column after cleaning:", processed_df['code'].unique())
    
    # Define target columns using cleaned names
    numeric_cols = [
        'subsidized_units_available', 
        '_occupied',
        'household_income_per_year', 
        '_in_poverty_census_tract_',
        'average_hud_expenditure_per_month_',
        '_very_low_income',
        '_extremely_low_income'
    ]
    
    # Clean numeric columns
    for col in numeric_cols:
        if col in processed_df.columns:
            processed_df[col] = pd.to_numeric(
                processed_df[col].astype(str)
                .str.replace('[^0-9.]', '', regex=True),
                errors='coerce'
            )
            print(f"Cleaned {col}: {processed_df[col].notna().sum()} non-null values")
        else:
            print(f"Warning: Column {col} not found")
    
    # Filter states (exclude territories)
    state_mask = (
        processed_df['code'].astype(str).str.len() == 2
    ) & (
        ~processed_df['code'].isin(['XX', '66', '69', '72', '78', 'US'])
    )
    processed_df = processed_df[state_mask]
    print(f"Processed DataFrame shape after state filtering: {processed_df.shape}")
    
    # Create final output
    final_columns = {
        'state_code': 'code',
        'state_name': 'name',
        'total_units': 'subsidized_units_available',
        'occupancy_rate_pct': '_occupied',
        'wait_time_months': 'average_months_on_waiting_list',
        'median_income': 'household_income_per_year',
        'hud_monthly_expenditure': 'average_hud_expenditure_per_month_',
        'pct_very_low_income': '_very_low_income',
        'pct_extremely_low_income': '_extremely_low_income',
        'pct_local_poverty': '_in_poverty_census_tract_'
    }
    
    final_df = pd.DataFrame()
    for new_col, old_col in final_columns.items():
        if old_col in processed_df.columns:
            final_df[new_col] = processed_df[old_col]
            print(f"Added {new_col}: {final_df[new_col].notna().sum()} non-null values")
        else:
            print(f"Warning: Column {old_col} not found. Setting {new_col} to NaN.")
            final_df[new_col] = np.nan
    
    # Extract state name from the 'name' column
    if 'state_name' in final_df.columns:
        final_df['state_name'] = final_df['state_name'].str.split().str[-1]
        print(f"Extracted state names: {final_df['state_name'].nunique()} unique values")
    
    # Calculate derived metrics
    if 'total_units' in final_df.columns and 'occupancy_rate_pct' in final_df.columns:
        final_df['available_units'] = final_df['total_units'] * (1 - final_df['occupancy_rate_pct']/100)
        print(f"Calculated available units: {final_df['available_units'].notna().sum()} non-null values")
    
    # Calculate need_score, handling potential NaN values
    need_score_components = [
        final_df['wait_time_months'].rank(pct=True, na_option='keep') if 'wait_time_months' in final_df.columns else pd.Series(np.nan, index=final_df.index),
        final_df['pct_extremely_low_income'].rank(pct=True, na_option='keep') if 'pct_extremely_low_income' in final_df.columns else pd.Series(np.nan, index=final_df.index),
        final_df['pct_local_poverty'].rank(pct=True, na_option='keep') if 'pct_local_poverty' in final_df.columns else pd.Series(np.nan, index=final_df.index)
    ]
    
    final_df['need_score'] = (
        need_score_components[0] * 0.4 +
        need_score_components[1] * 0.3 +
        need_score_components[2] * 0.3
    ) * 100
    print(f"Calculated need score: {final_df['need_score'].notna().sum()} non-null values")
    
    return final_df.sort_values('state_code').reset_index(drop=True)

if __name__ == "__main__":
    # Fetch the CSV file from the provided URL
    url = "data/hudPicture2023_313635.csv"
    df = pd.read_csv(url, dtype=str)  # Read all as strings initially
    print(f"CSV file read. Shape: {df.shape}")

