from model.model import MyModel
from model.train import train
from torch import nn, optim
from data.data import train_loader, val_loader


model = MyModel()

loss_function = nn.BCEWithLogitsLoss()
opt = optim.Adam(model.parameters(), lr = 0.001)


epochs = 100
if __name__ == "__main__":
    train(epochs,model,loss_function, opt,train_loader,val_loader)