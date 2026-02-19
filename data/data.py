from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import torch
from torch.utils.data import TensorDataset, DataLoader

device = "cuda" if torch.cuda.is_available() else "cpu"
feature_name = load_breast_cancer().feature_names
load_breast_cancer().target_names
data = load_breast_cancer().data
target = load_breast_cancer().target
X, y = load_breast_cancer(return_X_y=True)
scale = StandardScaler()

X_tensor = torch.from_numpy(X).type(torch.float32)
y_tensor = torch.from_numpy(y).type(torch.float32).to(device)

y_tensor = y_tensor.reshape(-1, 1)

X_train, X_val, y_train, y_val = train_test_split(
    X_tensor, y_tensor, test_size=0.4, random_state=42
)
X_val, X_test, y_val, y_test = train_test_split(
    X_val, y_val, test_size=0.5, random_state=42
)


X_train = torch.from_numpy(scale.fit_transform(X_train)).type(torch.float32).to(device)
X_test = torch.from_numpy(scale.transform(X_test)).type(torch.float32).to(device)
X_val = torch.from_numpy(scale.transform(X_val)).type(torch.float32).to(device)

train_data = TensorDataset(X_train, y_train)
val_data = TensorDataset(X_val, y_val)
test_data = TensorDataset(X_test, y_test)

val_loader = DataLoader(val_data, batch_size=8, shuffle=True)
train_loader = DataLoader(train_data, batch_size=8, shuffle=True)
test_loader = DataLoader(test_data, batch_size=8, shuffle=True)
