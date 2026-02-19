from model.model import MyModel
from model.train import train
from torch import nn, optim
from data.data import train_loader, val_loader
import matplotlib.pyplot as plt


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
plt.plot(accu_iteration, accu_train_accuracy, c='red')
plt.plot(accu_iteration, accu_val_accuracy, c='green')

plt.legend(['train accuracy', 'val accuracy'])
plt.xlabel('iteration')
plt.ylabel('accuracy')


plt.show()