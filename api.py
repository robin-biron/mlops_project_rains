from fastapi import FastAPI, Header, HTTPException,Depends,status,  Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import pickle
import json
import pandas as pd

from enum import Enum
from typing import Optional, Set
from fastapi.responses import JSONResponse


api = FastAPI(title='Rain prediction for tomorrow @Datascientest')

model_dico = { "Logistic regression" :"final_model_lr.pkl",
                "Support Vector":'final_model_svm.pkl',
                "KNN":'final_model_knn.pkl',
                "Decision Tree":'final_model_decision_tree.pkl',
                "Boosting":'final_model_adaboost.pkl',
                "Random Forest":'final_model_random_forest.pkl',
            }

@api.get("/")
async def get_prevision(model:str = Query("Logistic regression",enum=list(model_dico.keys()) )):
 
    model_file = pickle.load( open( model_dico[model], "rb" ) )
 
    with open('feature.json') as json_data:
        feature = json.load(json_data)
        #print(feature)

    df = pd.DataFrame([feature])
    rain_tomorow = model_file.predict(df)

    return {"rain_tomorow": rain_tomorow[0]}
