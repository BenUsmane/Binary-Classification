from fastApi import FastAPI
from pydantic import BaseModel
import torch
from ..model.model import MyModel
from ..main import model_path
from ..data.data import device


model = MyModel()
model.load_state_dict(torch.load(model_path,map_location=device))

class Input(BaseModel):
    features : list[float]

app = FastAPI()

@app.post("/predict")
def predict(data :Input):
    data = torch.tensor([data.features], dtype= torch.float32)

    with torch.no_grad():
        pred_logit = model(data)

        pred =  torch.round(torch.sigmoid(pred_logit)).cpu().detach().numpy()

        return {
            "the model prediction is " : pred
        }
