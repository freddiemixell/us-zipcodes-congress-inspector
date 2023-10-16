from lookup import CongressionalDistrictLookup

if __name__ == "__main__":
    lookup = CongressionalDistrictLookup('zccd.csv')
    districts_by_zip = lookup.by_zipcode('17552')
    if districts_by_zip:
        # Get the first district (state, cd) tuple from the list
        state, cd = districts_by_zip[0]
        zips_by_district = lookup.by_district(state, cd)
        print(f'Districts By Zipcode: {districts_by_zip}')
        print(f'Zips by District: {zips_by_district}')



