#/bin/bash

rm search/nutch/urls/seed.txt
python3 crawler2.py
cd search/nutch
./crawlScript.sh
cd ../../
python3 mysite/manage.py runserver
