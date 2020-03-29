import numpy as np
from math import hypot
from gpxpy import geo


def closest_point_on_path(point, path):
    for index, row in path.iterrows():
        distance = hypot(point[0] - row['lat'], point[1] - row['lon'])
        try:
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_distance_coordinates = row['lat'], row['lon']
        except NameError:
            shortest_distance = distance
            shortest_distance_coordinates = row['lat'], row['lon']

    return shortest_distance_coordinates


def find_paths_midpoint(path1, path2):
    midpoints_lat = []
    midpoints_lon = []
    for index, row in path1.iterrows():
        closest_point_coord = closest_point_on_path((row['lat'], row['lon']), path2)
        midpoints_lat.append((row['lat']+closest_point_coord[0])/2)
        midpoints_lon.append((row['lon']+closest_point_coord[1])/2)

    return midpoints_lat, midpoints_lon


def get_geo_translation(x1, y1, x2, y2):
    return (x2-x1),(y2-y1)


def smooth_geo_path_points(x1, y1, x2, y2, smooth_factor=0.1):
    """Return more points between two points. This smooths out the path. The lower the smooth factor
    the more intermediate points that there will be."""

    x_trans, y_trans = get_geo_translation(x1, y1, x2, y2)

    smooth_x = [x1]
    smooth_y = [y1]

    for factor in np.arange(smooth_factor, 1, smooth_factor):
        smooth_x.append(x1 + (factor * x_trans))
        smooth_y.append(y1 + (factor * y_trans))

    smooth_x.append(x2)
    smooth_y.append(y2)

    return smooth_x, smooth_y


def smooth_geo_path(path, smooth_factor=0.1):
    """Generates a new smoothed path based on the old path."""
    interpolated_x = []
    interpolated_y = []

    for index, rows in path.iterrows():
        if index == 0:
            pass
        else:
            smooth_x, smooth_y = smooth_geo_path_points(path.iloc[index - 1]['lon'], path.iloc[index - 1]['lat'],
                                                        path.iloc[index]['lon'], path.iloc[index]['lat'], smooth_factor)
            interpolated_x.append(smooth_x)
            interpolated_y.append(smooth_y)

    return interpolated_x, interpolated_y
