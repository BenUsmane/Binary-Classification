from model.model import MyModel
from model.train import train
from torch import nn, optim
from data.data import train_loader, val_loader
import matplotlib.pyplot as plt
import torch


model = MyModel()

loss_function = nn.BCEWithLogitsLoss()
opt = optim.Adam(model.parameters(), lr = 0.001)


epochs = 50
if __name__ == "__main__":
    accu_train_loss, accu_val_loss, accu_train_accuracy, accu_val_accuracy, accu_train_precision, accu_val_precision, accu_iteration, model =train(
        epochs,
        model,
        loss_function,
        opt,
        train_loader,
        val_loader
    )
    fig , axis = plt.subplots(2,2, figsize=(10,10))

    axis[0,0].plot(accu_iteration, accu_train_accuracy, c='red')
    axis[0,0].plot(accu_iteration, accu_val_accuracy, c='green')
    axis[0,0].legend(["train accuracy", "val accuracy"])
    axis[0,0].set_xlabel('iteration')
    axis[0,0].set_ylabel('accuracy')

    axis[0,1].plot(accu_iteration, accu_train_precision, c='red')
    axis[0,1].plot(accu_iteration, accu_val_precision, c='green')
    axis[0,1].legend(["train precision", "val precision"])
    axis[0,1].set_xlabel('iteration')
    axis[0,1].set_ylabel('Precision')

    axis[1,0].plot(accu_iteration, accu_train_loss, c='red')
    axis[1,0].plot(accu_iteration, accu_val_loss, c='green')
    axis[1,0].legend(["train Loss", "val Loss"])
    axis[1,0].set_xlabel('iteration')
    axis[1,0].set_ylabel('Loss')
    
    plt.show()
    torch.save(model.state_dict(),'./model.pth')
    