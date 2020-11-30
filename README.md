# Running Coding Workshops with VS Code in the Browser

## Prerequisites
* Docker
* Python 3
* `pip install pyyaml`

## Usage
Create a Docker image for code-server. This repo has Dockerfiles for Java and JavaScript. Setup a workshop.config.json file with the appropriate values for your workshop. Run `python start-workshop.py` which will create the necessary number of Docker containers, create directories for each container, copy appropriate files for your workshop, and start the containers. 

## workshop.config.json
```json
{
    "image": "code-server",
    "repos": [
        "https://github.com/someid/somerepo.git"
    ],
    "student_count": 2,
    "setup_instructor": true,
    "pwd": "abc123"
}
```
**image** - Docker image containing code-server and any necessary build tools/language runtimes
**repos** - List of URLs to git repos containing student exercises
**student_count** - Number of containers to create.
**setup_instructor** - Create an instructor container with access to files in all student containers
**pwd** - Password to access VS code in browser using HTTP Basic Authentication.

## code-server-config.yaml
```yaml
bind-addr: 127.0.0.1:8080
auth: password
password: abc12345
cert: false
```
Values used by code-server. You probably won't need to change any of these. See [here](https://github.com/cdr/code-server/blob/v3.6.2/doc/FAQ.md#how-does-the-config-file-work) for more configuration options.


