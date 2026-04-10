# Biggest Cities by percentage

**CS178: Cloud and Database Systems — Project #1**
**Author:** [Rex Spieker]
**GitHub:** [Spiekrex]

---

## Overview

This project shows the cities that have the highest percent of their countries population, ordered by percent. I thought it would be interesting to see what cities are the highest amount of their countries population. 
---

## Technologies Used

- **Flask** — Python web framework
- **AWS EC2** — hosts the running Flask application
- **AWS RDS (MySQL)** — relational database for cities and their percentage of country population
- **GitHub Actions** — auto-deploys code from GitHub to EC2 on push

---

## Project Structure

```
ProjectOne/
├── flaskapp.py          # Main Flask application — routes and app logic
├── dbCode.py            # Database helper functions (MySQL connection + queries)
├── creds_sample.py      # Sample credentials file (see Credential Setup below)
├── templates/
│   ├── home.html        # Landing page
│   ├── [other].html     # Add descriptions for your other templates
├── .gitignore           # Excludes creds.py and other sensitive files
└── README.md
```

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

2. Install dependencies:

   ```bash
   pip3 install flask pymysql boto3
   ```

3. Set up your credentials (see Credential Setup below)

4. Run the app:

   ```bash
   python3 flaskapp.py
   ```

5. Open your browser and go to `http://127.0.0.1:8080`

---

## How to Access in the Cloud

The app is deployed on an AWS EC2 instance. To view the live version:

```
http://127.0.0.1:8080
```

_(Note: the EC2 instance may not be running after project submission.)_

---

## Credential Setup

This project requires a `creds.py` file that is **not included in this repository** for security reasons.

Create a file called `creds.py` in the project root with the following format (see `creds_sample.py` for reference):

```python
# creds.py — do not commit this file
host = "cs178-chinook.cn9nbw41gsla.us-east-1.rds.amazonaws.com"
user = "admin"
password = "I<3Cloud!"
db = "world"
```

---

## Database Design

### SQL (MySQL on RDS)

The relational database for this project uses the world database schema hosted on MySQL in Amazon RDS.

country stores information about countries such as country code, name, continent, and total population. Primary key is code
city stores information about cities such as city name, district, population, and the country the city belongs to. Primary key is id
city.countrycode is a foreign key that links each city to country.code


- `[TableName]` — stores [description]; primary key is `[key]`
- `[TableName]` — stores [description]; foreign key links to `[other table]`

The JOIN query used in this project: Combines the city and country tables so the website can display each city along with the country it belongs to

### DynamoDB

<!-- Describe your DynamoDB table. What is the partition key? What attributes does each item have? How does it connect to the rest of the app? -->

- **Table name:** `[your-table-name]`
- **Partition key:** `[key-name]`
- **Used for:** [description]

---

## CRUD Operations

| Operation | Route      | Description    |
| --------- | ---------- | -------------- |
| Create    | `/[add_city]` | [Displays a form and inserts a new city into the MySQL city table] |
| Read      | `/[biggest_cities]` | [Retrieves cities using a SQL JOIN between city and country and displays the cities with the highest percentage of their country's population] |
| Update    | `/[update_city]` | [Loads a selected city, displays an edit form, and updates the city in the database] |
| Delete    | `/[delete-city]` | [Deletes the selected city from the MySQL city table] |

---

## Challenges and Insights

I shouldn't have procrastinated so much, I had to go back and look at the previous labs to recall how to work with SQl and get it working for this lab. I'll definitely start earlier for the next project so I'm not rushing it out like this. I had to decide what I wanted to focus on to try and get the most points possible since I ran out of time to finish everything.
---

## AI Assistance

I used ChatGPT to help with the styling of the website. I wanted it to look better, but my HTML was not good enough for what I wanted it to look like, so I had ChatGPT help polish the design. I also used it to try and fix my automatic deploying which was being problematic, though I eventually fixed it by simply deleting and reforking the project.