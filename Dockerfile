FROM node:6.9.5-alpine
RUN npm install angular-cli -g && apk --update --no-cache add python3 && mkdir /srv/angular4django
ADD requirements.txt /srv/angular4django
RUN cd /srv/angular4django && pip install -r requirements.txt