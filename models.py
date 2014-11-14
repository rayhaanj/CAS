from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Text, Enum
from database import Base

class User(Base):
	"""Represents a person's account on the compsoc authentication system."""
	__tablename__= 'user'

	id = Column(Integer, primary_key = True)

	full_name = Column(String(256))
	preferred_name = Column(String(128))
	nickname = Column(String(128))

	password = Column(String(256))
	salt = Column(String(256))

	email_address = Column(String(128))
	website = Column(String(128))

	date_joined = Column(DateTime)
	last_login = Column(DateTime)

	active = Column(Boolean)
	staff = Column(Boolean)
	superuser = Column(Boolean)  # Grant all priviliges and never delete.


class Group(Base):
	"""A grouping of users."""
	__tablename__ = 'group'

	id = Column(Integer, primary_key = True)

	name = Column(String(128))
	description = Column(Text)



class GroupMembershipRequest(Base):
	"""A proposal to add a user to a given group.
		Only group admin or superusers can approve.
	"""
	
	class TYPE:
		ADD = 1
		REMOVE = 2
		MAKE_ADMIN = 3
		REMOVE_ADMIN = 4

	__tablename__ = 'group_proposal'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('user.id'))
	group_id = Column(Integer, ForeignKey('group.id'))
	proposer_id = Column(Integer, ForeignKey('user.id'))
	type = Column(Integer)


class ShellAccount(Base):
	"""A shell account."""
	__tablename__ = 'shell_accounts'

	id = Column(Integer, primary_key = True)
	username = Column(String(128))
	password = Column(String(256))
	salt = Column(String(256))


class AuthenticationLog(Base):
	"""Represents an authentication attempt."""
	__tablename__ = 'authentication_log'

	id = Column(Integer, primary_key = True)
	compsoc_user_id = Column(Integer, ForeignKey('user.id'))
	success = Column(Boolean)
	login_ip = Column(String(16))
	service_name = Column(String(128))


class YubiKey(Base):
	"""Yubikey inventory"""
	__tablename__ = 'yubikey'

	id = Column(Integer, primary_key = True)
	aeskey = Column(String(128))

