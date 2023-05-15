# 3M-CLIP
Multilingual Multimodal Pre-training Model for Medical.
## Download Datasets
1.download the mimic-cxr-jpg
```bash
wget -r -N -c -np --user vickyuan --ask-password --no-check-certificate https://physionet.org/files/mimic-cxr-jpg/2.0.0/

# password:liqiyuan1107
```
1.download the chexpert
```bash
wget -r -N -c -np --user vickyuan --ask-password --no-check-certificate https://physionet.org/files/mimic-cxr-jpg/2.0.0/

# password:liqiyuan1107
```

## Download 3M-CLIP

Import Environment
```bash
conda env create -f environment.yml
```

Main installation package
```bash
python 3.8   cuda 10.2
pip install -r requirements.txt
```

```bash
git clone https://github.com/vicky-yuan/3M-CLIP.git
```

## Run
pre-training

```bash
cd examples
nohup python -u run_medclip_pretrain.py > nohup.out 2>&1 &
```
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
    --medclip
    --mimic-cxr-jpg
        --2.0.0
            --files
                --p10
```

