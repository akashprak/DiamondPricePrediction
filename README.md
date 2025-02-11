## End to End ML project
## Diamond Price Prediction

### environment created
```
conda create -p venv python==3.10

conda activate venv/
```

### Installed required libraries
```
pip install -r requirements.txt
```

### Training model
```
python src/training_pipeline.py
```

### Running flask app
```
python app.py
```

### Docker Setup In EC2 commands to be Executed

sudo apt-get update -y

sudo apt-get upgrade

#### required
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
