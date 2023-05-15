# 3M-CLIP
Multilingual Multimodal Pre-training Model for Medical.
## Download Datasets
1.download the mimic-cxr-jpg
```bash
wget -r -N -c -np --user vickyuan --ask-password --no-check-certificate https://physionet.org/files/mimic-cxr-jpg/2.0.0/

# password:liqiyuan1107
```
2.download the chexpert（11G）
```bash
https://us13.mailchimp.com/mctx/clicks?url=http%3A%2F%2Fdownload.cs.stanford.edu%2Fdeep%2FCheXpert-v1.0-small.zip&h=487bf3848ef9d950db525691805d077a085d3543b4562bef44f44e409d658d3c&v=1&xid=8a7c3d70af&uid=55365305&pool=contact_facing&subject=CheXpert-v1.0%3A+Subscription+Confirmed
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

