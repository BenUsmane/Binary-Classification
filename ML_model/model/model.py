from torch import nn
class MyModel (nn.Module):
  def __init__(self):
    super().__init__()

    self.layer1 = nn.Linear(30, 20)
    self.layer2 = nn.Linear(20,10)
    self.layer3 = nn.Linear(10,1)
    self.relu = nn.ReLU()

  def forward(self, x):
    x = self.relu(self.layer1(x))
    x = self.relu(self.layer2(x))
    z = self.layer3(x)
    return z