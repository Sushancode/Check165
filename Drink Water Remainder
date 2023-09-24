# Problem statement
# Exercise 11 - Drink Water Reminder
# Write a python program which reminds you of drinking water every hour or two. Your program can either beep
# or send desktop notifications for a specific operating system


# Documentations
# classplyer.facades.Notification
# Notification facade.
#
# notify(title='', message='', app_name='', app_icon='', timeout=10, ticker='', toast=False, hints={})
# Send a notification.
#
# Parameters:
# title (str) – Title of the notification
# message (str) – Message of the notification
# app_name (str) – Name of the app launching this notification
# app_icon (str) – Icon to be displayed along with the message
# timeout (int) – time to display the message for, defaults to 10
# ticker (str) – text to display on status bar as the notification arrives
# toast (bool) – simple Android message instead of full notification
# hints (dict) – Optional hints that can be used to pass along extra instructions on Linux. (See https://specifications.freedesktop.org/notification-spec/latest/ar01s08.html) # noqa: E501
# Note
#
# When called on Windows, app_icon has to be a path to a file in .ICO format.
#
# New in version 1.0.0.
#
# Changed in version 1.4.0: Add ‘toast’ keyword argument

#code
from plyer import notification
import time

name = input('Enter your name: ')

while True:
    notification.notify(title = 'Drink Water remainder:',
                        message = f'Hey, {name}, it is time to drink water!',
                        app_name = 'Reamainder',
                        toast = True,
                        timeout = 5
                        )
    time.sleep(2 * 3600)
