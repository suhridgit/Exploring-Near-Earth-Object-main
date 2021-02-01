"""A database encapsulating collections of near-Earth objects and their close approaches.

A `NEODatabase` holds an interconnected data set of NEOs and close approaches.
It provides methods to fetch an NEO by primary designation or by name, as well
as a method to query the set of close approaches that match a collection of
user-specified criteria.

Under normal circumstances, the main module creates one NEODatabase from the
data on NEOs and close approaches extracted by `extract.load_neos` and
`extract.load_approaches`.

You'll edit this file in Tasks 2 and 3.
"""


def get_linked_approaches_neos(neos, approaches):
    """Link neos and approaches objects
    Each `CloseApproach` has an attribute (`._designation`) that
    matches the `.designation` attribute of the corresponding NEO. This
    function modifies the supplied NEOs and close approaches to link them
    together and return linked neos, approaches collection.
    :param neos: A collection of `NearEarthObject`s.
    :param approaches: A collection of `CloseApproach`es.
    """
    neoList = {}
    approachList = []
    for approach in approaches:
        for neo in neos:
            if neo.designation == approach._designation:
                approach.neo = neo
                if neo.designation in neoList:
                    neoList[neo.designation].approaches.append(approach)
                else:
                    neo.approaches.append(approach)
                    neoList[neo.designation] = neo
                break
        approachList.append(approach)
    for neo in neos:
        if neo.designation not in neoList:
            neoList[neo.designation] = neo

    return (neoList.values(), approachList)


class NEODatabase:
    """A database of near-Earth objects and their close approaches.

    A `NEODatabase` contains a collection of NEOs and a collection of close
    approaches. It additionally maintains a few auxiliary data structures to
    help fetch NEOs by primary designation or by name and to help speed up
    querying for close approaches that match criteria.
    """
    def __init__(self, neos, approaches):
        """Create a new `NEODatabase`.

        As a precondition, this constructor assumes that the collections of NEOs
        and close approaches haven't yet been linked - that is, the
        `.approaches` attribute of each `NearEarthObject` resolves to an empty
        collection, and the `.neo` attribute of each `CloseApproach` is None.

        However, each `CloseApproach` has an attribute (`._designation`) that
        matches the `.designation` attribute of the corresponding NEO. This
        constructor modifies the supplied NEOs and close approaches to link them
        together - after it's done, the `.approaches` attribute of each NEO has
        a collection of that NEO's close approaches, and the `.neo` attribute of
        each close approach references the appropriate NEO.

        :param neos: A collection of `NearEarthObject`s.
        :param approaches: A collection of `CloseApproach`es.
        """
        # neos.sort(key=lambda x: x.designation)
        # approaches.sort(key=lambda x: x.designation)

        # self._neos = neos
        # self._approaches = approaches
        #
        # i = 0
        # j = 0
        #
        # while i < len(neos) and j < len(approaches):
        #     neo = neos[i]
        #     approach = approaches[j]
        #     if neo.designation == approach.designation:
        #         neo.append(approach)
        #         approach.attach(neo)
        #         j += 1
        #     else:
        #         i += 1

        self.neos_name_dict = {}
        self.neos_designation_dict = {}
        self._neos, self._approaches = get_linked_approaches_neos(neos, approaches)
        for neo in self._neos:
            if neo.name:
                self.neos_name_dict[neo.name] = neo
            self.neos_designation_dict[neo.designation] = neo

    def get_neo_by_designation(self, designation):
        """Find and return an NEO by its primary designation.

        If no match is found, return `None` instead.

        Each NEO in the data set has a unique primary designation, as a string.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param designation: The primary designation of the NEO to search for.
        :return: The `NearEarthObject` with the desired primary designation, or `None`.
        """

        for neo in self._neos:
            if neo.designation == designation:
                return neo
        return None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name.

        If no match is found, return `None` instead.

        Not every NEO in the data set has a name. No NEOs are associated with
        the empty string nor with the `None` singleton.

        The matching is exact - check for spelling and capitalization if no
        match is found.

        :param name: The name, as a string, of the NEO to search for.
        :return: The `NearEarthObject` with the desired name, or `None`.
        """
        for neo in self._neos:
            if neo.neo_name == name:
                return neo
        return None

    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters.

        This generates a stream of `CloseApproach` objects that match all of the
        provided filters.

        If no arguments are provided, generate all known close approaches.

        The `CloseApproach` objects are generated in internal order, which isn't
        guaranteed to be sorted meaninfully, although is often sorted by time.

        :param filters: A collection of filters capturing user-specified criteria.
        :return: A stream of matching `CloseApproach` objects.
        """
        for approach in self._approaches:
            flag = False in map(lambda f: f(approach), filters)
            if flag == False:
                yield approach
