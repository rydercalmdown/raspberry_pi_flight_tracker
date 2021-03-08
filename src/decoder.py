import os
import json
import time

current_aircraft = []


def get_data_directory_path():
    """Return the path of the data directory"""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, '../data')


def clean_up_directory():
    """Cleans up the JSON directory"""
    for file_name in os.listdir(get_data_directory_path()):
        if file_name.startswith('history_'):
            os.remove(os.path.join(get_data_directory_path(), file_name))


def get_aircraft():
    """Retrieving aircraft from dump1090 json output"""
    clean_up_directory()
    print('getting aircraft at {}'.format(str(int(time.time()))))
    json_path = os.path.join(get_data_directory_path(), 'aircraft.json')
    with open(json_path) as file:
        aircraft_json = json.loads(file.read())
    print('{} found'.format(len(aircraft_json['aircraft'])))
    return aircraft_json['aircraft']
