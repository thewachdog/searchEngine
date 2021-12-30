#/bin/bash

rm solr/server/solr/configsets/nutch/conf/managed-schema
rm search/nutch/urls/seed.txt
touch ip.txt

hostname -I > ip.txt && \
python3 crawler2.py && \

rm ip.txt && \
cd search && \

mkdir -p solr/server/solr/configsets/nutch/ && \
cp -r solr/server/solr/configsets/_default/* solr/server/solr/configsets/nutch/ && \
solr/bin/solr stop && \
solr/bin/solr start && \
solr/bin/solr create -c nutch -d solr/server/solr/configsets/nutch/conf && \

cd nutch && \

./crawlScript.sh

cd ../../
pwd
python3 mysite/manage.py runserver
rm ip.txt
