 🛡️ Network Security: Phishing Detection Pipeline  

A complete **end-to-end MLOps project** for detecting phishing URLs using machine learning and deploying the model through a **Dockerized FastAPI application**.  

This project demonstrates ETL pipelines, data validation, model training with MLflow tracking, and artifact management using AWS S3 — providing a real-world network security ML workflow.  

---

## 🚀 Key Features  

### 🧩 Data Engineering (ETL)
- Extracts, transforms, and loads phishing data from network sources.  
- Cleans, validates, and prepares data for model training.  

### 🧾 Data Validation  
- Ensures incoming data conforms to defined schemas (`data_schema/`).  

### 🧠 Model Training & Tracking  
- Uses **MLflow** for experiment tracking and model versioning.  
- Models and metrics are automatically logged and stored.  

### 🧱 Artifact Management  
- Trained models and ML artifacts are pushed to **AWS S3**.  

### ⚡ FastAPI Inference App  
- Serves predictions through a lightweight and scalable API.  

### 🐳 Dockerized Deployment  
- End-to-end reproducible environment using Docker.  

---

## 🧠 Tech Stack  

| Category | Tools / Frameworks |
|-----------|--------------------|
| **Programming** | Python 3.9+ |
| **Data Processing** | Pandas, NumPy |
| **ML & Tracking** | scikit-learn, MLflow |
| **Cloud Storage** | AWS S3 |
| **API Framework** | FastAPI |
| **Deployment** | Docker |
| **Database** | MongoDB |
| **Validation** | Pydantic, Cerberus |
| **Logging** | Python Logging, MLflow Tracking |

---

## 🗂️ Project Structure  

```bash
networksecurity/
├── app.py                  # FastAPI app for model serving
├── main.py                 # Main training and MLflow tracking script
├── push_data.py            # ETL pipeline for loading and validating data
├── test_mongodb.py         # Database connection test
├── Dockerfile              # Docker environment setup
├── requirements.txt        # Dependencies
├── setup.py                # Project setup file
├── mlflow.db               # Local MLflow tracking database
├── mlruns/                 # MLflow experiment tracking folder
├── final_model/            # Saved trained model
├── network_data/           # Raw and processed data
├── valid_data/             # Validated data
├── data_schema/            # Schema definitions for validation
├── prediction_output/      # Model predictions output
├── templates/              # Frontend or FastAPI templates
└── README.md               # Project documentation
🧩 Workflow Overview
1️⃣ Data Ingestion
Source data is pulled using push_data.py from phishing repositories or MongoDB.

Schema validation ensures only clean data proceeds to training.

2️⃣ Feature Engineering & Validation
Data is transformed and stored in valid_data/.

Schema and integrity checks are performed via data_schema/.

3️⃣ Model Training
Run main.py to train the model.

MLflow logs metrics, parameters, and artifacts to mlruns/.

Best model is exported to final_model/ and uploaded to S3.

4️⃣ Deployment (FastAPI + Docker)
FastAPI app (app.py) loads the latest model from S3 or local storage.

Build and run the Docker container for inference.

⚙️ Installation & Setup
1. Clone Repository
bash
Copy code
git clone https://github.com/westobaba/networksecurity-phishing.git
cd networksecurity-phishing
2. Create Virtual Environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Linux/Mac
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure AWS & MongoDB
Create a .env file or set environment variables:

bash
Copy code
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_BUCKET_NAME=your_bucket
MONGODB_URI=mongodb+srv://...
🐳 Docker Deployment
Build Docker Image
bash
Copy code
docker build -t phishing-detector .
Run Docker Container
bash
Copy code
docker run -p 8080:8080 phishing-detector
Visit the API at 👉 http://localhost:8080

📈 MLflow Tracking
Start MLflow UI to view experiment runs:

bash
Copy code
mlflow ui --backend-store-uri sqlite:///mlflow.db
Then open http://localhost:5000 to explore logged runs, metrics, and models.

🧪 Example Prediction
Request:

bash
Copy code
curl -X POST "http://localhost:8080/predict" \
     -H "Content-Type: application/json" \
     -d '{"url": "http://suspicious-example.com/login"}'
Response:

json
Copy code
{
  "url": "http://suspicious-example.com/login",
  "prediction": "Phishing",
  "confidence": 0.97
}
🧰 Key Folders Summary
Folder	Description
network_data/	Raw and processed input data
data_schema/	Data validation schemas
valid_data/	Cleaned, validated data used for training
final_model/	Trained ML model
prediction_output/	Model inference results
mlruns/	MLflow experiment tracking metadata

🔐 S3 Integration
Models and artifacts are automatically pushed to your AWS S3 bucket after training for secure storage and deployment use.

🧾 Future Improvements
Implement real-time phishing detection API

Integrate CI/CD pipeline with GitHub Actions

Add model monitoring and automatic retraining

Enhance feature extraction using NLP-based URL analysis

📄 License
This project is licensed under the MIT License — free to use and modify.

👤 Author
Kelvin Benjamin
Data Scientist & MLOps Enthusiast
