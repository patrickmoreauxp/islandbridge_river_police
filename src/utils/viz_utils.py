from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource, GMapOptions
from bokeh.plotting import gmap
from bokeh.models import ColumnDataSource, GMapOptions, HoverTool

IB_LAT = 53.346205
IB_LON = -6.319618


def viz_infringements(infringement_df, google_api_key):
    output_file("gmap.html")
    source = ColumnDataSource(
        data=dict(lat=infringement_df['lat'],
                  lon=infringement_df['lon'],
                  upstream=infringement_df['upstream'],
                  time_on_incorrect_side=infringement_df['time_on_incorrect_side'])
    )

    map_options = GMapOptions(lat=IB_LAT, lng=IB_LON, map_type="roadmap", zoom=11)

    hover_info = [
        ("Upstream", "@upstream"),
        ("Duration of infringment", "@time_on_incorrect_side")
    ]

    p = gmap(google_api_key, map_options, title=f"You spent {sum(infringement_df['time_on_incorrect_side'])} "
                                                f"seconds on the wrong side of the river!")
    p.add_tools(HoverTool(tooltips=hover_info))
    p.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, source=source)

    show(p)
