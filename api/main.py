from fastapi import FastAPI, Header, HTTPException,Depends,status,  Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets
import pickle
import json
import pandas as pd

from enum import Enum
from typing import Optional, Set
from fastapi.responses import JSONResponse

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel


api = FastAPI(title='Rain prediction for tomorrow @Datascientest')


# define objects

models = { "Logistic regression" :"final_model_lr.pkl",
                "Support Vector":'final_model_svm.pkl',
                "KNN":'final_model_knn.pkl',
                "Decision Tree":'final_model_dtc.pkl',
                "Boosting":'final_model_adaboost.pkl',
                "Random Forest":'final_model_rfc.pkl',
            }

with open('sample_1.json') as json_data:
    sample_1 = json.load(json_data)

with open('sample_2.json') as json_data:
    sample_2 = json.load(json_data)

samples = {"sample 1" : sample_1, "sample 2" : sample_2
        }

# Identity & Access Management

security = HTTPBasic()

@api.get("/Login")
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):

    if (not credentials.username=='bob' or not credentials.password=='builder') and \
       (not credentials.username=='alice' or not credentials.password=='wonderland') and \
       (not credentials.username=='clementine' or not credentials.password=='mandarine'):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return credentials.username

# method that generates prediction based on user model's preference
@api.get("/select_model")
async def predict_unique_data(
    model:str = Query("Logistic regression",enum=list(models.keys())),
    test_data:str = Query("sample 1", enum=list(samples.keys())),
    username: str = Depends(get_current_username)):
    
    """
     This method predicts whether or not it will rain for the next day
    """
    if model in models:
        if test_data in samples:
            model_file = pickle.load( open( models[model], "rb" ) )
            sample = samples[test_data]

            df = pd.DataFrame([sample])
            rain_tomorow = model_file.predict(df)

            return {"username": username,
                "rain_tomorow": rain_tomorow[0],
                    }
        else:
            raise HTTPException(
            status_code=405,
            detail='Unknown Sample')
    else:
            raise HTTPException(
            status_code=404,
            detail='Unknown Model')


# method that enables user to add its test data to samples list

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

## new data needs to be preprocessed before prediction
# class RainSampleData(BaseModel):
#     name: str
#     description: Optional[str] = None
#     price: float
#     tax: Optional[float] = None
#     Date
#     Location
#     MinTemp
#     MaxTemp
#     Rainfall
#     Evaporation
#     Sunshine', 'WindGustDir', 'WindGustSpeed', 'WindDir9am', 'WindDir3pm',
#        'WindSpeed9am', 'WindSpeed3pm', 'Humidity9am', 'Humidity3pm',
#        'Pressure9am', 'Pressure3pm', 'Cloud9am', 'Cloud3pm', 'Temp9am',
#        'Temp3pm', 'RainToday', 'RainTomorrow'


# @api.post("/add_sample_data/")
# async def add_samples(sample: str, username: str = Depends(get_current_username)):
#     """
#      This method enables a user to add its test data to samples list, that will later be used for prediction
#     """



    

