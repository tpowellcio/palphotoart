from fabric.api import *


env.roledefs = {
    'app': [],
}


@roles('app')
def deploy():
    # Remove this line when you're happy that this Fabfile is correct
    raise RuntimeError("Please check the fabfile before using it")

    base_dir = '/usr/local/django/wtwebsite'
    virtualenv_dir = '/usr/local/django/virtualenvs/wtwebsite'
    python = virtualenv_dir + '/bin/python'
    pip = virtualenv_dir + '/bin/pip'

    user = 'wtwebsite'
    supervisor_task = 'wtwebsite'

    with cd(base_dir):
        with settings(sudo_user=user):
            sudo('git pull origin master')
            sudo(pip + ' install -r requirements/production.txt')
            sudo(python + ' wtwebsite/manage.py syncdb --settings=wtwebsite.settings.production --noinput')
            sudo(python + ' wtwebsite/manage.py migrate --settings=wtwebsite.settings.production --noinput')
            sudo(python + ' wtwebsite/manage.py collectstatic --settings=wtwebsite.settings.production --noinput')
            sudo(python + ' wtwebsite/manage.py compress --settings=wtwebsite.settings.production')
            sudo(python + ' wtwebsite/manage.py update_index --settings=wtwebsite.settings.production')

    sudo('supervisorctl restart ' + supervisor_task)
