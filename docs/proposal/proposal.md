# School of Computing &mdash; Year 4 Project Proposal Form


## SECTION A

|                     |                   |
|---------------------|-------------------|
|Project Title:       | StudySmart            |
|Student 1 Name:      | Shannon Mulgrew   |
|Student 1 ID:        | 16304263            |
|Student 2 Name:      | Sian   Lennon         |
|Student 2 ID:        | 16343896            |
|Project Supervisor:  | Andy Way            |



## SECTION B

### Introduction

Our proposed project is a Python web app to help the school of computing students while studying. The application will allow users to upload text or link a webpage, from which a number of questions can be generated.
The answers the user will give for the questions will be corrected by the application and then release a score to the user.
This web-app will be designed to help students prepare and practice for an exam. 
For the moment we are focusing on CASE 4 modules to train our data as we are most familiar with that. 
Once we feel it performs to standard we can expand to other modules within School of Computing.


### Outline

The application can be broken down into several components.

<br />
The main aspect of the project is Natural Language Processing. The application will read in any text/Webpage, then process and extract information in order to to creat questions and answers on that text.

The bulk of the project is the AI for creating questions and answers. For this we will need to work with Natural language processing, applying regular expressions to the text in order to create questions based on statements.


<br />

The other components consist of  
- A text uploader.
- A ‘scoring system’.
- A HTML linking and scraping system.
- A log-in/account system
- A database 
- A user interface.
- AWS Server.
- Docker continers.


### Background

The idea came about when reading about Natural Language processing and that it could be used for creating questions from text. We thought that this could be implemented well for students trying to learn and thought of this app. We realised that as 4th year computing students, this sort of application would be very useful for our modules. 

### Achievements

We hope to achieve an all inclusive app for School of Computing Students to be quizzed on their notes and topics. The user should also be able to log-in and out of the app with their score for each text uploaded displayed for them. 



### Justification

Rather than just reading off a set of notes, people could be quizzed on their topic and receive a ‘score’ based on their knowledge of these notes.

We believe this will greatly benefit anyone studying for exams, specifically students coming up to exam season.


### Programming language(s)

- Python - Backend/NLTK 
- SQL - For database in backend.
- HTML - For frontend.
- CSS - For frontend.
- JavaScript - For dynamic frontend.
- Markdown - Docs

### Programming tools / Tech stack

- Django - Framework for backend and frontend.
- MySQL/Firebase - Database management.
- Visual studio - text editor.
- Selenium - Automation Testing.
- Boostrap - Library.
- AWS - Amazon web services web hosting
- Docker - Containers


### Learning Challenges

The Natural Language Processing will be a challenge as we have never attempted a project in this area before. Docker and AWS are new to us and implementing this will reqiure research also.



New Tech:


- SQL/Firebase
- Boostrap
- AWS
- Docker


### Breakdown of work

The work will be split evenly with Sian taking the lead on creating the Natural Language Processing and Shannon working on the django app setup. The AWS and docker containers will be created together. Docs will be split evenly.


#### Student 1: Shannon

1. Django setup.
2. Link with database.
3. Text uploader.
4. HTML scraper.
5. User Interface.
6. Create Docker containers for components.
7. Set up AWS with Django and Docker containers.
8. User testing.


#### Student 1: Sian

1. Natural Language processing research.
2. NLP implementation.
3. NLP training.
4. NLP testing.
5. Create Docker containers for components.
6. Set up AWS with Django and Docker containers.
7. Linking with application.
8. Automation testing.
