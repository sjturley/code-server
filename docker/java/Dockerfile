FROM gradle:jre as gradle-base
FROM codercom/code-server:3.9.0

USER root

RUN apt-get update && apt-get -y install openjdk-11-jdk
COPY --from=gradle-base /opt/gradle /opt/gradle
ENV GRADLE_HOME=/opt/gradle
RUN ln -s "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle
    
RUN  printf "server \n{ \nlisten 5000; \nroot /home/coder/project; \nautoindex on; \n}" > /etc/nginx/sites-available/nginx-site
RUN ln -s /etc/nginx/sites-available/nginx-site /etc/nginx/sites-enabled/nginx-site
RUN service nginx restart
    
USER 1000

ENV SHELL=/bin/bash

RUN code-server --install-extension vscjava.vscode-java-pack
