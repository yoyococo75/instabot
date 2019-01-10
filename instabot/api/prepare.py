#!/usr/bin/env python

import getpass
import os
import sys

from .. import models

SECRET_FILE = "secret.txt"


def add_credentials_txt():
    with open(SECRET_FILE, "a") as f:
        print("Enter your login: ")
        f.write(str(sys.stdin.readline().strip()) + ":")
        print("Enter your password: ")
        f.write(getpass.getpass() + "\n")


def add_credentials_db():
    print("Enter your login: ")
    username = str(sys.stdin.readline().strip())
    print("Enter your password: ")
    password = getpass.getpass()

    models.InstabotUser.create(username=username, password=password)


def txt_credentials(username):
    while not check_secret():
        pass
    while True:
        try:
            with open(SECRET_FILE, "r") as f:
                lines = [line.strip().split(":", 2) for line in f.readlines()]
        except ValueError:
            msg = "Problem with opening `{}`, will remove the file."
            raise Exception(msg.format(SECRET_FILE))
        if username is not None:
            for login, password in lines:
                if login == username.strip():
                    return login, password
        print("Which account do you want to use? (Type number)")
        for ind, (login, password) in enumerate(lines):
            print("%d: %s" % (ind + 1, login))
        print("%d: %s" % (0, "add another account."))
        print("%d: %s" % (-1, "delete all accounts."))
        try:
            ind = int(sys.stdin.readline())
            if ind == 0:
                add_credentials_txt()
                continue
            elif ind == -1:
                delete_credentials(use_db=False)
                check_secret()
                continue
            elif 0 <= ind - 1 < len(lines):
                return lines[ind - 1]
        except Exception:
            print("Wrong input, enter the number of the account to use.")


def get_credentials(username=None, use_db=False):
    """Returns login and password stored in `secret.txt`."""
    if not use_db:
        return txt_credentials(username)

    while True:
        if username is not None:
            user = (
                models.InstabotUser.select()
                .where(models.InstabotUser.username == username)
                .first()
            )

            if user:
                return user.username, user.password

        users = models.InstabotUser.select()
        users_map = {}
        print("Which account do you want to use? (Type number)")

        for ind, user in enumerate(users, start=1):
            print("%d: %s" % (ind, user.username))
            users_map[ind] = user

        print("%d: %s" % (0, "add another account."))
        print("%d: %s" % (-1, "delete all accounts."))

        try:
            ind = int(sys.stdin.readline())
            if ind == 0:
                add_credentials_db()
                continue
            elif ind == -1:
                delete_credentials(use_db=False)
                continue
            elif ind in users_map.keys():
                user = users_map[ind]
                return user.username, user.password
        except Exception:
            print("Wrong input, enter the number of the account to use.")


def check_secret():
    while True:
        if os.path.exists(SECRET_FILE):
            with open(SECRET_FILE, "r") as f:
                try:
                    login, password = f.readline().strip().split(":")
                    if len(login) < 4 or len(password) < 6:

                        print(
                            "Data in `secret.txt` file is invalid. "
                            "We will delete it and try again."
                        )

                        os.remove(SECRET_FILE)
                    else:
                        return True
                except Exception:
                    print("Your file is broken. We will delete it " "and try again.")
                    os.remove(SECRET_FILE)
        else:
            print(
                "We need to create a text file '%s' where "
                "we will store your login and password from Instagram." % SECRET_FILE
            )
            print("Don't worry. It will be stored locally.")
            while True:
                add_credentials_db()
                print("Do you want to add another account? (y/n)")
                if "y" not in sys.stdin.readline():
                    break


def delete_credentials(use_db):
    if use_db:
        delete_credentials_db()
    else:
        delete_credentials_txt()


def delete_credentials_txt():
    if os.path.exists(SECRET_FILE):
        os.remove(SECRET_FILE)


def delete_credentials_db():
    models.InstabotUser.delete().execute()


if __name__ == "__main__":
    check_secret()
