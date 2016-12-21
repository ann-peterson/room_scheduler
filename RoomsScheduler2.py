import requests
import json



room_db = {"rm-a" : {"room_id" : "rm-a", "room_name" : "Room A", "time_available" : "Mondays-Sundays", "location" : "First Floor", "description" : "Accomodates 25 people."},
		"rm-b" : {"room_id" : "rm-b", "room_name" : "Room B", "time_available" : "Mondays-Sundays", "location" : "First Floor", "description" : "Accomodates 45 people."},
		"rm-c" : {"room_id" : "rm-c", "room_name" : "Room C", "time_available" : "Mondays-Sundays", "location" : "Second Floor", "description" : "Accomodates 100 people."}}

#booking_db = {"12/12/16" + "," + "1000" + "," + "rm-a" : {"date" : "12/12/16", "time" : "1000", "room" : "rm-a", "reserved_by" : "Ann"}}
		



def save_data(booking_db):
	with open('room_schedule_data2.json', 'w') as outfile:
		json.dump(booking_db, outfile)
		return
	



def open_data():
  	with open('room_schedule_data2.json', 'r') as f:
  		booking_db = json.load(f)
  	return booking_db


booking_db = open_data()
# save_data(booking_db)
	

def display_menu():
	print ''' 
	1 - View room information
	2 - Make a reservation
	3 - Show bookings
	4 - Exit menu
	'''

def show_rooms():
	print '''
	1 - Room A
	2 - Room B
	3 - Room C
	'''	
	

def view_room_info_by_room(room_db, room_num):
	print "Room Name: " + room_db[room_num]["room_name"]
	print "Times Available: " + room_db[room_num]["time_available"]
	print "Location: " + room_db[room_num]["location"]
	print "Room Description: " + room_db[room_num]["description"]



def view_all_rooms_info():
	print
	print "Take a look at our rooms."
	print
	view_room_info_by_room(room_db, room_num = "rm-a") 
	print
	view_room_info_by_room(room_db, room_num = "rm-b")
	print
	view_room_info_by_room(room_db, room_num = "rm-c")	



def book_a_room(booking_db, date, time, reservation_name, room_num):
	# my_key = (date, time, room_num)
	my_key = date + "," + time + "," + room_num
	if my_key in booking_db:
		print "I'm sorry, the room is unavailable at that time.  Please make another selection."
	else:
		print my_key	
		booking_db[my_key] = {"date" : date, "time" : time, "room" : room_num, "reserved_by" : reservation_name}
		print "Great it's booked, you're all set!  Here are your reservation details."
		print "Date: " + booking_db[my_key]["date"]
		print "Time: " + booking_db[my_key]["time"]
		print "Room: " + booking_db[my_key]["room"]
		print "Reserved by: " + booking_db[my_key]["reserved_by"]
		save_data(booking_db)
	

def show_bookings_menu():
	print '''
	1 - Show all bookings
	2 - Show bookings by room
	'''
	#3 - Show bookings by year
	

def show_all_bookings():
	print "All Reservations: "
	#global booking_db
	for key in booking_db:
		print "Date: " + booking_db[key]["date"]
		print "Time: " + booking_db[key]["time"]
		print "Room: " + booking_db[key]["room"]
		print 

def show_all_bookings_by_room(booking_room_choice):
	print "All Reservations in " + booking_room_choice
	for key in booking_db:
		if booking_db[key]["room"] == booking_room_choice:
			print "Date: " + booking_db[key]["date"]
			print "Time: " + booking_db[key]["time"]
			print "Room: " + booking_db[key]["room"]
			print

# def show_all_bookings_by_year():
# 	for key in booking_db:
# 		if booking_db[key]["date"][7] == "6":
# 			print "Date: " + booking_db[key]["date"]
# 			print "Time: " + booking_db[key]["time"]
# 			print "Room: " + booking_db[key]["room"]
# 			print 					 	

#def want_an_email():
	# email_preference = raw_input("Would you like an email confirming the details? Yes or no.").lower()
	# if email_preference == "yes":
	# 	reservation_email = raw_input("Please enter your email.").lower()
	# 	#send_email_confirmation(reservation_email, reservation_name, room_choice, day_choice, time_choice)
	# else:
	# 	pass
# def want_an_email(reservation_email, reservation_name, room_choice, day_choice, time_choice):
# 	email_preference = raw_input("Would you like an email confirming the details? Yes or no.").lower()
# 	if email_preference == "yes":
# 		reservation_email = raw_input("Please enter your email.")
# 		send_email_confirmation(reservation_email, reservation_name, room_choice, day_choice, time_choice)
# 	elif email_preference == "no":
# 		print "Ok, thanks for stopping by!"			
	

def send_email_confirmation(reservation_email, reservation_name, room_choice, day_choice, time_choice):
	key = 'key-f56400bb14c50034a1314e4787bc3975'
	sandbox = 'sandbox7b7ddee699f14d9fb8972aee21678217.mailgun.org'
	#recipient = reservation_email

	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
	request = requests.post(request_url, auth=('api', key), data={
    	'from': 'roomscheduler@example.com',
    	'to': reservation_email,
    	'subject': 'Room Confirmation',
    	'text': "Hello " + reservation_name + ", " + "looks like you're all set.  We've got you booked in " + room_choice + " on " + day_choice + " at " + time_choice + " hours.  Thanks for using the room scheduler!"
	})
	print
	print "Great, an email has been sent to that address.  Thanks for using the room scheduler!"
	#print 'Status: {0}'.format(request.status_code)
	#print 'Body:   {0}'.format(request.text)



def main():
	print "Hello, welcome to the room scheduler."
	while True:
		display_menu()
		menu_selection = raw_input("Please select one of the above:")
		
		#view room information
		if menu_selection == "1":
			view_all_rooms_info()
		
		#book a room
		elif menu_selection == "2":
			print "Here are the available rooms:  Room A, Room B, Room C."
			room_preference = raw_input("Do you already know which room you'd like to book?  Yes or no.").lower()
			# here are our rooms and their descriptions
			if room_preference == "yes":
				print
				show_rooms()
				# This allows the user to input a number corresponding to the room they want
				room_choice = raw_input("Please enter one of the above:")
				if room_choice == "1":
					room_choice = "rm-a"
				elif room_choice == "2":
					room_choice = "rm-b"
				elif room_choice == "3":
					room_choice = "rm-c"
				else:
					print "That doesn't exist.  Please make another choice."
				day_choice = raw_input("What date would you like to book?  Please enter in month/day/year format.")
				time_choice = raw_input("Great, what time would you like to book?  Please enter in military time - ex. 2100")
				reservation_name = raw_input("What name should I make the reservation under?")
				print
				print "Let me check to see if that's available for you."
				book_a_room(booking_db, day_choice, time_choice, reservation_name, room_choice)
				#want_an_email(reservation_email, reservation_name, room_choice, day_choice, time_choice)
				#want_an_email()
				email_preference = raw_input("Would you like an email confirming the details? Yes or no.").lower()
				if email_preference == "yes":
					reservation_email = raw_input("Please enter your email.")
					send_email_confirmation(reservation_email, reservation_name, room_choice, day_choice, time_choice)
				elif email_preference == "no":
					print
					print "Ok, thanks for stopping by!"	
				else:
				 	pass	

			elif room_preference == "no":
				view_all_rooms_info() #show room descriptions	
				show_rooms()
				# This allows the user to input a number corresponding to the room they want
				room_choice = raw_input("Please enter one of the above:")
				if room_choice == "1":
					room_choice = "rm-a"
				elif room_choice == "2":
					room_choice = "rm-b"
				elif room_choice == "3":
					room_choice = "rm-c"
				else:
					print "That doesn't exist.  Please make another choice."
				day_choice = raw_input("What date would you like to book?  Please enter in month/day/year format.")
				time_choice = raw_input("Great, what time would you like to book?  Please enter in military time - ex. 2100")
				reservation_name = raw_input("What name should I make the reservation under?")
				print "Let me check to see if that's available for you."
				book_a_room(booking_db, day_choice, time_choice, reservation_name, room_choice)
				email_preference = raw_input("Would you like an email confirming the details? Yes or no.").lower()
				if email_preference == "yes":
					reservation_email = raw_input("Please enter your email.")
					send_email_confirmation(reservation_email, reservation_name, room_choice, day_choice, time_choice)
				elif email_preference == "no":
					print "Ok, thanks for stopping by!"	

		#show bookings
		elif menu_selection == "3":
			show_bookings_menu()
			booking_menu_choice = raw_input("Please select one of the above.")
			if booking_menu_choice == "1":
				show_all_bookings()
			elif booking_menu_choice == "2":
				show_rooms()
				booking_room_choice = raw_input("Please enter one of the above:")
				if booking_room_choice == "1":
					booking_room_choice = "rm-a"
				elif booking_room_choice == "2":
					booking_room_choice = "rm-b"
				elif booking_room_choice == "3":
					booking_room_choice = "rm-c"
				show_all_bookings_by_room(booking_room_choice)
			# elif booking_menu_choice == "3":
			# 	show_all_bookings_by_year()		

	
		#exit menu
		elif menu_selection == "4":
			break	



	

if __name__ == '__main__':
		main()	

