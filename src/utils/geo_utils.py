from gpxpy import geo


def closest_point_on_path(point, path):
    for index, row in path.iterrows():
        distance = geo.haversine_distance(point[0], point[1], row['lat'], row['lon'])
        try:
            if distance < shortest_distance:
                shortest_distance = distance
                shortest_distance_coordinates = row['lat'], row['lon']
        except NameError:
            shortest_distance = distance
            shortest_distance_coordinates = row['lat'], row['lon']

    return shortest_distance_coordinates


def find_paths_midpoint(path1,path2):
    midpoints_lat = []
    midpoints_lon = []
    for index, row in path1.iterrows():
        closest_point_coord = closest_point_on_path((row['lat'], row['lon']), path2)
        midpoints_lat.append((row['lat']+closest_point_coord[0])/2)
        midpoints_lon.append((row['lon']+closest_point_coord[1])/2)

    return midpoints_lat, midpoints_lon
