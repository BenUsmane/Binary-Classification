import torch

def accuracy (y_train, y_pred ):
    correct = torch.eq(y_train, y_pred).sum().item()
    acc = (correct / len(y_train)) * 100
    return  acc