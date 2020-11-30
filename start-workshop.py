import json
import os
import shutil
import yaml

ROOT = os.getcwd()
PROJECT_ROOT = ROOT + '/workspace'
CONFIG_ROOT = ROOT + '/config'
BASE_PORT = 8080

def get_code_server_config():
  with open('code-server-config.yaml', 'r') as file:
    return yaml.load(file, Loader=yaml.SafeLoader)


def start_code_server(image, port, project_directory, pwd):
  os.chdir(ROOT)
  config_directory = "%s/%d/" % (CONFIG_ROOT, port)
  os.mkdir(config_directory)
  os.mkdir(config_directory + "/code-server")
  code_server_yaml = get_code_server_config()
  code_server_yaml['password'] = pwd
  with open(config_directory + "/code-server/config.yaml", 'w') as file:
    yaml.dump(code_server_yaml, file)
  os.system("sh start-code-server.sh %s %d %s %s" % (image, port, project_directory, config_directory))


def clean_volumes():
  shutil.rmtree(PROJECT_ROOT, True)
  shutil.rmtree(CONFIG_ROOT, True)
  os.mkdir(PROJECT_ROOT)  
  os.mkdir(CONFIG_ROOT)


def setup_repos(directory, repos):
  os.chdir(ROOT)
  os.mkdir(directory)
  os.chdir(directory)
  for repo in repos:
    os.system("git clone %s" % repo)


def setup_instructor(data):
  if data['setup_instructor']:
    start_code_server(data['image'], BASE_PORT, PROJECT_ROOT, data['pwd'])


def setup_students(data):
  student_count = int(data['student_count'])
  for i in range(1, student_count + 1):
    port = BASE_PORT + i
    project_directory = "%s/%d" % (PROJECT_ROOT, port) 
    setup_repos(project_directory, data['repos'])
    start_code_server(data['image'], port, project_directory, data['pwd'])


with open('workshop.config.json') as f:
  data = json.load(f)
  clean_volumes()
  setup_instructor(data)
  setup_students(data)


