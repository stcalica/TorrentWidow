FROM  

RUN apt-get install -y deluge 

RUN mkdir -p /usr/app/src
WORKDIR /usr/app/src 

COPY ./blackwidow/torrents.json /usr/app/src/data
COPY ./log /usr/app/src/data 


CMD ['torrent-download.sh']
