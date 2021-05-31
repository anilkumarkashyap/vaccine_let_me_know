# This code will be checking the for vaccine availbility on Cowin for adult under 45 years.

This script will check for vaccine availability and call to the famlity members on their phone numbers when available when there are more than 10 free slots availabile.

### How to use

#### Pre-requisites
* [python 3.x] must be installed on the system, you can downloads and install from https://www.python.org/downloads/
* Twilio account to provide calling number, you can create free account in a min at https://www.twilio.com/
* active internet connection on the system where it will be running.

#### Installation
* Open command prompt and install all required modules.
    ```sh
    pip install -r .\requirements.txt
    ```

* Add one row for each famly members at line 20. Name, Pincode and Contact number 
* Add Twilio information account_sid, auth_token and account_phone_number

##### Execution 

* Run the script.
    ```sh
    python vaccine_checker.py
    ```

##### Hope you like it.
