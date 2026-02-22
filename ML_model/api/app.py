from fastapi import FastAPI
from pydantic import BaseModel
import torch
from torch import nn


class MyModel(nn.Module):
    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(30, 20)
        self.layer2 = nn.Linear(20, 10)
        self.layer3 = nn.Linear(10, 1)
        self.relu = nn.ReLU()

    def forward(self, x):
        x = self.relu(self.layer1(x))
        x = self.relu(self.layer2(x))
        z = self.layer3(x)
        return z


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = MyModel().to(device)


model.load_state_dict(torch.load("model.pth", map_location=device))

model.eval()


class Input(BaseModel):
    features: list[float]


app = FastAPI()


@app.post("/predict")
def predict(data: Input):
    if data.features is None or len(data.features) != 30:
        return {"error": "Invalid input. Please provide a list of 30 features."}
    data = torch.tensor([data.features], dtype=torch.float32).to(device)

    with torch.no_grad():
        print(data.shape)
        pred_logit = model(data)

        prob = torch.sigmoid(pred_logit)
        pred = torch.round(torch.sigmoid(prob))

        final_pred = int(pred.item())

        return {
            "the model prediction is ": final_pred,
            "the probability is ": prob.item(),
            "status": "Healthy" if final_pred == 0 else "Bread cancer is present",
        }
