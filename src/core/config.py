from pydantic import BaseModel

class DatasetConfig(BaseModel):
    dir_base: str = "/home/adriano/Documents/datasets/dataset_files"
    image_file: str = "images.npy"
    label_file: str = "labels.npy"
    image_size: int = 300

class HyperParameters(BaseModel):
    author: str = "Adriano A. Santos"
    file_name: str = "PSPNet"
    dir_base: str = "/home/adriano/Documents/tutoriais/PSPNet-for-Self-driving-car/weights/"
    weights_path: str = "/home/adriano/Documents/tutoriais/PSPNet-for-Self-driving-car/weights/bestPSPNet.pt"
    n_epochs: int = 100
    max_lr: float = 3e-4
    n_classes: int = 3
    batch_size: int = 4
