import click
import os
import requests
import uuid

from tqdm import tqdm


# Bounding boxes limit extracted from https://nominatim.openstreetmap.org/
bounding_boxes = {
    'ile-de-france': (-0.06592, 49.58223, 5.07568, 47.76887),
    'paris': (2.18628, 48.91528, 2.50763, 48.80234),
    'lyon': (4.67434, 45.81779, 4.99569, 45.69803),
    'bourg-saint-maurice': (6.44005, 45.78381, 7.08275, 45.54387)
}


def _format_request(bbox_tuple, nb_traces=10):
    """Format OSM API v0.6 queries to get public GPS traces in a given area.

    The bbox_tuple determines the bounding box area (cf. OSM documentation
    https://wiki.openstreetmap.org/wiki/API_v0.6#GPS_traces).

    Args:
        bbox_tuple (tuple): Bounding box limit (left, bottom, right, and top)
        are the gps coordinates of the bounding box
        nb_traces (int): Number of traces to get.

    Returns:
        array: a list of length <nb_traces> of OSM API requests.
    """
    request_list = []
    osm_api_path = 'https://api.openstreetmap.org'
    left = bbox_tuple[0]
    top = bbox_tuple[1]
    right = bbox_tuple[2]
    bottom = bbox_tuple[3]
    for pageNumber in range(int(nb_traces)):
        request_list.append("{api_path}/api/0.6/trackpoints?bbox={left},{bottom},{right},{top}&page={pageNumber}".format(
            left=left, right=right, bottom=bottom, top=top,
            pageNumber=pageNumber, api_path=osm_api_path))
    return request_list


def _write_gpx_trace(output_file, content, output_dir='gpx_traces'):
    """ Writes GPX traces into output_file from request content into an
        output_dir.

    Args:
        output_file (str): Output file name should end with .gpx
        content (bytes): Content of an OSM API request
        output_dir(str): Output directory of where output_file will be written
    Returns:
        None
    """
    with open('{}/{}'.format(output_dir, output_file), 'w') as of:
        splits = str(content).split('\\n')
        len_splits = len(splits)
        for split in splits:
            print(split, len(split))
        for index, item in enumerate(splits):
            if index == 0:
                of.write(str(item)[2:] + '\n')
            else:
                if len(item) > 1:
                    of.write(str(item) + '\n')


@click.command()
@click.option('--nb_traces', default=2, prompt='Number of traces ?', help='Number of gpx traces.')
@click.option('--city_name', default='lyon',
              prompt='City Name? ({})'.format(', '.join(bounding_boxes.keys())),
              help='City name / examples: [{}].'.format(', '.join(bounding_boxes.keys())))
@click.option('--output_dir', default='gpx_traces',
            help='Directory for downloaded traces.')
def collect_traces(nb_traces, city_name, output_dir='gpx_traces'):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    requests_list = _format_request(
            bounding_boxes[city_name.lower()], nb_traces)
    for request_to_send in tqdm(requests_list):
        r = requests.get(request_to_send)
        output_file_name = 'trace_{}_{}.gpx'.format(
            city_name, uuid.uuid1(), output_dir)
        _write_gpx_trace(output_file_name, r.content, output_dir)


if __name__ == '__main__':
    collect_traces()
