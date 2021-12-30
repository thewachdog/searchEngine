#!/bin/bash

export JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:bin/java::")

# ../solr/bin/solr stop -all && \
# ../solr/bin/solr start
# ../solr/bin/solr create -c nutch -d solr/server/solr/configsets/nutch/conf


bin/nutch inject crawl/crawldb urls && \
bin/nutch generate crawl/crawldb crawl/segments

export s1=`ls -d crawl/segments/2* | tail -1` && \
bin/nutch fetch $s1 && \
bin/nutch parse $s1 && \
bin/nutch updatedb crawl/crawldb $s1

bin/nutch generate crawl/crawldb crawl/segments -topN 1000 && \
export s2=`ls -d crawl/segments/2* | tail -1` && \
bin/nutch fetch $s2 && \
bin/nutch parse $s2 && \
bin/nutch updatedb crawl/crawldb $s2

bin/nutch generate crawl/crawldb crawl/segments -topN 1000 && \
export s3=`ls -d crawl/segments/2* | tail -1` && \
bin/nutch fetch $s3 && \
bin/nutch parse $s3 && \
bin/nutch updatedb crawl/crawldb $s3

bin/nutch invertlinks crawl/linkdb -dir crawl/segments && \
bin/nutch index crawl/crawldb/ -linkdb crawl/linkdb/ $s3 -filter -normalize
