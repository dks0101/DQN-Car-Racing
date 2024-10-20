import torch
import torch.nn as nn
import torch.nn.functional as F

class CNNActionValue(nn.Module):
    def __init__(self, state_dim, action_dim, activation=F.relu):
        super(CNNActionValue, self).__init__()
        self.conv1 = nn.Conv2d(state_dim, 16, kernel_size=6, stride=3)  # [N, 4, 84, 84] -> [N, 16, 27, 27]
        self.conv2 = nn.Conv2d(16, 32, kernel_size=3, stride=2)  # [N, 16, 27, 27] -> [N, 32, 13, 13]
        self.in_features = 32 * 13 * 13
        self.fc1 = nn.Linear(self.in_features, 256)
        self.fc2 = nn.Linear(256, action_dim)
        self.activation = activation

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = x.view((-1, self.in_features))
        x = self.fc1(x)
        x = self.fc2(x)
        return x
