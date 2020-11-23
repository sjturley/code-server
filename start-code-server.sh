port=8080

image_name=code-server-java

if [ $1 ]; then
  port=$1
fi

mkdir -p ~/.config/$port
mkdir -p workspace/$port
docker run -it -d --rm -p 0.0.0.0:$port:8080 \
 -v "$HOME/.config/$port:/home/coder/.config" \
 -v "$PWD/workspace/$port:/home/coder/project" \
 -u "$(id -u):$(id -g)" \
 -e "DOCKER_USER=$USER" \
 $image_name:latest

