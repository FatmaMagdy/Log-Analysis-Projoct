# Log Analysis Projoct

An internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.

# Getting Started

These instructions will get you a copy of the project up and running on your local machine for testing purposes. See deployment for notes on how to run the project on a live system.

# Installing

-> install Python3
-> install Git Bash
-> install VirtualBox
-> install Vagrant

# Running

To get this project running you will need to have a virtual machine up and running on your system.
Use commands
-`vagrant up`.
-`vagrant ssh`.
-`cd /vagrant`.
-`psql -d news -f newsdata.sql` to load the database.

and simply Clone or download the Repo and run the news_analysis.py
[GitHub Repo](https://github.com/FatmaMagdy/Log-Analysis-Projoct.git)
by running the command
1.`python news_analysis.py`
