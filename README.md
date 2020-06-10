# Acuvere
## Background
The COVID-19 pandemic has overwhelmed hospitals around the world, and the struggles healthcare workers are facing has drawn much attention. However, while many projects have been created to ease the stress on healthcare systems fighting COVID, many have overlooked the impact of the pandemic on patients whose appointments, procedures, and general health needs have been neglected. Furthermore, as the spread of the virus continues to slow, hundreds of thousands of patients around the world will be recovering from COVID and face their own unique challenges. Acuvere is meant to support everyday people with semi-urgent health conditions and COVID patients going through the rehabilitation process via an online platform centered around patient biometric data.

This health care app allows for patients to share personal biometrics from common health devices (such as Fitbit, Google Fit, etc.) with health care providers, who can then recommend exercises for the patient to follow to improve their health, based on their current health condition and goals. Patients and doctors can also view the patient’s change in biometrics over time through graphs created by the app. Patients have the ability to view upcoming appointments and contact their doctors directly within the app as well.

## To use the app
### Method 1

http://acuvere.herokuapp.com  

Username: testuser  

Password: healthisgr8  

### Method 2

`$ source ll_env/bin/activate`  

`(ll_env)$ pip install -r requirements.txt`  

`python manage.py migrate`  

`python manage.py createsuperuser`  

`python manage.py runserver`

The superuser can be used to create appointments and tasks for patients created via the user interface. If there are any errors with these instructions or issues using the app, please let us know.

## For contributors
If you would like to contribute to Acuvere, please get in touch. Below, we have outlined our next steps for the platform for you to draw ideas for pull requests from.

A major next step would be to implement a separate half of the app for healthcare providers. Currently, appointments and tasks must be manually inputted from the default Django administrator page. Implementing another type of user account for healthcare providers and creating a separate user interface would make using the app more convenient for doctors and resolve possible privacy issues. To improve the scalability of the app, we would also like to explore integrating the platform with popular electronic medical record systems. After the website is fully developed and successfully deployed, our goal is to become verified from Google to access patients biometrics from the Google Fit API. Afterwards, we plan on publicizing the website such that both patients and doctors can use our platform as a method of communication and biometric monitoring.
