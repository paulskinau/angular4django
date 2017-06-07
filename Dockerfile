FROM node:6.10-alpine
RUN apk --update --no-cache add python3 && ln -s /usr/bin/python3 /usr/bin/python && npm install angular-cli -g && mkdir /srv/angular4django
ADD requirements.txt /srv/angular4django
RUN cd /srv/angular4django && pip3 install -r requirements.txt