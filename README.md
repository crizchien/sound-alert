This is README.md.

# Trigger a sound alert by webhook
## Install python modules
```
pip3 install -r pip-requirements.txt
```
## How to use
```
python3 main.py
```
## How to trigger
```
curl -X PUT -H "Content-Type: application/json" -d '{"sound_key": "hey-michael"}' http://localhost:50000/hey-michael
```
