# osm2gpx.py: public GPS traces collection from OSM

_Script to collect public GPS data from the [OSM API (0.6)](https://wiki.openstreetmap.org/wiki/API_v0.6#GPS_traces) around a given area._

## Requirements 

- `Python 3.7`
- `Click`
- `requests`
- `tqdm`

		$ pip install -r requirements.txt
	
## Usage

```	 
Usage: osm2gpx.py [OPTIONS]

Options:
  --nb_traces INTEGER  Number of gpx traces.
  --city_name TEXT     City name / examples: [ile-de-france, paris, lyon,
                       bourg-saint-maurice].
  --output_dir TEXT    Directory for downloaded traces.
  --help               Show this message and exit.
```
 	  
We can find traces in the `gpx_traces` directory by default. Traces naming follows this pattern:

	{output_dir}/trace_{city_name}_{uuid}.gpx
		
where `uuid` is based on the host ID and current time. 

We use uuid to avoid overwriting previous traces.
  	  
Note: as of now, bounding box coordinates are hardcoded in the script. An evolution could take them as coordinates :)

### Example

- Get 5 gpx traces in Paris from OSM
  	  
		python osm2gpx.py --nb_traces 5 --city_name paris
