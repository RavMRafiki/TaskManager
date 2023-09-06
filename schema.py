from pydantic import BaseModel
from typing import Optional

class task_schema(BaseModel):
   id : Optional[int]
   task_name :str
   task_des :str
   created_by : Optional[str]= None
   date_created : Optional[str]= None

   class Config:
       from_attributes = True