# BILLY APP

![image](https://user-images.githubusercontent.com/24440993/107157078-c5363700-698a-11eb-812b-06a67eef98c6.png)

## Description
This application was developed in order to apply Python knowledge, GIT workflows, data visualization and learn more at the same time. The application is under the shell of a learning project.
The main purpose was to create applicability - that being a desktop app for tracking consumer bills for selected Romanian electricity, natural gas, internet & TV providers/suppliers and subscriptions. The app functionalities served the purpose of learning more of Python and the creation of UI using Python, data visualization plus the managing of a GIT repository.

The learning project path included working with Python as the main programming language, GIT for project versioning, PySide2 for the UI (layout, animations, widgets, charts, forms and so on), creating a basic, not-so-secure auth service (that includes user creation and authentication), playing around with a simple sqlite db for storing data, reading and extracting data from pdf files with regex, generating charts for data visualization and creating some graphic resources.

### Billy logo can be found here: [https://dribbble.com/shots/5832071-B-Paper-Sheet]

### Other graphic resources can be found here: [https://www.freepik.com/]

## Installation

Prerequisites: pip, venv
Project font: SF UI Display Font Family (can be found online)

1. After cloning the project, select the project directory and create a venv (make sure you have installed venv prior to this):
```
python -m venv venvBillyApp
```
2. After the venv is created, access the venv and activate it:
```
cd \venvBillyApp\Scripts
activate
```
3. After the venv is active, return to the root of the cloned project
```
cd ..\..
```
And install the project requirements:
```
pip install -r requirements.txt
```

The list of needed libraries:
```
cffi==1.14.4
chardet==4.0.0
cryptography==3.3.1
CurrencyConverter==0.14.4
cycler==0.10.0
kiwisolver==1.3.1
pdfminer3==2018.12.3.0
Pillow==8.1.0
pycparser==2.20
pycryptodome==3.9.9
pyparsing==2.4.7
PyQt5==5.15.1
PyQt5-sip==12.8.1
PySide2==5.15.1
python-dateutil==2.8.1
shiboken2==5.15.1
six==1.15.0
sortedcontainers==2.3.0
speedtest-cli==2.1.2
urllib3==1.26.2
```
4. Wait for the libraries to install and make sure the font is installed on your machine (SF UI Display Font Family)

5. Run the Billy App by using:
```
python main.py
```
NOTE: Check that the screen scaling is set to 100% for the correct display of the application.

## Usage

1. First step in testing the app is the user creation from the SIGN UP tab. After the user is successfully created, the user can login from the SIGN IN tab, as seen below:
![image](https://user-images.githubusercontent.com/24440993/107157681-1693f580-698e-11eb-9259-6dd2dbe2386f.png)

2. After the user is logged in, the main page that is displayed is the Dashboard page. The user will be requested to access the Account preferences in order to setup up the data.
From the account preferences, the user can add the monthly earnings in order to visualize data, select from the available electricity, natural gas, internet & TV suppliers/providers and subscriptions.
![image](https://user-images.githubusercontent.com/24440993/107157781-b6518380-698e-11eb-91ac-fdb65a271d22.png)

3. After the account preferences fields/selections are filled/made, the user can proceed adding the bill for the selected provider/supplier and track the price, issue date, due date, price evolution and price impact on monthly earnings.



### Here are some screenshots of the app pages:
![image](https://user-images.githubusercontent.com/24440993/107280996-c25a4580-6a61-11eb-97de-d409ba167b96.png)
![image](https://user-images.githubusercontent.com/24440993/107280867-9048e380-6a61-11eb-8f6e-904566821904.png)
![image](https://user-images.githubusercontent.com/24440993/107280968-b8384700-6a61-11eb-8b54-23514f0ed958.png)

