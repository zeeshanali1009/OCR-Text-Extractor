from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from utils.ocr_model import extract_text

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/ocr")
async def ocr_endpoint(file: UploadFile = File(...)):
    image_bytes = await file.read()
    try:
        text = extract_text(image_bytes)
        return {"text": text}
    except Exception as e:
        return {"error": f"Failed to extract text: {str(e)}"}
