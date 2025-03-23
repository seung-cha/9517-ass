# 9517 Assignment 

## Table of Contents
* [Getting Started (Tutors)](#getting-started-tutors)
    * [Requirements](#requirements)
* [Getting Started (Team)](#getting-started-team)

## Getting Started (Tutors)

### Requirements
Install packages listed in `requirements.txt`
```
pip install -r requirements.txt
```
Additionally, install `Pytorch`

## Getting Started (Team)

Clone the repository
```
git clone https://github.com/seung-cha/9517-ass.git
```
Create a virtual environment (optional)

### Conda
```bash
conda create -n 9517_ass python=3.12
conda activate 9517_ass
```

### Venv
```bash
python3 -m venv .venv
source ./.venv/bin/activate
```


Install the packages
```bash
pip install -r requirements.txt
```

### Update requirements.txt
If you have installed more packages, update the requirements file:
```bash
pip freeze > requirements.txt
```