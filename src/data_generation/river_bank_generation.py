import pandas as pd
from src.utils import geo_utils


def banks_data_gen(south_bank, north_bank):

    interpolated_south_bank = pd.DataFrame()
    interpolated_south_bank['lat'] = [item for sublist in geo_utils.smooth_geo_path(south_bank)[1] for item in sublist]
    interpolated_south_bank['lon'] = [item for sublist in geo_utils.smooth_geo_path(south_bank)[0] for item in sublist]

    interpolated_north_bank = pd.DataFrame()
    interpolated_north_bank['lat'] = [item for sublist in geo_utils.smooth_geo_path(north_bank)[1] for item in sublist]
    interpolated_north_bank['lon'] = [item for sublist in geo_utils.smooth_geo_path(north_bank)[0] for item in sublist]

    return interpolated_south_bank, interpolated_north_bank
