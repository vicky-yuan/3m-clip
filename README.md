# 3M-CLIP
Multilingual Multimodal Pre-training Model for Medical.

## Tips
Path Details
```bash
MMMCLIP-main
    --CheXpert-v1.0-small
        --train
          --patientxxx
    --examples
    --example_data
    --local_data
        --chexpert-5x200-val-meta.csv
        --...
    --medclip
        --pretained
          --medclip-resnet
            --pytorch_model.bin
          --medclip-vit
            --pytorch_model.bin
    --mimic-cxr-jpg
        --2.0.0
            --files
                --p10
```

## Download Datasets
1.download the mimic-cxr-jpg
```bash
https://physionet.org/files/mimic-cxr-jpg/2.0.0/

```
2.download the chexpert（11G）
```bash
https://stanfordmlgroup.github.io/competitions/chexpert/
```

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
pre-training

```bash
cd examples
nohup python -u run_medclip_pretrain.py > nohup.out 2>&1 &
```
