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

# with open('/app/sample_1.json') as json_data:
#     sample_1 = json.load(json_data)

# with open('sample_2.json') as json_data:
#     sample_2 = json.load(json_data)

sample_1 = {   "Year":2022,
    "Month":5,
    "Day":1,
    "MinTemp":15,
    "MaxTemp":25,
    "Rainfall":33,
    "Evaporation":20, 
    "Sunshine":7,
    "WindGustSpeed":50,
    "WindSpeed9am":20,
    "WindSpeed3pm":30,
    "Humidity9am":20,
    "Humidity3pm":30,
    "Pressure9am":1013,
    "Pressure3pm":1013,
    "Cloud9am":3,
    "Cloud3pm":3,
    "Temp9am":18,
    "Temp3pm":23, 
    "RainToday_No":0,
    "RainToday_Yes":1,

    "Location_Adelaide":0,
    "Location_Brisbane":0,
    "Location_Canberra":0,
    "Location_GoldCoast":0,
    "Location_Melbourne":0,
    "Location_Newcastle":0,
    "Location_Perth":0,
    "Location_Sydney":1,
    
    "WindGustDir_0.0":1,
    "WindGustDir_E":0,
    "WindGustDir_ENE":0,
    "WindGustDir_ESE":0,
    "WindGustDir_N":0,
    "WindGustDir_NE":0,
    "WindGustDir_NNE":0,
    "WindGustDir_NNW":0,
    "WindGustDir_NW":0,
    "WindGustDir_S":0,
    "WindGustDir_SE":0,
    "WindGustDir_SSE":0,
    "WindGustDir_SSW":0,
    "WindGustDir_SW":0,
    "WindGustDir_W":0,
    "WindGustDir_WNW":0, 
    "WindGustDir_WSW":0,
    
    "WindDir9am_E":1,
    "WindDir9am_ENE":0,
    "WindDir9am_ESE":0,
    "WindDir9am_N":0,
    "WindDir9am_NE":0,
    "WindDir9am_NNE":0,
    "WindDir9am_NNW":0,
    "WindDir9am_NW":0,
    "WindDir9am_S":0,
    "WindDir9am_SE":0,
    "WindDir9am_SSE":0,
    "WindDir9am_SSW":0,
    "WindDir9am_SW":0,
    "WindDir9am_W":0,
    "WindDir9am_WNW":0,
    "WindDir9am_WSW":0,
    
    "WindDir3pm_E":1,
    "WindDir3pm_ENE":0,
    "WindDir3pm_ESE":0,
    "WindDir3pm_N":0,
    "WindDir3pm_NE":0,
    "WindDir3pm_NNE":0,
    "WindDir3pm_NNW":0,
    "WindDir3pm_NW":0,
    "WindDir3pm_S":0,
    "WindDir3pm_SE":0,
    "WindDir3pm_SSE":0,
    "WindDir3pm_SSW":0,
    "WindDir3pm_SW":0,
    "WindDir3pm_W":0,
    "WindDir3pm_WNW":0,
    "WindDir3pm_WSW":0
}

sample_2 = {   "Year":2022,
    "Month":5,
    "Day":3,
    "MinTemp":10,
    "MaxTemp":12,
    "Rainfall":45,
    "Evaporation":20, 
    "Sunshine":7,
    "WindGustSpeed":50,
    "WindSpeed9am":35,
    "WindSpeed3pm":30,
    "Humidity9am":20,
    "Humidity3pm":30,
    "Pressure9am":1013,
    "Pressure3pm":1013,
    "Cloud9am":3,
    "Cloud3pm":3,
    "Temp9am":18,
    "Temp3pm":23, 
    "RainToday_No":0,
    "RainToday_Yes":1,

    "Location_Adelaide":0,
    "Location_Brisbane":0,
    "Location_Canberra":0,
    "Location_GoldCoast":0,
    "Location_Melbourne":0,
    "Location_Newcastle":0,
    "Location_Perth":0,
    "Location_Sydney":1,
    
    "WindGustDir_0.0":1,
    "WindGustDir_E":0,
    "WindGustDir_ENE":0,
    "WindGustDir_ESE":0,
    "WindGustDir_N":0,
    "WindGustDir_NE":0,
    "WindGustDir_NNE":0,
    "WindGustDir_NNW":0,
    "WindGustDir_NW":0,
    "WindGustDir_S":0,
    "WindGustDir_SE":0,
    "WindGustDir_SSE":0,
    "WindGustDir_SSW":0,
    "WindGustDir_SW":0,
    "WindGustDir_W":0,
    "WindGustDir_WNW":0, 
    "WindGustDir_WSW":0,
    
    "WindDir9am_E":1,
    "WindDir9am_ENE":0,
    "WindDir9am_ESE":0,
    "WindDir9am_N":0,
    "WindDir9am_NE":0,
    "WindDir9am_NNE":0,
    "WindDir9am_NNW":0,
    "WindDir9am_NW":0,
    "WindDir9am_S":0,
    "WindDir9am_SE":0,
    "WindDir9am_SSE":0,
    "WindDir9am_SSW":0,
    "WindDir9am_SW":0,
    "WindDir9am_W":0,
    "WindDir9am_WNW":0,
    "WindDir9am_WSW":0,
    
    "WindDir3pm_E":1,
    "WindDir3pm_ENE":0,
    "WindDir3pm_ESE":0,
    "WindDir3pm_N":0,
    "WindDir3pm_NE":0,
    "WindDir3pm_NNE":0,
    "WindDir3pm_NNW":0,
    "WindDir3pm_NW":0,
    "WindDir3pm_S":0,
    "WindDir3pm_SE":0,
    "WindDir3pm_SSE":0,
    "WindDir3pm_SSW":0,
    "WindDir3pm_SW":0,
    "WindDir3pm_W":0,
    "WindDir3pm_WNW":0,
    "WindDir3pm_WSW":0
}

sample_3 = {   "Year":2022,
    "Month":5,
    "Day":3,
    "MinTemp":"froid",
    "MaxTemp":12,
    "Rainfall":45,
    "Evaporation":20, 
    "Sunshine":7,
    "WindGustSpeed":50,
    "WindSpeed9am":35,
    "WindSpeed3pm":30,
    "Humidity9am":20,
    "Humidity3pm":30,
    "Pressure9am":1013,
    "Pressure3pm":1013,
    "Cloud9am":3,
    "Cloud3pm":3,
    "Temp9am":18,
    "Temp3pm":23, 
    "RainToday_No":0,
    "RainToday_Yes":1,

    "Location_Adelaide":0,
    "Location_Brisbane":0,
    "Location_Canberra":0,
    "Location_GoldCoast":0,
    "Location_Melbourne":0,
    "Location_Newcastle":0,
    "Location_Perth":0,
    "Location_Sydney":1,
    
    "WindGustDir_0.0":1,
    "WindGustDir_E":0,
    "WindGustDir_ENE":0,
    "WindGustDir_ESE":0,
    "WindGustDir_N":0,
    "WindGustDir_NE":0,
    "WindGustDir_NNE":0,
    "WindGustDir_NNW":0,
    "WindGustDir_NW":0,
    "WindGustDir_S":0,
    "WindGustDir_SE":0,
    "WindGustDir_SSE":0,
    "WindGustDir_SSW":0,
    "WindGustDir_SW":0,
    "WindGustDir_W":0,
    "WindGustDir_WNW":0, 
    "WindGustDir_WSW":0,
    
    "WindDir9am_E":1,
    "WindDir9am_ENE":0,
    "WindDir9am_ESE":0,
    "WindDir9am_N":0,
    "WindDir9am_NE":0,
    "WindDir9am_NNE":0,
    "WindDir9am_NNW":0,
    "WindDir9am_NW":0,
    "WindDir9am_S":0,
    "WindDir9am_SE":0,
    "WindDir9am_SSE":0,
    "WindDir9am_SSW":0,
    "WindDir9am_SW":0,
    "WindDir9am_W":0,
    "WindDir9am_WNW":0,
    "WindDir9am_WSW":0,
    
    "WindDir3pm_E":1,
    "WindDir3pm_ENE":0,
    "WindDir3pm_ESE":0,
    "WindDir3pm_N":0,
    "WindDir3pm_NE":0,
    "WindDir3pm_NNE":0,
    "WindDir3pm_NNW":0,
    "WindDir3pm_NW":0,
    "WindDir3pm_S":0,
    "WindDir3pm_SE":0,
    "WindDir3pm_SSE":0,
    "WindDir3pm_SSW":0,
    "WindDir3pm_SW":0,
    "WindDir3pm_W":0,
    "WindDir3pm_WNW":0,
    "WindDir3pm_WSW":0
}



samples = {"sample 1" : sample_1, "sample 2" : sample_2, "sample 3": sample_3
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



# if __name__ == "__main__":
#     uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=False, root_path="/")

# method that enables user to add its test data to samples list

# from typing import Optional

# from fastapi import FastAPI
# from pydantic import BaseModel

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



    

