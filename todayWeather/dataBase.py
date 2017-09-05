# import modules

import sqlite3

def add_to_database(temp_high, temp_low,description):
	# connection
	con = sqlite3.connect('weather.db')

	with con:
		# add a cursor
		c = con.cursor()

		c.execute("""
		INSERT INTO weatherData 
			(temp_high,temp_low,description) 
			values (?,?,?)
	
		""",(temp_high, temp_low, description))