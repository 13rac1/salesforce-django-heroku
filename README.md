#Salesforce Django Heroku Quickstarter
by Brad Erickson (eosrei) 10-12-2014

This is a quickstart for using the Salesforce Username/Password Web OAuth2.0
workflow in Django 1.7 on Heroku (or BYOWH w/HTTPS.) It connects to Salesforce
and loads a list of your Contacts. The resulting project runs on both your local
`manage.py runserver` and Heroku.

##Instructions

This assumes you've run a Django Project locally and used Heroku before. If not
then get going:

 * https://docs.djangoproject.com/en/1.7/intro/tutorial01/
 * https://devcenter.heroku.com/articles/getting-started-with-django

1. Clone this repo:
```
$ git clone https://github.com/eosrei/salesforce-django-heroku.git
$ cd salesforce-django-heroku
```

2. Create a new Heroku dyno (which adds the remote) and write down the URL:
```
$ heroku apps:create
Creating verb-noun-1234... done, stack is cedar
http://verb-noun-1234.herokuapp.com/ | git@heroku.com:verb-noun-1234.git
Git remote heroku added
```

3. Sign up for a Salesforce Developer Account (if you don't have one) at: https://developer.salesforce.com/
4. Get your security token. Login and click the 'Your Name' dropdown and select `Setup`.
5. On the right sidebar under `Personal Setup` select: *Personal Information->Reset My Security Token*.
6. Click the `Reset Security Token` button and your Token will be emailed to you.
7. Setup the Connected App. Click the 'Your Name' dropdown in the upper right to select `Setup`.
8. On the right sidebar under the `App Setup` heading, click: *Create->Apps*.
9. There are three headings in the main content area. The last is `Connected Apps`. Click the `New` button.
10. Fill out the form:
    * Connected App Name: *salesforce-django-heroku*
    * API Name: *salesforce-django-heroku*
    * Contact Email: *Your Email*
    * Check the `Enable OAuth Settings` checkbox
    * Callback URL (Your new Heroku dyno URL with HTTPS, not really needed for our auth workflow): https://verb-noun-1234.herokuapp.com/
    * Select the `Full access (full)` scope and click `Add`
    * Click the `Save` button.

11. You'll be directed to the Salesforce Connected App page. Click `Click to reveal` the `Consumer Secret`.
12. Make note of both the `Consumer Key` and `Consumer Secret`.
13. Copy the `sdh/local_settings.py.example` file to `sdh/local_settings.py`.
14. Edit the new `sdh/local_settings.py` file and fill in all the fields. Note: The
    PASSWORD field is made up from your User Account Password + User Account Token. 
    
```
DATABASES['salesforce'] = {
    'ENGINE': 'salesforce.backend',
    'CONSUMER_KEY' : None,
    'CONSUMER_SECRET' : None,
    'USER': None,
    'PASSWORD': None,
    'HOST': 'https://login.salesforce.com',
}
```
14. Now

##Actually using your own Salesforce SObjects
Export the Salesforce table models you need:

    ./manage.py inspectdb --database="salesforce" --table-filter="Lead$|Contact$" > sdh\models.py

Then comment/remove model field the foreign keys to unused SObjects.
