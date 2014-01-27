pywwo
=====

Python wrapper library for [World Weather Online API](http://www.worldweatheronline.com) using lxml.objectify

How to use
---------------
```python
from pywwo import *
setKey('<your_key>', 'free')
w=LocalWeather('london')
w.data.current_condition.temp_C
w=LocalWeather('sdfasdgasdga')
```
> Unable to find any matching weather location to the query submitted!

For more test cases, see test run inside the script
> python pywwo.py

see test result inside the script.

Feature
---------
1. lxml.objectifiy
2. error checking

See also
--------
1. [NodeJS client for WWO API](https://github.com/michaelben/nodejswwo)
2. [Javascript client for WWO API](https://github.com/michaelben/jswwo)
3. [Java client for WWO API](https://github.com/michaelben/JavaWWO)
4. [Android client for WWO API](https://github.com/michaelben/AndroidWWO)
5. [Python client for WWO API](https://github.com/michaelben/pywwo)
