# osm2gpx.py: public GPS traces collection from OSM

_Script to collect public GPS data from the [OSM API (0.6)](https://wiki.openstreetmap.org/wiki/API_v0.6#GPS_traces) around a given area._

## Requirements 

- Python 3.6
- Click
- requests
- tqdm

		$ pip install -r requirements.txt
	
## Usage

	 
	Usage: osm2gpx.py [OPTIONS]
	
	Options:
	  --nb_traces INTEGER  Number of gpx traces (default: 10).
	  --city_name TEXT     Examples: [ile-de-france, paris, lyon, bourg-saint-maurice]
  	  --help               Show this message and exit.
  	  
 As of now, bounding box coordinates are hardcoded in the script. An evolution could take them as coordinates :)

### Example

- Get 5 gpx traces in Paris from OSM
  	  
		python osm2gpx.py --nb_traces 5 --city_name paris
