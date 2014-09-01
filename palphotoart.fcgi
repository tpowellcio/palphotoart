#!/home6/archerbu/miniconda/envs/ppa/bin/python
import sys, os
project_name = "wtwebsite"

# Add a custom Python path.
sys.path.insert(0, os.path.expanduser("~") + "/miniconda/envs/ppa")
sys.path.insert(13, os.path.expanduser("~") + "/www/palphotoartv2/" + project_name)

os.environ['DJANGO_SETTINGS_MODULE'] = project_name + '.settings'
from django.core.servers.fastcgi import runfastcgi
runfastcgi(method="threaded", daemonize="false")
