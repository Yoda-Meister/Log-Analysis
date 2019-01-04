# Logs Analysis
This is a project for Udacity's [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

The task is to create a reporting tool that prints out reports (in plain text) 
based on the data in the database. This reporting tool is a Python program 
using the psycopg2 module to connect to the database.

The reporting tool is used to answer these 3 questions:

1. What are the most popular three articles of all time?

2. Who are the most popular article authors of all time?

3. On which days did more than 1% of requests lead to errors?

## How to run:

## 1. Setup
1. Install [Vagrant](https://www.vagrantup.com/)
2. Install [VirtualBox](https://www.virtualbox.org/)
3. Download the vagrant setup files from [Udacity's Github](https://github.com/udacity/fullstack-nanodegree-vm)
4. Download the database setup: [Data](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
5. Unzip the data to get the newsdata.sql file and put the newsdata.sql file into the vagrant directory
6. Download the project
7. Unzip and copy all the files into the vagrant directory

## 2. Start VM
1. Open the terminal and navigate to the project folder
2. cd into vagrant and run ``` vagrant up ``` to start the VM
3. Once done, run ``` vagrant ssh ``` to connect
4. cd to the project directory

## 3. Load the data and run the project:
1. Load the data with this command ``` psql -d news -f newsdata.sqpl ```
2. Run ``` python logs-analysis.py ``` to run the project

## Output:
Expected to be identical to the text in the output.txt file