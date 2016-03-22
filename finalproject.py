

contact = {
	"First": "Lydia", 
	"Last": "Huang", 
	"Tel": "619-203-0186", 
	"Address": "542 Mason", 
	"Email": "lyd.huang@gmal.com"
}

def create_contact(First,Last,Tel,Address,Email):
	new_contact = {
		"First": First,
		"Last": Last,
		"Tel": Tel,
		"Address": Address,
		"Email": Email,
	}
	return new_contact

contact_list = [create_contact("Aaron", "Elligsen", "541-556-8263", "368 Citrus Ave", "aaron@hackbrightacademy.com")]




def delete_contact():
	for index, person in enumerate(contact_list):
		print " %i, %s, %s" %(index, person["First"], person["Last"])
	user_index = raw_input("What would you like to delete?")
	contact_list.pop(int(user_index))



#delete_contact()

def edit_contact():
	for index, person in enumerate(contact_list):
		print " %i, %s, %s" %(index, person["First"], person["Last"])
	index = raw_input("Who would you like to edit?")

	print contact_list[index]
	changing_name = raw_input("Would you like to change first name?")
	if  changing_name == "yes":
		new_name = raw_input("new_name")
		contact_list[index]["First"]=new_name

	if raw_input("Would you like to change last name?") == "yes":
		new_lastname = raw_input("new_lastname")
		contact_list[index]["Last"] = new_lastname

	if raw_input("Would you like to change telephone?") == "yes":
		new_tel = raw_input("new_tel")
		contact_list[index]["tel"] = new_tel

	if raw_input("Would you like to change address?") == "yes":
		new_address = raw_input("new_address")
		contact_list[index]["new_address"] = new_address

	if raw_input("Would you like to change email?") == "yes":
		new_email = raw_input ("new_address")
		contact_list[index]["new_email"] = new_email

# edit_contact(0)
# print contact_list[0]

def search_contact(first_name, last_name):
	for person in contact_list:
		if person["First"]==first_name and person["Last"] ==last_name:
			return person

# print search_contact("Aaron", "Elligsen")

user_action = None

while user_action != "5":
	print "(1) Create a contact"
	print "(2) Delete a contact"
	print "(3) Edit a contact"
	print "(4) Search a contact"
	print "(5) Exit the program"
	user_action= raw_input("What would you like to do?")
	if user_action == "1":
		first_name = raw_input("What is the first name?")
		last_name  = raw_input("What is the last name?")
		tel = raw_input ("What is the tel?")
		address = raw_input ("What is the address?")
		email = raw_input ("What is the email?")
		new_contact = create_contact(first_name,last_name,tel,address,email)
		contact_list.append(new_contact)
		print "--------------------------"
		print "Contact Added Woohoo! :-D "
		print "--------------------------"


	elif user_action =="2":
		delete_contact()
		print "--------------------------"
		print "Contact Deleted Boohoo! :-( "
		print "--------------------------"
		
	elif user_action =="3":
		edit_contact()

	elif user_action =="4":
		first_name = raw_input("What is the first name?")
		last_name  = raw_input("What is the last name?")
		person = search_contact(first_name,last_name)
		print person["First"], person["Last"], person["Tel"], person["Address"], person["Email"]

	elif user_action =="5": 
		print "Good Bye"
		# add contact 







	#while the user wants to keep using the program
	#the user will want to use the following 4 functions
	#enter, delete, edit, and search
	#optional: categorize, alternative alias, titles
	#if user picks enter then we will create 5 raw_inputs for variables
	#we will use the 5 variables to pass into create_contact
	#we will save that into new variable called new_contact
	#we will append that contact to the contacts_list up on top
	#that will be adding a contact
	#go over list chapter to append

	#define edit: start off by printing the index in the contact_list array and their name
	#write a couple of if statements to ask if user would like to change one of the 5 properties
	#write while loop after defining all 5 functions
