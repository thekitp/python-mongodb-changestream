# python-mongodb-changestream

## install python3 pymongo module and dnspython
```
python3 -m pip install -r requirements.txt
```

## setup mondb endpoint and auth
```
source ./setup.sh
```

## Terminal #1 run watcher
```
python changestream_watch.py
```

## Terminal #2 run insert
```
python changestream_insert.py
```
