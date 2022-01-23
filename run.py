#!/usr/bin/env python3.6
from accounts import Accounts
from passwords import Password


def create_account(first_name, last_name, user_name, password):
    accounts = Accounts(first_name, last_name, user_name, password)
    return accounts


def save_account(accounts):
    accounts.save_account()


def delete_account(accounts):
    accounts.delete_account()


def find_accounts(user_name):
    return Accounts.find_by_user_name(user_name)


def isexist_accounts(user_name):
    return Accounts.account_exists(user_name)


def display_accounts():
    return Accounts.display_accounts()


def create_page(page, password):
    passwords = Password(page, password)
    return passwords


def save_page(passwords):
    passwords.save_page()


def find_page(pager):
    return Password.find_by_page(pager)


def isexist_page(pager):
    return Password.page_exists(pager)


def delete_page(passwords):
    passwords.delete_page()


def display_pages():
    return Password.display_page()
