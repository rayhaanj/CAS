from database import db_session
from models import User


def checkLogin(username, password):
	user = db_session.query(User).filter_by(User.email_address == username).first()
	if user is None:
		return False
	if user.password == password:
		return True
	return False


def attemptLogin(username, password, service, ip, client):
	if checkLogin(username, password):
		return True
	# Record login failure and fire notification

