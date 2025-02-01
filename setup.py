from setuptools import setup

setup(
	name='midnight_snack_game',
	version='0.2',
	description='Game for telegram',
	author='Vladimir Nenakhov',
	author_email='nenahov@gmail.com',
	packages=['domain'],
	install_requires=[
		'aiogram', 'colorama'
	],
)
