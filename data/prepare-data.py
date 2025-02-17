from os import getenv
from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from tqdm import tqdm
from dotenv import load_dotenv

load_dotenv()
ds = load_dataset(getenv('HF_DATASET'), split='train')

blip_processor = BlipProcessor.from_pretrained('Salesforce/blip-image-captioning-large')
blip_model = BlipForConditionalGeneration.from_pretrained('Salesforce/blip-image-captioning-large')
clip_model = SentenceTransformer('clip-ViT-B-32')
minilm_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def blip_process(image: Image.Image):
    inputs = blip_processor(image, return_tensors='pt')
    out = blip_model.generate(**inputs)
    return blip_processor.decode(out[0], skip_special_tokens=True)

image_descriptions = []
image_description_vectors = []
image_vectors = []
for image in tqdm(ds['image']):
    image_description = blip_process(image)
    image_descriptions.append(image_description)
    image_description_vectors.append(minilm_model.encode(image_description).tolist())
    image_vectors.append(clip_model.encode(image_description).tolist())

ds = ds.add_column('description_blip', image_descriptions)
ds = ds.add_column('description_vector', image_description_vectors)
ds = ds.add_column('image_vector', image_vectors)
ds = ds.remove_columns('image')

ds.to_json('tshirts.json')


