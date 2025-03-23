import os
import random
import numpy as np
from torch.utils.data import Dataset
from PIL import Image
from sklearn.model_selection import train_test_split

class SkyviewDataset(Dataset):
    """
    Skyview Multi-Landscape Aerial Imagery Dataset loader
    """
    def __init__(self, root_dir='data', categories=None, transform=None, split='train', train_ratio=0.8, seed=42):
        """
        Args:
            root_dir (string): Directory with all the category folders.
            categories (list): List of categories to include. If None, all categories are included
            transform (callable, optional): Optional transform to be applied on an image
            split (string): 'train' or 'test'
            train_ratio (float): Ratio of images to use for training (0.0-1.0)
            seed (int): Random seed for reproducibility
        """
        self.root_dir = root_dir
        self.transform = transform
        self.split = split
        
        # Set random seed for reproducibility
        random.seed(seed)
        np.random.seed(seed)
        
        # Available categories in the dataset
        all_categories = [
            'Agriculture', 'Airport', 'Beach', 'City', 'Desert',
            'Forest', 'Grassland', 'Highway', 'Lake', 'Mountain',
            'Parking', 'Port', 'Railway', 'Residential', 'River'
        ]
        
        # Use specified categories or all available ones
        self.categories = categories if categories is not None else all_categories
        
        # Collect all image paths and their labels
        self.images = []
        self.labels = []
        self.label_to_idx = {cat: idx for idx, cat in enumerate(self.categories)}
        
        for cat in self.categories:
            cat_dir = os.path.join(self.root_dir, cat)
            if not os.path.exists(cat_dir):
                print(f"Warning: Category directory {cat_dir} not found.")
                continue
                
            image_files = [f for f in os.listdir(cat_dir) 
                         if os.path.isfile(os.path.join(cat_dir, f)) and 
                         f.lower().endswith(('.png', '.jpg', '.jpeg'))]
            
            # Perform train/test split for this category
            train_files, test_files = train_test_split(
                image_files, train_size=train_ratio, random_state=seed
            )
            
            # Select the appropriate files based on split
            selected_files = train_files if split == 'train' else test_files
            
            for img_file in selected_files:
                img_path = os.path.join(cat_dir, img_file)
                self.images.append(img_path)
                self.labels.append(self.label_to_idx[cat])
    
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        img_path = self.images[idx]
        image = Image.open(img_path).convert('RGB')
        label = self.labels[idx]
        
        if self.transform:
            image = self.transform(image)
            
        return image, label