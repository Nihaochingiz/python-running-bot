# Bot Documentation

## Introduction
This bot is designed to receive messages from users containing distance and time data in a specific format and store it in a PostgreSQL database.



## Setup Instructions
1. Make sure you have Python installed on your machine.
2. Install the required Python packages using the following command:

```
pip install python-telegram-bot python-dotenv psycopg2-binary
```
3. Create a `.env` file in the same directory as your script and add the following environment variables with your specific values:
```
BOT_TOKEN=your_token
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="postgres"
DB_USER="postgres"
DB_PASSWORD="0000"
```
4. You need to set up a PostgreSQL database and store the connection information in a `.env` file in the same directory as your script. Include the following keys:
- `DB_NAME`
- `DB_USER`
- `DB_HOST`
- `DB_PORT`
- `DB_PASSWORD`

...

## Database Module (db.py)
### Description
The `db.py` module handles database operations for storing running statistics data.

### Functions
- `init_table()`: Creates the `running_statistics` table if it doesn't exist.
- `create_record(km, minutes, date)`: Inserts a new record into the `running_statistics` table.
- `read_all_records()`: Fetches and displays all records from the `running_statistics` table.

### Database Schema
The `running_statistics` table schema:
- `id`: SERIAL PRIMARY KEY
- `kilometers`: FLOAT
- `minutes`: INTEGER
- `date`: DATE

### Database Connection
The module establishes a connection to a PostgreSQL database using the provided environment variables for connection details.

### Usage Example
1. The `init_table()` function initializes the `running_statistics` table.
2. You can create a new record using the `create_record(km, minutes, date)` function.
3. Use the `read_all_records()` function to display all records in the `running_statistics` table.

### Author
- ilya.fofanov