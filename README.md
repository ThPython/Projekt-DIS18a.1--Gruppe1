# Project_Linked Open Data and Knowledge Graphs_DIS18a.1-Group_1 University of Applied Sciences Cologne
## Course of study: Data and Information Science, Prof. Dr. Konrad Förstner and Dr. Eva Seidlmayer

Group members: Aschraf Aouina, Ismail Arda, Felix Borgmann, Yasin Gevrek, Gregory Köskeroglu, Luca Miliziano, Parsa Sarabian and Burghardt Thomas.

[OurGithubPage](https://thpython.github.io/Projekt-DIS18a.1--Gruppe1/)

[Workflow/Meetings](https://pad.gwdg.de/Ip1JREDHRsa1HIvDMc_XCA#Pr%C3%BCfungsleistung)

## Data information

[KnowledgeGraph.gephi](https://github.com/ThPython/Projekt-DIS18a.1--Gruppe1/blob/main/KnowledgeGraph.gephi) Our Gephi project file with corresponding knowledge graphs.

[Unsere_Datei_movieID.csv](https://github.com/ThPython/Projekt-DIS18a.1--Gruppe1/blob/main/Unsere_Datei_movieID.csv) Contains movieID, title, genre and director and their ID for our recommender system.

[Unsere_Datei_movieID_serial.csv](https://github.com/ThPython/Projekt-DIS18a.1--Gruppe1/blob/main/Unsere_Datei_movieID_serial.csv) Sliced 500 dataset raw. For gephi.

[Unsere_Datei_movieID_serial_ref.csv](https://github.com/ThPython/Projekt-DIS18a.1--Gruppe1/blob/main/Unsere_Datei_movieID_serial_ref.csv) Contains Edges or links of the film-ID's. Readable for Gephi.

[Unsere_Ratings.csv](https://github.com/ThPython/Projekt-DIS18a.1--Gruppe1/blob/main/Unsere_Ratings.csv) Includes User Id, movieId and ratings for our recommender system.

[movie_references.py](https://github.com/ThPython/Projekt-DIS18a.1--Gruppe1/blob/main/movie_references.py) Contains our Python code for automating assignments and links to make it readable by the Gephi program.

                    
## Project description and project goal:

In the course of our studies in Data and Information Science at the University of Applied Sciences Cologne, we created the following project in the summer semester of 2020: DIS - Project "Linked Open Data and Knowledge Graphs". 
Using an imdb dataset, which we trimmed down to 500 films, we visualized individual links between films belonging to the same director and the same genre with the help of the program Gephi.
Furthermore, a recommender system was programmed, which provided us with film suggestions. Based on ratings.

The goal is to build a prototype, that based on the ratings and genres, predicts which film is recommended. Also the goal was to design and document the work in such a way that it can be reused and further developed.


## Proceeding:

Our group decided to create a recommender system that recommends movies based on user ratings and the respective genre. 

The idea for this project came from the entertainment platform YouTube. There, videos are suggested based on search histories. We built a Python-based recommender system that uses the IMDB database. The Internet Movie Database is a database of movies and television shows, and the respective people who worked on them. 

This database consists of thousands of movie records. We have focused on only a subset. More specifically, we focused on a total of 500 titles, directors, and ratings from different users. 

To build an initial prototype, we chose 100 records from the Marvel genre to test our recommender system.

Our prototype should later provide ratings or predictions based on vectors in a matrix, which movies seem to be recommendable. The test corpus should be extended after successful implementation.

In order to establish the relation to knowledge graphs, the individual genres and titles of our dataset were related. The visualization was done by the software Gephi. As preliminary work In Gehpi, two independent CSV files, a rating file and the film database truncated to 500 records, were linked via an inner joint so that film, genre and director, could be uniquely assigned.

Films of the same type were connected by edges and nodes represent different types. The clustering clearly shows which films are recommended. 
In Gehpi, two independent CSV files, a rating file and the film database truncated to 500 records, were linked via an inner joint so that film, genre and director could be uniquely assigned.


## Structure of the system (implementation) and data:

## Data basis

As a data basis serves a Csv file, which we have compiled from various databases. This Csv file is called "Unsere_Datei_movieID.csv". 
We took the columns "Title", "Genre" and "Director" from the IMDB-Movie-Data.csv, which contains the 1000 most popular movies of the [IMDB](https://www.kaggle.com/PromptCloudHQ/imdb-data).
For the genres, we decided to take only the first mentioned genre so that the visualization in Gephi would not look too complex.
We cut the dataset to 500 movies, otherwise the resource overhead would be too large.

Since we need user ratings for the recommender system, which the [MovieLens database](https://grouplens.org/datasets/movielens/25m/) provides, we added an "ID" column to our csv file. Using SVERWEIS we added the corresponding "movieId" from the "movies.csv" of the MovieLens database to each movie.
Using this ID we can access the userratings from the "ratings.csv" file.   

## Gephi

Gephi is a visualization software for all types of graphics. It is open source and free of charge. In our project we used Gephi for a knowledge graph. We chose this software because it is very easy to use. It is very easy to combine two or more values, which is important for the creation of a knowledge graph and was crucial for us. For Gephi, in most cases you read two CSV files that contains the values you want to connect. The software then creates the connections, resulting in a Knowledge Graph.

In our Gephi project there are nodes and edges. The nodes are 500 movies from several genres. The different genres are as follows:
Action, Adventure, Drama, Biography, Animation, Comedy, Crime and Horror.

In addition, our input file, which contains the 500 movies, also contains the associated genres and the directors of each movie. We used the input file to create our "Our_File_movieID_serial_ref.csv" using our automation code, which we wrote using Python. There are two columns in the "Our_File_movieID_serial_ref.csv" file. The Source and Target columns tell which movies in our Knowledge Graph should be linked together. All movies in this file that have the same genre and director will be linked. These links were created using automation code. The Python code is located in the Python file "movie_references.py". After creating the two CSV files, they were imported into Gephi via the data lab. The Knowledge Graph now shows us the movies that have the same director and genre. Edges with a thick arrow are the connection of films with the same director. The thinner lines or connections represent the genre. Our graph is a directed graph with 47558 edges. That means we have 47558 connections at 499 nodes. For the layout we chose the "Fruchterman Reingold" layout, because this layout shows a nice cluster. 

Requirements to run the knowledge graph:

- [Gephi](https://gephi.org/users/download/)
- [Java SE Runtime Environment 8](https://www.oracle.com/java/technologies/javase-jre8-downloads.html)
- KnowledgeGraph.gephi

This code was tested on a system with the following specifications:

- operating system: Windows 10
- CPU: Intel i5
- memory (RAM): 16GB


## Recommender System 

The goal was to program a recommender system that gives movie recommendations for a movie entered by the user. To build our recommender system we chose Jupyter Notebook, which is included with the installation of [Anaconda](https://www.anaconda.com/products/individual). However, any Python program can be used. The installation of Anaconda is free of charge.
The Recommender System recommends movies based on userratings, which are included in the MovieLens dataset. To recommend a movie, the program calculates the correlation of the ratings of all users of the entered movie to the ratings of all movies in the dataset. 
Only movies that have received at least 100 ratings are recommended.
After running the program, the user has the possibility to enter a movie again for which recommendations should be provided. As soon as the user enters "exit" as a movie name, the loop is terminated. 


This code was tested on a system with the following specifications:

- operating system: Windows 10
- CPU: I7-4790k
- memory (RAM): 24 GB
- disk storage: 1000 GB
- GPU: Geforce RTX 3070

The main software requirements are Python, Excel and Gephi.


## Hardware and Software Requirements
(.txt) Installationsanleitung:

To install all required  python packages, execute
```
pip install -r requirements.txt
```

## Outlook

In addition to Gephi, NetworkX is also available for visualization.  NetworkX is a Python package for the creation, manipulation, and study of the structure, dynamics, and functions of complex networks.  NetworkX would be an alternative that we could consider to improve our recommender system.

Because so far we have incorporated 500 film titles, directors and ratings from various users for the recommender system.  We would also like to expand this corpus in order to be able to create further connections in Gephi with the previous and the additional data.  The more extensive our corpus, the better we can deliver specific results for the user.

In addition, we would like to incorporate further search criteria.  For example, users should be able to filter their favorite actors or search for the location and year of the film's release. Furthermore, we could think about an extension by means of [People2Vec](https://github.com/People2Vec).





