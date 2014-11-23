Description
--
A Python interface for the [Dicks API](http://dicks-api.herokuapp.com)

Installation
--
```bash
pip install python-dicks
```

Requires
--
- requests
- simplejson

Example
--
```python
import dicks

api = dicks.Client()

dicks = api.get_dicks()
print(dicks)

served = api.get_dicks_served()
print(served)
```

This example can also be found in the example.py file.

License
--
python-dicks is available under the MIT license.


