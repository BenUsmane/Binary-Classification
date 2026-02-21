from fastapi import FastAPI
from pydantic import BaseModel
import torch
from model.model import MyModel
from data.data import device
import uvicorn

model = MyModel()


model.load_state_dict(torch.load('api/model.pth', map_location=device))
model.eval()


class Input(BaseModel):
    features: list[float]


app = FastAPI()


@app.post("/predict")
def predict(data: Input):
    data = torch.tensor([data.features], dtype=torch.float32)

    with torch.no_grad():
        print(data.shape)
        pred_logit = model(data)

        pred = torch.round(torch.sigmoid(pred_logit))
        prob = torch.sigmoid(pred_logit).item()
        final_pred = int(pred.item())

        return {"the model prediction is ": final_pred, 
                "the probability is " : prob,
                "status" : "Healthy" if final_pred == 0 else "Bread cancer is present"
                }
