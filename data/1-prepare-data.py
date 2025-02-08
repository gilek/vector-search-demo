from sentence_transformers import SentenceTransformer
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import pandas as pd
from tqdm import tqdm

blip_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
blip_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
clip_model = SentenceTransformer('clip-ViT-B-32')
minilm_model = SentenceTransformer('sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2')

def blip_process(image: Image.Image):
    inputs = blip_processor(image.convert('RGB'), return_tensors="pt")
    out = blip_model.generate(**inputs)
    return blip_processor.decode(out[0], skip_special_tokens=True)

df = pd.read_csv('./thirts.csv')

image_descriptions = []
image_description_vectors = []
image_vectors = []
for image_id in tqdm(df['id']):
    image = Image.open(f'../ui/dist/images/{image_id}.jpg')
    image_description = blip_process(image)
    image_descriptions.append(image_description)
    image_description_vectors.append(minilm_model.encode(image_description).tolist())
    image_vectors.append(clip_model.encode(image_description).tolist())

df['description_blip'] = image_descriptions
df['description_vector'] = image_description_vectors
df['image_vector'] = image_vectors

df.to_json('./tshirts.json')
