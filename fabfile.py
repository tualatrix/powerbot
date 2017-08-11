from fabric.api import *
from fabric.context_managers import shell_env

def build():
    local('docker build -t powerbot .')
