FROM gradle:jre as gradle-base
FROM codercom/code-server:3.9.0

USER root

RUN apt-get update && apt-get -y install openjdk-11-jdk
COPY --from=gradle-base /opt/gradle /opt/gradle
ENV GRADLE_HOME=/opt/gradle
RUN ln -s "${GRADLE_HOME}/bin/gradle" /usr/bin/gradle
    
USER 1000

ENV SHELL=/bin/bash

RUN code-server --install-extension vscjava.vscode-java-pack
