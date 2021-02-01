"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, designation = '', name = None, diameter = float('nan'), hazardous = "N"):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self._designation = designation

        if name:
            self.name = name
        else:
            self.name = None

        if diameter:
            self.diameter = float(diameter)
        else:
            self.diameter = float('nan')

        if hazardous == 'Y':
            self.hazardous = True
        else:
            self.hazardous = False

        self.approaches = list()

    @property
    def neo_name(self):
        return self.name

    def append(self, item):
        if type(item) == CloseApproach:
            self.approaches.append(item)


    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f"{self.designation} {self.name}" \
            if (self.name != '' and isinstance(self.name,str)) else f"{self.designation}"

    def __getitem__(self, index):
        return self[index]

    @property
    def designation(self):
        return self._designation

    @property
    def time_str(self):
        return datetime_to_str(self.time)


    def __str__(self):
        """Return `str(self)`."""
        return f'A NearEarthObject {self.fullname} has a diameter of {self.diameter: .3f} km and  ' \
               f'{  "is" if self.hazardous else "is not "} hazardous'


    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")

    def serialize(self):
        """Return serialized dictionary data to write in CSV and JSON file"""
        name = self.name if self.name != None else ''
        return {'designation': self.designation, 'name': name, 'diameter_km': self.diameter,
                'potentially_hazardous': self.hazardous}


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initally, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    def __init__(self, designation,time,distance,velocity,neo = None):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self._designation = designation
        if type(time) == str:
            self.time = cd_to_datetime(time)

        if type(distance) == float:
            self.distance = distance
        else:
            self.distance = float(distance)

        if type(velocity) == float:
            self.velocity = velocity
        else:
            self.velocity = float(velocity)

        if neo:
            self.neo = neo
        else:
            self.neo = None

    def __getitem__(self, index):
        return self[index]

    @property
    def designation(self):
        return self._designation

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def attach(self, neo):
        if type(neo) == NearEarthObject:
            self.neo = neo

    def __str__(self):
        return f"At {self.time_str}, '{self.designation}' approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s. Hazardous: {self.neo.hazardous}"

    def __repr__(self):
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f})")

    def serialize(self):
        """Return serialized dictionary data to write in CSV and JSON file"""
        return {'datetime_utc': datetime_to_str(self.time), 'distance_au': self.distance,
                'velocity_km_s': self.velocity, 'neo': self.neo.serialize()}
