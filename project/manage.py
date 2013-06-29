#!/usr/bin/env python
import os
import sys
import site

dir=os.path.dirname(__file__)
if dir:
    os.chdir(dir)
venv_dir='/srv/www/li259-36.members.linode.com/djblog/venv/pyvenv26/lib/python2.6/site-packages'
prev_sys_path=sys.path[:]
site.addsitedir(venv_dir)
sys.path[:0] = [sys.path.pop(pos) for pos, p in enumerate(sys.path) if p not in prev_sys_path]

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djsblog.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
