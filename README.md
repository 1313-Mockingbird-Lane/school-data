# school-data

## Installing dependencies

As always its probably best to isolate the app within a virutalenv.
Install virutalenv if needed:

```
pip install virutalenv
```

Create a virutalenv, activate it, and install requirements.txt


```
virutalenv venv
source venv/bin/activate
pip install -r requirements.txt

```

Download the school data and convert to line seperated json
```
python get_school_data.py
```

View top of output file:

```
head -n5 schools.lsjson
```