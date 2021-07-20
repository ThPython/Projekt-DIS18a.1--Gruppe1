# Project_Linked Open Data und Knowledge Graphs_DIS18a.1--Group_1 University of Applied Sciences Cologne
## Course of study: Data and Information Science, Prof. Dr. Konrad Förstner and Dr. Eva Seidlmayer

Group members: Aschraf Aouina, Ismail Arda, Felix Borgmann, Yasin Gevrek, Gregory Köskeroglu, Luca Miliziano, Parsa Sarabian und Burghardt Thomas.

[UnsereGithubPage](https://thpython.github.io/Projekt-DIS18a.1--Gruppe1/)
                    
## Project description and project goal:

In the course of our studies in Data and Information Science at the University of Applied Sciences Cologne, we created the following project in the summer semester of 2020: DIS - Project "Linked Open Data and Knowledge Graphs". 
Using an imdb dataset, which we trimmed down to 500 films, we visualized individual links between films belonging to the same director and the same genre with the help of the program Gephi.
Furthermore, a recommender system was programmed, which provided us with film suggestions. Based on the same director and the same genre.

The goal was to design and document the work in such a way that it could be reused and further developed.


## Proceeding: Our group decided to create a recommendation system that recommends movies based on user ratings and the respective genre. 

The idea for this project came from the entertainment platform YouTube. There, videos are suggested based on search histories. We built a Python-based recommendation system that uses the IMDB database. The Internet Movie Database is a database of movies and television shows, and the respective people who worked on them. 

This database consists of thousands of movie records. We have focused on only a subset. More specifically, we focused on a total of 500 titles, directors, and ratings from different users. 

To build an initial prototype, we chose 100 records from the Marvel genre to test our recommender system.

Our prototype should later provide ratings or predictions based on vectors in a matrix, which movies seem to be recommendable. The test corpus should be extended after successful implementation.

In order to establish the relation to knowledge graphs, the individual genres and titles of our dataset were related. The visualization was done by the software Gephi. As preliminary work In Gehpi, two independent CSV files, a rating file and the film database truncated to 500 records, were linked via an inner joint so that film, genre and director, could be uniquely assigned.


Films of the same type were connected by edges and nodes represent different types. The clustering clearly shows which films are recommended. 
In Gehpi, two independent CSV files, a rating file and the film database truncated to 500 records, were linked via an inner joint so that film, genre and director could be uniquely assigned.



## Structure of the system (implementation) and data: Recommender und Gephi. Jedes Team für sich, bitte! Voraussetzungen Hardware und Software.
Gephi (Ismail und Gregory)
Hardware and Software Instructions--> Das sind nur Platzhalter. Bitte entsprechend ausfüllen oder zumindest sinngemäß ähnliches eintragen.

This code was tested on a system with the following specifications:

- operating system: Windows 10
- CPU: Intel i5
- memory (RAM): 16GB
- disk storage: 500GB
- GPU: NVIDIA Titan 

The main software requirements are Python 3.7


## Recommender System (bitte ab hier)

Hardware and Software Instructions--> Das sind nur Platzhalter. Bitte entsprechend ausfüllen.


This code was tested on a system with the following specifications:

- operating system: Windows 10
- CPU: I7-4790k
- memory (RAM): 24 GB
- disk storage: 1000 GB
- GPU: Geforce RTX 3070

The main software requirements are Python, Excel and Gehphi



## Team: Hardware and Software Requirements
(.txt) Installationsanleitung: Gephi und Recommender. pip install etc. Yasin und Eazy, Installationsanteilung inkl. Abhängigkeiten

To install all required  python packages, execute
```
pip install -r requirements.txt
```


## Outlook: Mehr Verbindungen unter Gephi--> im Pad nachschauen. Spezialist! Parsa.

## Anhang ??? notwendig?
  - Archiv und Glossar

## Übersichtsgraphik??? Wer kann? Evtl. MIttwochvormittag



