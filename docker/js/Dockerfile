FROM codercom/code-server

USER root

RUN apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_15.x | bash - \
  && apt-get install -y nodejs 

RUN npm install

USER 1000

RUN code-server --install-extension dbaeumer.vscode-eslint


