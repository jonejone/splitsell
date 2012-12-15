from fabric.api import *

env.hosts = ['www.splitsell.com',]

def deploy():
    with cd('/home/jone/splitsell/project'):
        run('git pull')
        run('workon splitsell')
        run('python manage.py collectstatit --noinput')
        run('sudo /etc/init.d/apache2 restart')
