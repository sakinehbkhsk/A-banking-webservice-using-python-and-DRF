from django.test import TestCase


from decimal import Decimal

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Customer, Account


class BankingAPITest(APITestCase):

    def setUp(self):
        """
        This method runs before each test.
        Create a customer for our tests.
        """
        self.customer = Customer.objects.create(
            first_name="Ali",
            last_name="bakhshi"
        )

    # Test 1: Creating an account
    def test_create_account(self):
        url = reverse("account-create")
        data = {"account_no": "5000", "customer_no": self.customer.id}
        response = self.client.post( url, data, format="json")
        self.assertEqual( response.status_code, status.HTTP_201_CREATED)
        self.assertTrue( Account.objects.filter(account_no="5000").exists() )

    # Test 2: Retrieving a non-existing account
    def test_retrieve_non_existing_account(self):
        url = reverse( "account_detail", kwargs={"account_no": "9999"})
        response = self.client.get(url)
        self.assertEqual( response.status_code, status.HTTP_404_NOT_FOUND )

    # Test 3: Attempting to debit a blocked account
    def test_debit_blocked_account(self):

        account = Account.objects.create( account_no="6000", customer=self.customer, account_status=Account.AccountStatus.BLOCKED, account_balance=Decimal("1000.00"))
        url = reverse( "debit_account", kwargs={"account_no": account.account_no})
        data = {
            "amount": "200.00"
        }

        response = self.client.post( url, data, format="json")
        self.assertEqual( response.status_code, status.HTTP_403_FORBIDDEN)
        account.refresh_from_db()
        self.assertEqual( account.account_balance, Decimal("1000.00"))

