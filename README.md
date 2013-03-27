pywwo
=====

Python wrapper library for [World Weather Online API](http://www.worldweatheronline.com) using lxml.objectify

How to use
---------------
<<<<<<< HEAD
> >>> from pywwo import *
> >>> setKey('<your_key>', 'free')
> >>> w=LocalWeather('london')
> >>> w.data.current_condition.temp_C
> >>> w=LocalWeather('sdfasdgasdga')
Unable to find any matching weather location to the query submitted!

For more usage, see test run inside the script
> >>> python pywwo.py
=======
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
>>>>>>> 597144dcca77469f8f5f33a8a11f52f3f9c27ea0

see test result inside the script.

Feature
---------
1. lxml.objectifiy
2. error checking
