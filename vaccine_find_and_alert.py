from datetime import datetime, timedelta
import time
import schedule
import requests
import re
from twilio.rest import Client

##========================== Configuration ===================================###

#************ twilio config ***********
# add your sid here
account_sid = ''
# add your token here
auth_token = ''
# add your twilio phone number
account_phone_number = ''
#************ twilio config ***********

# add your contact list here 
contact_list = [
                {'Name': 'Anil','Pincode' : '560066', 'contact_num':'+910000000000'}, 
                {'Name': 'Rajiv','Pincode' : '249403', 'contact_num':'+910000000000'}, 
                {'Name': 'Gaurav','Pincode' : '560065', 'contact_num':'+910000000000'}
               ]

##============================================================================###

phone_number_to_call = ''
contact_name_to_call = ''


def check_for_vaccine():
    try:
        for contact in contact_list:
            cowin_query(contact['Pincode'])
    except:
        print("Something went wrong. But I am still alive.")


def cowin_query(code):
    date_to_check = (datetime.today() + timedelta(days=1)).strftime('%d-%m-%Y')
    api_url = 'api/v2/appointment/sessions/public/calendarByPin?pincode'
    query_url = 'https://www.cowin.gov.in/{}={}&date={}'.format(api_url, code, date_to_check)
    print(query_url)
    response = requests.get(query_url)
    centers_list = response.json()
    check_availability(code, centers_list)


def check_availability(code, centers_list):
    for center in centers_list['centers']:
        if 'sessions' in center:
            for session in center['sessions']:
                if(session['available_capacity_dose1'] > 0 and session['min_age_limit'] < 45):
                    print('{} Hurreeeyyy vaccine available :) for {}. Search code: {}, {}, {}, {}, {}'.format(
                        datetime.now().strftime("%m/%d/%Y, %H:%M:%S"),
                        session['date'],
                        code,
                        session['available_capacity_dose1'],
                        session['vaccine'],
                        center['name'],
                        center['address']))
                    if(session['available_capacity'] > 10 and account_sid != '' and phone_number_to_call != '' and auth_token != '' and account_phone_number != ''):
                        callme(code,'found {} {} vaccine available at {}, {}'.format(
                            session['available_capacity'],
                            session['vaccine'],
                            center['name'],
                            center['address']))


def callme(code,message):
    if bool(re.match("^[A-Za-z0-9]*$", account_sid)) and \
            bool(re.match("^[A-Za-z0-9]*$", account_sid)):
        client = Client(account_sid, auth_token)
        for contact in contact_list:
            if (found_pin == contact['Pincode']):
                contact_name_to_call = contact['Name']
                phone_number_to_call = contact['contact_num']
        client.calls.create(
            twiml='''<Response><Say>Hi {} !! {}. </Say></Response>'''.format(contact_name_to_call, message),
            to=phone_number_to_call,
            from_=account_phone_number
        )
    else:
        print('Cannot call back. Incorrect Twilio configuration.')


#check_for_vaccine()
schedule.every(5).seconds.do(check_for_vaccine)
print('Vaccine monitoring started.')
while True:
    schedule.run_pending()
    time.sleep(1)
