image_name=$1
port=$2
project_volume=$3
config_volume=$4

docker run -it -d --rm -p 0.0.0.0:$port:8080 \
 -v "/var/run/docker.sock:/var/run/docker.sock" \
 -v "$config_volume:/home/coder/.config" \
 -v "$project_volume:/home/coder/project" \
 -u "$(id -u):$(id -g)" \
 -e "DOCKER_USER=$USER" \
 $image_name:latest
