import torch
import numpy
from torch.utils.data import DataLoader, Dataset, TensorDataset
from sklearn.datasets import load_breast_cancer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from torch import nn, optim

from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, confusion_matrix
from seaborn import heatmap


from model.model import MyModel
from model.train import train


if __name__ == "__main__":
    