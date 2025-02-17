import sys
import os

from datasets import load_dataset


ds = load_dataset(os.getenv('HF_DATASET'), split='train')

path = (sys.argv[1] if len(sys.argv) > 1 else "/images").rstrip('/')
if os.path.exists(path) is False:
    os.makedirs(path)

for index, image in enumerate(ds['image']):
    id = str(ds[index]['id'])
    image.save(f'{path}/{id}.jpg')