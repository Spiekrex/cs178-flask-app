# author: T. Urness and M. Moore
# description: Flask example using redirect, url_for, and flash
# credit: the template html files were constructed with the help of ChatGPT

from flask import Flask
from flask import render_template
from flask import Flask, render_template, request, redirect, url_for, flash
from dbCode import *

app = Flask(__name__)
app.secret_key = 'your_secret_key'


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/display-countries')
def display_countries():
    country_list = get_countries()
    return render_template('display_countries.html', country=country_list)


# -------------------------
# CREATE
# -------------------------
@app.route('/add-city', methods=['GET', 'POST'])
def add_city_route():
    if request.method == 'POST':
        name = request.form['name']
        countrycode = request.form['countrycode']
        district = request.form['district']
        population = request.form['population']

        try:
            add_city(name, countrycode, district, population)
            flash('City added successfully!', 'success')
            return redirect(url_for('biggest_cities'))
        except Exception as e:
            flash(f'Error adding city: {e}', 'danger')
            return redirect(url_for('add_city_route'))

    countries = get_country_codes()
    return render_template('add_city.html', countries=countries)


# -------------------------
# READ
# -------------------------
@app.route('/biggest-cities')
def biggest_cities():
    cities = get_biggest_cities()
    return render_template('biggest_cities.html', cities=cities)


# -------------------------
# UPDATE
# -------------------------
@app.route('/update-city/<int:city_id>', methods=['GET', 'POST'])
def update_city_route(city_id):
    city = get_city_by_id(city_id)

    if not city:
        flash('City not found.', 'warning')
        return redirect(url_for('biggest_cities'))

    if request.method == 'POST':
        name = request.form['name']
        district = request.form['district']
        population = request.form['population']

        try:
            update_city(city_id, name, district, population)
            flash('City updated successfully!', 'success')
            return redirect(url_for('biggest_cities'))
        except Exception as e:
            flash(f'Error updating city: {e}', 'danger')
            return redirect(url_for('update_city_route', city_id=city_id))

    return render_template('update_city.html', city=city)


# -------------------------
# DELETE
# -------------------------
@app.route('/delete-city/<int:city_id>', methods=['POST'])
def delete_city_route(city_id):
    try:
        deleted = delete_city(city_id)
        if deleted:
            flash('City deleted successfully!', 'warning')
        else:
            flash('City not found.', 'warning')
    except Exception as e:
        flash(f'Error deleting city: {e}', 'danger')

    return redirect(url_for('biggest_cities'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)