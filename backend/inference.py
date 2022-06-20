import os

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.transforms as transforms
from PIL import Image

# constant for classes
classes = (
    "T-shirt/top",
    "Trouser",
    "Pullover",
    "Dress",
    "Coat",
    "Sandal",
    "Shirt",
    "Sneaker",
    "Bag",
    "Ankle Boot",
)


class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 4 * 4, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 4 * 4)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


def load_model(experiment_name: str):
    PATH = os.path.join("./service/fashion_mnist_experiment", experiment_name, "model.pth")
    model = Net()
    model.load_state_dict(torch.load(PATH))
    return model


def load_image(image: str):
    """
    image_path (str): path to image
    """
    image = image
    image_path = os.path.join("./data", image)
    image = Image.open(image_path)
    return image


def inference(experiment_name: str, image):
    """
    experiment_name (str): name of experiment (refer to csv column -> Experiment Name)
    image (PIL.Image)
    """
    model = load_model(experiment_name)
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])
    image = load_image(image)
    x = transform(image)[0].unsqueeze(0).unsqueeze(0)
    pred = model(x)
    idx = torch.argmax(pred).cpu().detach().numpy()
    return classes[idx]
