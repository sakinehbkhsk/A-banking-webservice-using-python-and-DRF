
  # **  Account Management API**
  A RESTful Banking Web Service developed using Python, Django REST Framework.
  This project provides basic banking operations, including customer management, create an account and credit/debit transactions.

##  Technologies
- Python
- Django
- Django Rest Framework
- SQlite
- Git and Github
- Postman or Thunder Client (API testing)

## Project Features
- Customer creation and management
- Bank account creation
- Assigning multiple accounts to a customer
- Retrieving customer and account information
- Checking account status
- Credit (deposit) operations
- Debit (withdrawal) operations

## Business rules
- An available account could be debit or credit
- A debit/credit amount must be positive value
- Debit amount must be less than or equal to account balance
- An account could be debit if it's status is OPEN
- An account could be credit if it's status is not CLOSED

## Build the Project

### 1. Clone the Repository (master branch)
git clone https://github.com/sakinehbkhsk/A-banking-webservice-using-python-and-DRF.git

### 2. Create Virtual Enviornment
python -m venv venv

### 3. Activate Virtual Enviornment
venv\Scripts\activate

### 4. Install Dependencies
pip install -r requirements.txt

## Database Configuration

This project uses SQlite as its default database.
The database configuration is defined in settings.py


## Run the Project

- python manage.py makemigrations
- python manage.py migrate
- python manage.py runserver
- The server will run at: http://127.0.0.1:8000


## API Endpoints and Examples

| POST | api/customers/ | create_customer |
| GET | api/customers/all | all_customers |

| POST | api/accounts/ | create_account |
| GET |  api/accounts/all  | all_accounts |

| POST | api/accounts/5000/credit/ | credit_account |
|  POST | api/accounts/5000/debit/ | debit_account |









