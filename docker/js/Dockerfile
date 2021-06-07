FROM codercom/code-server:3.9.0

USER root

RUN apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
  && apt-get install -y nodejs 

RUN npm install -g npm@7.16.0

USER 1000

ENV SHELL=/bin/bash

RUN code-server --install-extension dbaeumer.vscode-eslint


