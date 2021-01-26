"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    print ('load neos function called')
    output = []
    # TODO: Load NEO data from the given CSV file.
    with open(neo_csv_path, 'r') as fileObject:
        reader = csv.DictReader(fileObject)
        for elem in reader:
            diameterValue = float('nan')
            nameValue = None
            if (elem['diameter'] != '' and elem['diameter'] != None):
                diameterValue = float(elem['diameter'])
            if (elem['name'] != '' and elem['name'] != None):
                nameValue = elem['name']
            output.append(NearEarthObject(
                pdesignation = elem['pdes'], name = nameValue,
                hazardous = elem['pha'], diameter = diameterValue))
    print ('neos data loaded')
    return output


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    """         {'pdes':elem['pdes'], 'name': elem['name'], 'phs': elem['pha'], 'diameter': elem['diameter']} """
    print ('load approaches function called')
    closeApproach = []
    # TODO: Load NEO data from the given CSV file.
    with open(cad_json_path, 'r') as fileObject:
        approachesObj = json.load(fileObject)
        for approach in approachesObj['data']:
            closeApproach.append(CloseApproach(
                approach[0], time=approach[3],
                distance=float(approach[4]), velocity=float(approach[7])))
    print ('approaches data loaded')
    return closeApproach
    # TODO: Load close approach data from the given JSON file.
