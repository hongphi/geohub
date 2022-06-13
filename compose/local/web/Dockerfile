FROM node:16

WORKDIR /frontend

COPY ./frontend/package.json /frontend
COPY ./frontend/vite.config.ts /frontend

RUN npm install && npm cache clean --force

ENV PATH ./frontend/node_modules/.bin/:$PATH
