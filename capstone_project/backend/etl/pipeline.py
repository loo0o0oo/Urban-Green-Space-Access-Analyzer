import pandas as pd
import geopandas as gpd

def run_etl():
    print("ETL script running...")
    # Example: Load and print data structure
    try:
        # Replace with actual file paths or URLs
        canopy_df = gpd.read_file("data/tree_canopy.geojson")
        demo_df = pd.read_csv("data/demographics.csv")

        merged = canopy_df.merge(demo_df, on="GEOID")
        merged.to_file("data/merged_data.geojson", driver='GeoJSON')
        print("ETL complete: merged_data.geojson saved.")
    except Exception as e:
        print(f"ETL failed: {e}")

if __name__ == "__main__":
    run_etl()