import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import sigmoid_kernel
from sklearn.feature_extraction.text import TfidfVectorizer

steam_data = pd.read_csv("Msteam.csv")
print("Game Data: ", steam_data.shape)
steam_data = steam_data.rename(index=str, columns={"steamspy_tags": "tags"})

#Calcultaion formula for finding the precent simulatiries based on TF-IDF
comp = TfidfVectorizer(min_df=3,  max_features=None, strip_accents='unicode', analyzer='word',token_pattern=r'\w{1,}', ngram_range=(1, 3), use_idf=1,smooth_idf=1,sublinear_tf=1, stop_words = 'english')

#Preps the tags to be read
steam_data["tags"] = steam_data["tags"].fillna("")

#Calculates the percents
comp_matrixG = comp.fit_transform(steam_data["tags"])

#Stores the computed values
compMatrix = sigmoid_kernel(comp_matrixG, comp_matrixG)

#Get rid of Duplicate Values
index = pd.Series(steam_data.index, index=steam_data["name"]).drop_duplicates()

def recomend(title, compMatrix=compMatrix):
    idx = index[title]
    relation = list(enumerate(compMatrix[int(idx)]))

    #Sorts the games based on relation score
    relation = sorted(relation, key=lambda x: x[1], reverse=True)

    #Returns the top 10 most similar games
    relation = relation[1:11]
    game_idx = [i[0] for i in relation]
    return steam_data["name"].iloc[game_idx]

print("What is a game you enjoyed?")
game = input()
print("Here are the top 10 games you might enjoy:")
print(recomend(game))