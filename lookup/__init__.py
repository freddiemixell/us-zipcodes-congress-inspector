import utils

class CongressionalDistrictLookup:
    """A class to look up congressional districts by zip code and vice versa."""

    def __init__(self, filename):
        """Initialize the lookup with data from the specified file."""
        self.zip_to_cd = self._load_zip_to_cd_mapping(filename)
        self.cd_to_zip = self._load_cd_to_zip_mapping(filename)

    def _load_zip_to_cd_mapping(self, filename):
        """Load a mapping from zip codes to congressional districts from a CSV file."""
        data = utils.load_csv_columns(filename)
        zip_to_cd = {}
        for row in data:
            zip_code = row['zcta']
            state = row['state_abbr']
            cd = row['cd']
            if zip_code not in zip_to_cd:
                zip_to_cd[zip_code] = []
            zip_to_cd[zip_code].append((state, cd))
        return zip_to_cd
    
    def _load_cd_to_zip_mapping(self, filename):
        """Load a mapping from congressional districts to zip codes from a CSV file."""
        data = utils.load_csv_columns(filename)
        cd_to_zip = {}
        for row in data:
            zip_code = row['zcta']
            state = row['state_abbr']
            cd = row['cd']
            key = (state, cd)
            if key not in cd_to_zip:
                cd_to_zip[key] = []
            cd_to_zip[key].append(zip_code)
        return cd_to_zip
    
    def get_all_districts(self):
        """Return all the congressional districts."""
        return list(self.cd_to_zip.keys())

    def by_zipcode(self, zip_code):
        """Return the congressional district(s) for a given zip code."""
        if zip_code in self.zip_to_cd:
            return self.zip_to_cd[zip_code]
        else:
            return None

    def by_district(self, state, cd):
        """Return the zip code(s) for a given state and congressional district."""
        key = (state, cd)
        if key in self.cd_to_zip:
            return self.cd_to_zip[key]
        else:
            return None