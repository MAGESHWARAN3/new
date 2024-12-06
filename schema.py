from typing import Optional
from pydantic import BaseModel


class withdraw(BaseModel):
     account_id:int
     amount:float