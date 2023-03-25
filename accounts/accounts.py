import hashlib
import secrets

class Account:
  def __init__(self, id, name, email):
    self.id = id
    self.name = name
    self.email = email



def get_id(reference):
  """ fetches the id of a user by their name or email """

def authenticate(id, hash):
  """ checks if the provided password hash is the correct hash for the user with given id """

def register(name, email, unsalted_hash):
  """ registers a user with given name and email; generates a salt and a salted hash for that user to save their password """
  id = secrets.randbits(64)
  final_hash = encrypt(unsalted_hash)



def encrypt(unsalted_hash, salt):
  """ salt and hash a received password hash """
  final_hash = hashlib.sha512()
  global_salt = get_global_salt()
  return final_hash.update(unsalted_hash+salt+global_salt).hexdigest()

def get_global_salt():
  """ standin """
  return '17de4'