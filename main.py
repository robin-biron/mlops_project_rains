from fastapi import FastAPI, Request, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import secrets

from enum import Enum
from typing import Optional, Set
from fastapi.responses import JSONResponse