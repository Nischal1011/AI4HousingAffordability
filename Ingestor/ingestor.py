from Wrapper.census import CensusAPIWrapper
import os
import pandas as pd

if __name__ == "__main__":
    API_KEY = os.getenv("CENSUS_API_KEY")
    census_api = CensusAPIWrapper(API_KEY)

    # Define variables to fetch (ZIP-level housing & affordability indicators)
    variables = [
        "B25004_001E",  # Total Vacant Housing Units
        "B25003_002E",  # Owner-Occupied Housing Units
        "B25003_003E",  # Renter-Occupied Housing Units
        "B25064_001E",  # Median Gross Rent
        "B19013_001E",  # Median Household Income
        "B25105_001E",  # Median Monthly Housing Costs
        "B17001_002E",  # Population Below Poverty Level
        "B25077_001E",  # Median Home Value
        "B08303_001E",  # Total Public Transportation Usage (commute insights)
        "B25058_001E",  # Median Contract Rent
        "B25071_001E",  # Gross Rent as Percentage of Household Income
    ]

    # Fetch data at ZIP code level
    df = census_api.get_zip_data(variables)

    # Create column name mapping dictionary
    column_mapping = {
        "B25004_001E": "total_vacant_housing_units",
        "B25003_002E": "owner_occupied_housing_units",
        "B25003_003E": "renter_occupied_housing_units",
        "B25064_001E": "median_gross_rent",
        "B19013_001E": "median_household_income",
        "B25105_001E": "median_monthly_housing_costs",
        "B17001_002E": "population_below_poverty_level",
        "B25077_001E": "median_home_value",
        "B08303_001E": "total_public_transportation_usage",
        "B25058_001E": "median_contract_rent",
        "B25071_001E": "gross_rent_percentage_of_income"
    }

    # Rename columns using the mapping dictionary
    df = df.rename(columns=column_mapping)

    # Convert numeric columns (preserve renamed columns)
    numeric_cols = [col for col in df.columns if col not in ["NAME", "zip code tabulation area"]]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors="coerce")

    print(df.head())


    from Wrapper.HUD import HUDDataProcessor

    hud = HUDDataProcessor(file_path="data/HUD.csv")
    hud_data = hud.get_hud_data()