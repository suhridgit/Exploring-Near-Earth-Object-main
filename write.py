"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json


def write_to_csv(results, filename):

    fieldnames = ('datetime_utc',
                  'distance_au',
                  'velocity_km_s',
                  'designation',
                  'name',
                  'diameter_km',
                  'potentially_hazardous')
    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for elem in results:
            approach_dict = elem.serialize()
            neo_dict = elem.neo.serialize()
            csv_dict = merge(approach_dict, neo_dict)
            csv_dict.pop('neo')
            writer.writerow(csv_dict)


def merge(dict1, dict2):

    res = {**dict1, **dict2}
    return res


def write_to_json(results, filename):

    output = [approach.serialize() for approach in results]
    with open(filename, 'w') as outfile:
        json.dump(output, outfile, indent=2)
