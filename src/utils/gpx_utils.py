import gpxpy
import pandas as pd


def gpx_to_df(gpx_file_name):

    gpx_file = open(gpx_file_name, 'r')
    gpx = gpxpy.parse(gpx_file)
    df = pd.DataFrame(columns=['lon', 'lat', 'alt', 'time'])
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                df = df.append({'lon': point.longitude, 'lat': point.latitude,
                                'alt': point.elevation, 'time': point.time}, ignore_index=True)
    return df
