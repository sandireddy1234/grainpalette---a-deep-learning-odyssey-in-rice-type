import os
import shutil
import random

# Paths
original_dataset_dir = 'Rice_Image_Dataset'
base_dir = 'dataset'
train_dir = os.path.join(base_dir, 'Train')
val_dir = os.path.join(base_dir, 'Validation')

# Create folders
os.makedirs(train_dir, exist_ok=True)
os.makedirs(val_dir, exist_ok=True)

# Define split ratio
split_ratio = 0.8  # 80% train, 20% validation

# Get class folders (rice types)
classes = os.listdir(original_dataset_dir)

for cls in classes:
    cls_path = os.path.join(original_dataset_dir, cls)
    images = os.listdir(cls_path)
    random.shuffle(images)

    split_index = int(len(images) * split_ratio)
    train_images = images[:split_index]
    val_images = images[split_index:]

    # Create class folders in train and val dirs
    os.makedirs(os.path.join(train_dir, cls), exist_ok=True)
    os.makedirs(os.path.join(val_dir, cls), exist_ok=True)

    # Move images
    for img in train_images:
        shutil.copy(os.path.join(cls_path, img), os.path.join(train_dir, cls, img))

    for img in val_images:
        shutil.copy(os.path.join(cls_path, img), os.path.join(val_dir, cls, img))

print("Dataset split complete!")
