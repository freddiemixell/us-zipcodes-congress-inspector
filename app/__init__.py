from flask import Flask, render_template, request
from lookup import CongressionalDistrictLookup

app = Flask(__name__)
lookup = CongressionalDistrictLookup('zccd.csv')

@app.route('/')
def home():
    # Fetch the list of available districts
    districts = lookup.get_all_districts()
    return render_template('home.html', districts=districts)

@app.route('/lookup', methods=['POST'])
def lookup_zip():
    zip_code = request.form['zip']
    districts = lookup.by_zipcode(zip_code)
    results = []
    for state, cd in districts:
        zips = lookup.by_district(state, cd)
        results.append((state, cd, zips))
    return render_template('result.html', districts=results)

@app.route('/lookup_district', methods=['POST'])
def lookup_district():
    district = request.form['district']
    # Split the district into the state and district number
    state, cd = district.split('-')
    zips = lookup.by_district(state, cd)
    return render_template('result.html', districts=[(state, cd, zips)])

if __name__ == '__main__':
    app.run(debug=True)