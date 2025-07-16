import torch
from torchvision import transforms
from PIL import Image
from torchvision.models import resnet18
import torch.nn as nn

class_names = ['casuals', 'elegante', 'sports']

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

def load_model(path="backend/fitsense.pth"):
    model = resnet18(pretrained=False)
    model.fc = nn.Linear(model.fc.in_features, 3)
    model.load_state_dict(torch.load(path, map_location='cpu'))
    model.eval()
    return model

def predict_image(image: Image.Image, model):
    img = transform(image).unsqueeze(0)
    with torch.no_grad():
        outputs = model(img)
        _, predicted = torch.max(outputs, 1)
    return class_names[predicted.item()]
