from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from PIL import Image
from utils import load_model, predict_image
from gemini import get_style_tips

app = FastAPI()
model = load_model()


class LabelRequest(BaseModel):
    label: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image = Image.open(file.file).convert("RGB")
    label = predict_image(image, model)
    return {"prediction": label}


@app.post("/suggest")
async def suggest(req: LabelRequest):
    tips = get_style_tips(req.label)
    return {"tips": tips}
