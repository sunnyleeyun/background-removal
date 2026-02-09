# Backgroud Removal Pipeline

# Pipeline

Budget
↓
Requirement -> Planning -> Execution -> Deliverable -> Testing -> Deliverable Approved -> Maintence

# Requirements

Link

# Planning

IMG

# Execution

State of Art

## ⚙️ Operations & Setup

### 0. Connect to EC2

Before connecting, ensure your private key has the correct permissions:

```bash
# Secure the key file (read-only for the owner)
chmod 400 /path/to/your-key.pem

# Access the instance via SSH
ssh -i /path/to/your-key.pem ubuntu@<YOUR_EC2_PUBLIC_IP>
```

### 1. Server Preparation

```bash
sudo apt-get update
sudo apt install -y python3-pip nginx python3-virtualenv

sudo nano /etc/nginx/sites-enabled/fastapi_nginx
```

### 2. Nginx Configuration

Edit your site configuration: sudo nano /etc/nginx/sites-enabled/fastapi_nginx

```
server {
    listen 80;
    server_name <YOUR_EC2_IP>;
    location / {
        proxy_pass http://127.0.0.1:8000;
    }
}
```

Restart Nginx after saving: `sudo systemctl restart nginx`

### 3. Application Installation

```
git clone https://github.com/sunnyleeyun/background-removal.git
cd background-removal

sudo apt install python3-virtualenv
virtualenv venv --python=python3
source venv/bin/activate

pip install -r requirements.txt
```

### 4. Running the API

```
python3 -m uvicorn main:app
```
