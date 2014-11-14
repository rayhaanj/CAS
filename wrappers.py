from functools import wraps
from flask import session, Response

def logged_in(f):
	@wraps(f)
	def decorated_function(*args, **kwargs):
		if session.get('logged_in') is not None:
			return f(*args, **kwargs)
		else:
			return Response("Access denied", 403)
	return decorated_function

def has_permission(permission):
	def decorator(func):
		def wrapper(*args, **kwargs):
			func(args, kwargs)
		return wrapper
	return decorator
