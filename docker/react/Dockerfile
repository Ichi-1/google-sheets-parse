FROM node:18-alpine3.15

RUN mkdir /react_app

WORKDIR /react_app

COPY ./frontend /react_app

RUN npm i

CMD ["npm", "run", "start"]