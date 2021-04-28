FROM codercom/code-server:3.9.0

USER root

RUN apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_15.x | bash - \
  && apt-get install -y nodejs 

RUN npm install

RUN apt-get install -y libgtk2.0-0 libgtk-3-0 libgbm-dev libnotify-dev libgconf-2-4 libnss3 libxss1 libasound2 libxtst6 xauth xvfb

USER 1000

RUN npx --yes cypress@7.2.0 install

ENV SHELL=/bin/bash

RUN code-server --install-extension dbaeumer.vscode-eslint


