from medclip import MedCLIPModel, MedCLIPVisionModelViT
from medclip import MedCLIPProcessor
from PIL import Image

# prepare for the demo image and texts
processor = MedCLIPProcessor()
image = Image.open('../example_data/view1_frontal.jpg')
inputs = processor(
    text=["lungs remain severely hyperinflated with upper lobe emphysema",
        "opacity left costophrenic angle is new since prior exam ___ represent some loculated fluid cavitation unlikely"],
    images=image,
    return_tensors="pt",
    padding=True
    )

# pass to MedCLIP model
model = MedCLIPModel(vision_cls=MedCLIPVisionModelViT)
model.from_pretrained()
# model.cuda()
outputs = model(**inputs)
print(outputs.keys())
print(outputs)
# dict_keys(['img_embeds', 'text_embeds', 'logits', 'loss_value', 'logits_per_text'])