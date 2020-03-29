import pandas as pd
from src.utils import geo_utils


def midpoint_data_generation(interpolated_south_bank, interpolated_north_bank):
    midpoints_lat, midpoints_lon = geo_utils.find_paths_midpoint(interpolated_south_bank, interpolated_north_bank)
    midpoint_df = pd.DataFrame()
    midpoint_df['lat'] = midpoints_lat
    midpoint_df['lon'] = midpoints_lon

    return midpoint_df
