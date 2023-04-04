import hashlib
import os
import secrets
import rsa
import functools
from flask import redirect, url_for
from auth.models import User, BlacklistToken

class Account:
  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email


# Procedures

def get_id(reference):
      """ fetches the id of a user by their name or email """
  


def authenticate(id, salted_hash):
  """ checks if the provided password hash is the correct hash for the user with given id """

def register(name, email, unsalted_hash):
  """ registers a user with given name and email; generates a salt and a salted hash for that user to save their password """
  id = secrets.randbits(64)
  final_hash = encrypt(unsalted_hash)

def set_username(id, name):
  """ updates the stored username for a given user """

def set_email(id, email):
  """ updates the stored email for a given user """

def set_password(id, unsalted_hash):
  """ updates the stored password for a given user """

def remove_user(id):
  """ removes an account from the database """

def is_refresh_jwt():
  pass

def get_global_salt():
  """ standin """
  return '17de4'


# Functions

def get_secret():
  return os.urandom(24)

def encrypt(unsalted_hash, salt):
  """ salt and hash a received password hash """
  final_hash = hashlib.sha512()
  global_salt = get_global_salt()
  return final_hash.update(unsalted_hash+salt+global_salt).hex_digest()


#login dependent decorators
def login_dependent(view):
  @functools.wraps(view)
  def wrapped_view(**kwargs):
        if is_refresh_jwt() is None:
          return redirect(url_for('login'))
        return view(**kwargs)