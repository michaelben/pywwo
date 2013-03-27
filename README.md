pywwo
=====

Python wrapper library for [World Weather Online API](http://www.worldweatheronline.com)

How to use
---------------
>>> from pywwo import *
>>> setKey('<your_key>', 'free')
>>> w=LocalWeather('london')
>>> w.data.current_condition.temp_C
>>> w=LocalWeather('sdfasdgasdga')
Unable to find any matching weather location to the query submitted!

For more usage, see test run inside the script
>>> python pywwo.py

see test result inside the script.
