import pandas as pd
from src.utils import geo_utils


def is_correct_side(point, midpoint_df, upstream_direction):
    closest_midpoint = geo_utils.closest_point_on_path(point, midpoint_df)

    if upstream_direction:
        if point[0] < closest_midpoint[0]:  # lat should be lower than the mid of river on the way up
            return True
        else:
            return False

    if not upstream_direction:
        if point[0] > closest_midpoint[0]:  # lat should be higher than the mid of river on the way down
            return True
        else:
            return False


def assign_side_features(rower_data, midpoint_df):
    upstream = [None]  # first time point
    correct_side = [True]  # start on correct side
    time_on_incorrect_side = [0]  # start not on the wrong side

    for index, row in rower_data.iterrows():
        if index == 0:
            pass
        else:
            if rower_data.iloc[index]['lon'] <= rower_data.iloc[index - 1]['lon']:  # going upstream, longitude gets lower
                upstream.append(True)
                point = row['lat'], row['lon']
                correct_side.append(is_correct_side(point, midpoint_df, upstream_direction=True))

            else:  # going downstream
                upstream.append(False)
                point = row['lat'], row['lon']
                correct_side.append(is_correct_side(point, midpoint_df, upstream_direction=False))

            if not correct_side[-1] and not correct_side[-2]:
                time_on_incorrect_side.append(
                    pd.Timedelta(rower_data.iloc[index]['time'] - rower_data.iloc[index - 1]['time']).seconds)
            else:
                time_on_incorrect_side.append(0)

    rower_data['upstream'] = upstream
    rower_data['correct_side'] = correct_side
    rower_data['time_on_incorrect_side'] = time_on_incorrect_side

    return rower_data
