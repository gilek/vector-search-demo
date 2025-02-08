from os import getenv
from datasets import load_dataset
from dotenv import load_dotenv

load_dotenv()
ds = load_dataset(getenv('HF_DATASET'), split='train')

for index, image in enumerate(ds['image']):
    id = str(ds[index]['id'])
    image.save(f'../ui/dist/images/{id}.jpg')