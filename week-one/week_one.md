Day 1: Introduce vectors as feature representations in ML

Vectors are the atomic unit of Machine Learning. 
Vectors are an ordered list of numbers that represents something. They represent data in numerical form because ML models only understand numbers. 
Each number in a vector is a feature. 
Stacked up vectors (dataset) are a matrix. 
Embeddings are learned vectors. 
Neural networks are repeated vector operations.  

Exercise 
Why is a dataset just a collection of vectors?
Because ML models are a mathematical function. ML models can only evaluate numeric functions. 

Why can’t ML models work with raw text directly?
ML models are just computers at the end of the day. Feeding raw text has no meaning to it. There can't be any comparison between words etc. Like embeddings allow to measure similarity and rertrieve relevant information. Words that have a semantic relationship have similar embeddings. 

Why must everything be converted into numbers?
Because ML models --> computers --> need numbers to make value out of everything 

A resume scoring model --> Vector could contain --> x =([numberOfjobs, yearsOfExperience, numberOfDegrees]) ( Example I gave is not best because it wouldnt be able to distinguish 2 candidates with that same vector, it is best to be precise and use the following features: skill similarity, role similarity, career trajectory patterns, these actually make a difference)
A fraud detector --> amount, currency, location 
A recommendation engine --> age, gender, location 