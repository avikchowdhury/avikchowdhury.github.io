import requests

def user_menu():

    user_input=input("""Hi!What would you like to do
    1. PNR Status
    2. Train running status
    3. Train route
    4. Trains between stations
    5. Seat Availability""")


    if user_input=='1':
        #check PNR
        check_pnr()
    elif user_input=='2':
        #running status
        check_running_status()
    elif user_input=='3':
        #train route
        show_train_route()
    elif user_input=='4':
        #between station
        show_train_between_stations()
    elif user_input=='5':
        #seat avail
        check_seat_availability()
    else:
        print('Bye')
    check_pnr()

def check_pnr():

    pnr=input('Enter pnr')
    response=requests.get('https://api.railwayapi.com/v2/pnr-status/pnr/'+ pnr+ '/apikey/db69wc7lcb')
    json_text=response.json()
    print(json_text['passengers'])
def check_running_status():
    train_no=input("Enter the train number")
    doj=input('Enter the date')
def show_train_route():
    pass

def show_train_between_stations():
    pass

def check_seat_availability():
    pass
