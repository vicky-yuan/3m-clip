# 3M-CLIP
Decoupled Contrastive Learning for Multilingual Multimodal Medical Pre-trained Model.

Qiyuan Li, Chen Qiu, Haijiang Liu, Jinguang Gu, Dan Luo

Multilingual multimodal pre-training in healthcare faces challenges related to language diversity, suboptimal multi-modal interactions, and an absence of coherent multilingual multimodal representations. In response to these challenges, we introduce a novel multilingual multimodal medical pre-training model. 
We employ a strategic augmentation of the medical corpus by expanding the MIMIC-CXR report dataset to 20 distinct languages using machine translation techniques. 
We develop a targeted label disambiguation technique to address the labeling noise within decoupled contrastive learning.
We present a refined multilingual multimodal medical pre-training model, significantly enhancing the understanding of medical multimodal data and adapting the model to multilingual medical contexts.


## Datasets
1. Download the MIMIC-CXR
```bash
https://physionet.org/content/mimic-cxr/2.1.0/
```
2. Download the CheXpert（11G）
```bash
https://stanfordmlgroup.github.io/competitions/chexpert/
```
3. Translate the multilingual reports
```bash
https://huggingface.co/facebook/nllb-200-distilled-600M
```

## Vision and Text Encoder
1. Vision encoder -- clip-vit-base-patch32
```bash
https://huggingface.co/openai/clip-vit-base-patch32
```
2. Text encoder -- xlm-roberta
```bash
https://github.com/facebookresearch/XLM
```
3. Med-XLM-Roberta

We obtain a medical multilingual text encoder based on XLM-R, trained with translated data.

## Download 3M-CLIP

Import Environment
```bash
conda env create -f environment.yml
```

Or Only import main installation package
```bash
python 3.8   cuda 10.2
pip install -r requirements.txt
```

```bash
git clone https://github.com/vicky-yuan/3m-clip.git
```

## Run
```bash
cd examples
nohup python -u run_medclip_pretrain.py > nohup.out 2>&1 &
```


