
from model.model import MyModel
import torch
from torch import nn, optim
from sklearn.metrics import accuracy_score, precision_score


device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model = MyModel().to(device)
loss_function = nn.BCEWithLogitsLoss()
opt = optim.Adam(model.parameters(), lr = 0.001)




def train(epochs, model, loss_function, opt, train_loader, val_loader):
    accu_train_loss = []
    accu_val_loss = []
    accu_val_accuracy = []
    accu_train_accuracy = []
    accu_iteration = []
    accu_train_precision = []
    accu_val_precision = []
    all_pred = []
    all_y = []
    for i in range(epochs):
        accuracy = 0
        precision = 0
        model.train()
        for data in train_loader:
            X , y =  data
            pred = model(X)

            opt.zero_grad()
            batch_loss = loss_function(pred, y)
            batch_loss.backward()
            opt.step()

            pred = torch.round(torch.sigmoid(pred)).cpu().detach().numpy()
            y = y.cpu().detach().numpy()
            accuracy += accuracy_score( y,pred)
            precision += precision_score(y,pred)

        accuracy = accuracy / len(train_loader)
        precision = precision / len(train_loader)

        if i % 10 == 0 :
            accu_train_accuracy.append(accuracy)
            accu_train_loss.append(batch_loss.item())
            accu_iteration.append(i)
            accu_train_precision.append(precision)


        accuracy = 0
        precision = 0
        model.eval()
        with torch.no_grad():
            for data in val_loader:
                X , y = data
                pred = model(X)

                val_batch_loss = loss_function(pred, y)
                pred = torch.round(torch.sigmoid(pred)).cpu().detach().numpy()

                y = y.cpu().detach().numpy()
                all_pred.extend(pred)
                all_y.extend(y)
                accuracy += accuracy_score(y,pred)
                precision += precision_score(y,pred)


            precision = precision / len(val_loader)
            accuracy = accuracy / len(val_loader)

            if i % 10 == 0 :
                accu_val_accuracy.append(accuracy)
                accu_val_loss.append(val_batch_loss.item())
                accu_val_precision.append(precision)

    return accu_train_loss, accu_val_loss, accu_train_accuracy, accu_val_accuracy, accu_train_precision, accu_val_precision, accu_iteration, model
