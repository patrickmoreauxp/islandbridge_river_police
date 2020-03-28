import pandas as pd
from src import features
from config import config
from src.utils import viz_utils
from src.utils import gpx_utils


def infringement_finder(rower_data_file):
    rower_data = gpx_utils.gpx_to_df(rower_data_file)
    midpoint_data = pd.read_csv(config['MIDPOINT_DATA'])
    rower_data = features.assign_side_features(rower_data, midpoint_data)
    infringements = rower_data[rower_data['time_on_incorrect_side'] != 0]
    viz_utils.viz_infringements(infringements, config['GOOGLE_MAPS_API_KEY'])

