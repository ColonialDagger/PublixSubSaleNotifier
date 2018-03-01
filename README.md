# PublixSubSaleNotifier
Notifies multiple users via SMS when Publix Chicken Tender subs are on sale.
Runs on Python 2.7.12

## Dependencies
### Required
* BeautifulSoup4
* time
* requests
* config
* sys
* Twilio
  - To install Twilio, use `pip install twilio` or, you can [download the source code (ZIP)](https://github.com/twilio/twilio-python/zipball/master "twilio-python).
  - Don't have pip installed? Try installing it, by running this from the command line:
```
$ curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
```

## Getting Started
1. Setup a Twilio account and phone number.
2. Configure the bot in the bot.py file.
3. Run the bot by running run.py with an active internet connection.
