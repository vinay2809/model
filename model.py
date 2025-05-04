
import torch
import torch.nn as nn

class BusterNet(nn.Module):
    def __init__(self):
        super(BusterNet, self).__init__()
        # Define layers and architecture (simplified)
        self.conv1 = nn.Conv2d(3, 64, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(64 * 16 * 16, 10)  # Placeholder sizes

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(x.size(0), -1)
        x = self.fc1(x)
        return x
