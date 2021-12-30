# searchEngine

----
A search engine which is used for search in private networks.

## Technologies Used

- Python3
- Apache Nutch (For Crawler)
- Apache Solr (For Indexing)

## Installation

### for Debian based distros

Pre-requestie: python3

`
pip3 install urllib3 django bs4 requests subprocess
`

Clone this repo
`
git clone https://github.com/thewachdog/searchEngine.git
`

Navigate into the folder
`
cd searchEngine
`

Run main.sh
```./main.sh```

### Docker image

["Click here"](https://hub.docker.com/r/thewachdog/search-engine-final)

OR

Use this in Dockerfile (you must have installed openjdk)
example Dockefile

```bash
FROM openjdk:13
WORKDIR /home
COPY searchEngine/ /home
CMD ['./main.py']
```

build docker image

```bash
docker build -t imagename .
```
