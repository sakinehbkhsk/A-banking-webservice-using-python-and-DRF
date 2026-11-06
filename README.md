
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


## API Endpoints

All API endpoints use the following base URL:

```text
http://127.0.0.1:8000/api/
```

### Customer Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | `/api/customers/create/` | Create a new customer |
| GET | `/api/customers/` | Retrieve all customers |
| GET | `/api/customers/{customer_no}/` | Retrieve customer details |
| GET | `/api/customers/{customer_no}/accounts/` | Retrieve all accounts belonging to a customer |

### Account Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | `/api/accounts/create/` | Create a new account |
| GET | `/api/accounts/` | Retrieve all accounts |
| GET | `/api/accounts/{account_no}/` | Retrieve account details |

### Transaction Endpoints

| HTTP Method | Endpoint | Description |
|---|---|---|
| POST | `/api/accounts/{account_no}/credit/` | Deposit money into an account |
| POST | `/api/accounts/{account_no}/debit/` | Withdraw money from an account |

### Example Requests

**1. Create a Customer**

`POST /api/customers/create/`

```json
{
    "first_name": "Ali",
    "last_name": "Ahmadi"
}
```

**2. Create an Account**

`POST /api/accounts/create/`

```json
{
    "account_no": "5000",
    "customer_no": 1
}
```

**3. Credit an Account**

`POST /api/accounts/5000/credit/`

```json
{
    "amount": "1000.00"
}
```

**4. Debit an Account**

`POST /api/accounts/5000/debit/`

```json
{
    "amount": "300.00"
}
```


### Running Tests

Run the automated API tests using:

```bash
python manage.py test banking
```

The tests cover:
- Creating an account.
- Retrieving a non-existing account.
- Attempting to debit a blocked account.









