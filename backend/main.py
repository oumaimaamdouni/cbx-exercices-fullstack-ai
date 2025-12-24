from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from models.cv_result import CVResult
from services.pdf_parser import extract_text_from_pdf
from services.docx_parser import extract_text_from_docx
from services.extractor import extract_info

app = FastAPI(title ="CV Extractor API", version ="1.0.0")

@app.post("/api/v1/upload-cv", response_model=CVResult)
async def upload_cv(file: UploadFile = File(...)):
   
    extension = file.filename.split(".")[-1].lower()
    if extension not in ["pdf", "docx"]:
        raise HTTPException(status_code=400, detail="Seuls les fichiers PDF et DOCX sont acceptés.")

    temp_path = f"temp_{file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:

        if extension == "pdf":
            raw_text = extract_text_from_pdf(temp_path)
        else:
            raw_text = extract_text_from_docx(temp_path)

        result = extract_info(raw_text)
        
        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors du traitement : {str(e)}")
    
    finally:
        
        if os.path.exists(temp_path):
            os.remove(temp_path)

