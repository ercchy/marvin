# Badges

A bunch of scripts to manage ***Badges*** on an Ubuntu Server 12.04 x86 using [ansible](http://ansible.cc).

Our enviroments are modelled after our development workflow as following:

***LOCAL***
* developer's preferred Django development setup (mine is Ubuntu and PyCharm, your's may vary :-)

***DEV***
* environment used for testing new features by developers themselves and for integration testing with external services
* same installation setup as live production servers
* usually run locally on developer's machine using [Vagrant](http://www.vagrantup.com/)

***INT***
* staging and pre-production server
* same installation setup as live production servers
* should be run on separate machine

***PRD***
* live production servers

# Setup

For preparing your LOCAL development environment, please consult our ***Badges*** source code repository at https://github.com/p2pu/badges

For DEV, INT and PRD environments:

1. Install Vagrant

Usage:
* before you run this playbook, you need to setup credentials in var/credentials.yml, copy credentials.yml and rename it to credentials_(your_host).yml

The playbook sets up Badges in a virtual enviroment, configures hosting using apache and mod wsgi, 

##### TODO:
* setup DB
* setup celery

The best place to see all the moving parts is by looking in the playbook itself: install.yml.

 
