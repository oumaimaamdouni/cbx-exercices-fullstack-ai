from pydantic import BaseModel 
from typing import Optional 

class CVResult(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional [str] = None 
    email: Optional[str] = None 
    phone: Optional[str] = None 
    degree: Optional[str] = None 
    
    