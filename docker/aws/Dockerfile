FROM codercom/code-server:3.9.0
  
USER root

RUN apt-get install -y curl \
  && curl -sL https://deb.nodesource.com/setup_16.x | bash - \
  && apt-get install -y nodejs

RUN npm install -g npm@7.16.0
RUN npm install -g aws-cdk
RUN apt-get install -y unzip

RUN curl -sL https://download.docker.com/linux/debian/dists/buster/pool/stable/amd64/docker-ce-cli_20.10.9~3-0~debian-buster_amd64.deb --output docker-ce-cli.deb && dpkg -i docker-ce-cli.deb
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install
RUN curl -sL https://github.com/aws/aws-sam-cli/releases/download/sam-cli-beta-cdk/aws-sam-cli-linux-x86_64.zip --output aws-sam-cli-linux-x86_64.zip && unzip aws-sam-cli-linux-x86_64.zip -d sam-installation && ./sam-installation/install

USER 1000

ENV SHELL=/bin/bash

RUN code-server --install-extension dbaeumer.vscode-eslint

