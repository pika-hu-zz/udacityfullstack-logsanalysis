# Logs Analysis

> Raymond Hu

## Overview

This is a reporting tool that extracts summaries from a large database containing newspaper articles as awell as the web server log for the newspaper site. The reports generated answer the following questions:

* What are the three most popular articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

## Code Design

* The code interacts with data extracted from the the *newsdata.sql* file (this can be obtained from Udacity)
* Each report uses a single database query to allow for most of the load to be handled by the database, with minimal post-processing by the Ptyhon code

## Technologies Used

* Python3
* PostgreSQL
* Vagrant
* VirtualBox
* Git

## Setup

> Assuming you have Python3, Vagrant, and VitualBox already installed

1. Clone this repository
2. Download the *newsdata.sql* from Udacity and move both *newsdata.sql* and *generate-report.py* (from cloned repository) into the vagrant directory within your VM
3. Start up and log into your VM and change to your vagrant directory
4. Run command ```psql -d news -f newsdata.sql``` to load the data from *newsdata.sql* into your local database
5. Run command ```python3 generate-report.py``` to generate the report