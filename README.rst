===========
mydashboard
===========

mydashboard is written as an example for adding a custom Angular 
dashboard to OpenStack Dashboard. 
Shoutout to Thai Tran's
https://github.com/tqtran7/mon-ext for how to package it. :)

How to use this
===============

1. Git clone this repo to your local machine
2. Run "python setup.py sdist" in mydashboard folder
3. Run "./tools/withvenv.sh pip install mydashboard/dist/..tar.gz" in horizon
4. Link or copy files to enabled folder at ``openstack-dashboard/local/enabled``
