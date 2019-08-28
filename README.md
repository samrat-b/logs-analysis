Project: Logs Analysis
========================

Project Details:
-----------------
This project requires to create a reporting tool, querying database having 
real world like data. Output of the queries is depicted at terminal. A 
Python program is been created for this project, which connects to database 
using psycopg2 library. There is a corresponding method with respect to each 
of the below questions:

- What are the most popular three articles of all time?    -> most_pop_art()
- Who are the most popular article authors of all time?    -> pop_art_auth()
- On which days did more than 1% of requests lead to errors?   -> err_logs()

Setup Runtime Environment
--------------------------    
It is recommended to set up the environment first like the one is used to 
develop this program. 

> Install Vagrant: 
Download Vagrant software using URL "https://www.vagrantup.com/downloads.html"
, then install the version respective to your OS.

> Install VirtualBox:
Download VirtualBox using URL 
"https://www.virtualbox.org/wiki/Download_Old_Builds_5_1", then install the 
version respective to your OS.

> Download VM Configuration:
Download VM Configuration using URL 
"https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip"    

How to run the program:
------------------------
Download the data using URL 
"https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip". 
Open the git bash from the path, where Virtual Machine is set up in the local 
system. Run below commands in order to execute the reporting tool:

    1: "vagrant up"     - to bring virtual machine online
    2: "vagrant ssh"    - to login to virtual machine
    3: "cd /vagrant"    - to access the shared folder
    4: "psql -d news -f newsdata.sql" - to load the data
    5: "psql -d news"   - to connect to the database. 
    6: Then exit from database
    7: "python logs.py" - to run the reporting tool  
