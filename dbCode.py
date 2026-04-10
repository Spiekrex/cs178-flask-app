# dbCode.py
# Author: Rex Spieker
# Helper functions for database connection and queries

import pymysql
import creds

def get_conn():
    """Returns a connection to the MySQL RDS instance."""
    return pymysql.connect(
        host=creds.host,
        user=creds.user,
        password=creds.password,
        db=creds.db,
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )

def execute_query(query, args=()):
    """Executes a SELECT query and returns all rows as dictionaries."""
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query, args)
            rows = cur.fetchall()
        return rows
    finally:
        conn.close()

def execute_action(query, args=()):
    """Executes INSERT, UPDATE, or DELETE queries."""
    conn = get_conn()
    try:
        with conn.cursor() as cur:
            cur.execute(query, args)
            return cur.rowcount
    finally:
        conn.close()


# -------------------------
# COUNTRY HELPERS
# -------------------------

def get_countries():
    query = """
        SELECT name
        FROM country
        LIMIT 20
    """
    return execute_query(query)

def get_country_codes():
    query = """
        SELECT code, name
        FROM country
        ORDER BY name
    """
    return execute_query(query)


# -------------------------
# CITY CRUD
# -------------------------

def add_city(name, countrycode, district, population):
    query = """
        INSERT INTO city (name, countrycode, district, population)
        VALUES (%s, %s, %s, %s)
    """
    return execute_action(query, (name, countrycode, district, population))

def get_biggest_cities():
    query = """
        SELECT
            ci.id,
            ci.name AS city_name,
            ci.district,
            ci.population AS city_population,
            co.code AS country_code,
            co.name AS country_name,
            co.continent,
            co.population AS country_population,
            ROUND((ci.population / NULLIF(co.population, 0)) * 100, 2) AS country_pop_percent
        FROM city ci
        JOIN country co
            ON ci.countrycode = co.code
        WHERE ci.population IS NOT NULL
          AND co.population IS NOT NULL
          AND co.population > 0
        ORDER BY country_pop_percent DESC, ci.population DESC
        LIMIT 50
    """
    return execute_query(query)

def get_city_by_id(city_id):
    query = """
        SELECT id, name, countrycode, district, population
        FROM city
        WHERE id = %s
    """
    rows = execute_query(query, (city_id,))
    if rows:
        return rows[0]
    return None

def update_city(city_id, name, district, population):
    query = """
        UPDATE city
        SET name = %s,
            district = %s,
            population = %s
        WHERE id = %s
    """
    return execute_action(query, (name, district, population, city_id))

def delete_city(city_id):
    query = """
        DELETE FROM city
        WHERE id = %s
    """
    return execute_action(query, (city_id,))
