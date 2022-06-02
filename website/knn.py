#!/usr/bin/env python3

# Written by Ivona Obonova
# 22.2.2022

import pandas as pd
import sklearn.neighbors

class Knn:
    def init():
        Knn.books = pd.read_csv(
            'data/BX-CSV-Dump/BX-Books.csv',
            sep=';',
            usecols=[0, 1, 2],
            quoting=1,
            escapechar='\\',
            encoding='latin-1'
        )
        Knn.ratings = pd.read_csv(
            'data/BX-CSV-Dump/BX-Book-Ratings.csv',
            sep=';',
            quoting=1,
            escapechar='\\',
            encoding='latin-1'
        )

        Knn.ratings = Knn.ratings[Knn.ratings['Book-Rating'] != 0]
        counts      = Knn.ratings['User-ID'].value_counts()
        reviewers   = Knn.ratings[Knn.ratings['User-ID'].isin(counts[counts >= 10].index)]
        counts      = Knn.ratings['ISBN'].value_counts()
        popular     = Knn.ratings[Knn.ratings['ISBN'].isin(counts[counts >= 50].index)]

        Knn.ratings = pd.merge(reviewers, popular, how='inner')
        Knn.books   = Knn.books[Knn.books['ISBN'].isin(Knn.ratings['ISBN'])]


    def find(title):
        return Knn.books.loc[Knn.books['Book-Title'].str.contains(title, case=False)]


    def knn(isbn):
        matrix = Knn.ratings.pivot(index='ISBN', columns='User-ID', values='Book-Rating').fillna(0)
        knn = sklearn.neighbors.NearestNeighbors(metric='cosine', algorithm='brute').fit(matrix)
        distances, indices = knn.kneighbors(matrix.loc[isbn].values.reshape(1, -1), n_neighbors=6)

        recommended = [ ]
        for i in range(1, len(indices[0])):
            index = indices[0][i]
            recommended.append(Knn.books[Knn.books['ISBN'] == matrix.index[index]].iloc[0])
        return recommended
