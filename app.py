from flask_api import app

# import for faker file for seed data
from faker_seed_db import seedData

if __name__ == '__main__':
    app.run(debug=True)
    # seedData()
    # uncomment if you want to add more patient data to your database