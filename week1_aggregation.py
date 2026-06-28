import pandas as pd
import glob

# Find all sold files
sold_files = glob.glob('CRMLSSold*.csv')

# Read each file into a DataFrame
sold_dfs = [pd.read_csv(file, low_memory=False) for file in sold_files]

# Row count before concatenation
sold_rows_before_concat = sum(len(df) for df in sold_dfs)

# Concatenate all Sold DataFrames
sold = pd.concat(sold_dfs, ignore_index=True)

# Row count after concatenation
sold_rows_after_concat = len(sold)

# -------------------------------
# Load and concatenate Listing data
# -------------------------------

# Find all monthly Listing CSV files
listing_files = glob.glob("CRMLSListing*.csv")

# Read each file into a DataFrame
listing_dfs = [pd.read_csv(file, low_memory=False) for file in listing_files]

# Row count before concatenation
listing_rows_before_concat = sum(len(df) for df in listing_dfs)

# Concatenate all Listing DataFrames
listings = pd.concat(listing_dfs, ignore_index=True)

# Row count after concatenation
listing_rows_after_concat = len(listings)

# -------------------------------------------------
# Comments confirming row counts before/after concat
# -------------------------------------------------

print("Sold rows before concatenation:", sold_rows_before_concat)
print("Sold rows after concatenation:", sold_rows_after_concat)

print("Listing rows before concatenation:", listing_rows_before_concat)
print("Listing rows after concatenation:", listing_rows_after_concat)

# -----------------------------
# Filter to Residential only
# -----------------------------

# Row counts before Residential filter
sold_rows_before_filter = len(sold)
listing_rows_before_filter = len(listings)

# Keep only Residential properties
sold = sold[sold["PropertyType"] == "Residential"]
listings = listings[listings["PropertyType"] == "Residential"]

# Row counts after Residential filter
sold_rows_after_filter = len(sold)
listing_rows_after_filter = len(listings)

# --------------------------------------------------
# Comments confirming row counts before/after filter
# --------------------------------------------------

print("Sold rows before Residential filter:", sold_rows_before_filter)
print("Sold rows after Residential filter:", sold_rows_after_filter)

print("Listing rows before Residential filter:", listing_rows_before_filter)
print("Listing rows after Residential filter:", listing_rows_after_filter)

# -----------------------------
# Save the filtered datasets
# -----------------------------

sold.to_csv("CombinedSoldResidential.csv", index=False)
listings.to_csv("CombinedListingsResidential.csv", index=False)

print("Combined Residential datasets have been saved successfully.")