# Network Security Phishing Detection Project  

This project focuses on detecting phishing attacks using machine learning techniques.  
It includes a complete ETL → Training → Deployment pipeline, with MLflow experiment tracking and Dockerized deployment for reproducibility.  

---

## 🚀 Key Features  

- **Data Pipeline:** Automated ETL and validation of network data  
- **Model Training:** Machine learning model trained and tracked via MLflow  
- **Deployment:** FastAPI-based API for model inference  
- **Cloud Integration:** Model artifacts and data stored in AWS S3  
- **Reproducibility:** Docker environment for consistent builds and deployments  
- **Database Integration:** MongoDB for data management  

---

## 🧰 Tech Stack  

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
├── app.py                # FastAPI app for model serving
├── main.py               # Model training and MLflow tracking script
├── push_data.py          # ETL pipeline for loading and validating data
├── test_mongodb.py       # MongoDB database connection test
├── Dockerfile            # Docker environment setup
├── requirements.txt      # Project dependencies
├── setup.py              # Project setup file
├── mlflow.db             # Local MLflow tracking database
├── mlruns/               # MLflow experiment tracking folder
├── final_model/          # Saved trained model
├── network_data/         # Raw and processed data
├── valid_data/           # Validated data
├── data_schema/          # Schema definitions for validation
├── prediction_output/    # Model predictions output
├── templates/            # Frontend or FastAPI templates
└── README.md             # Project documentation
🐳 Dockerized Deployment
You can run the entire application inside Docker for a consistent environment.

Build the Docker image
bash
Copy code
docker build -t networksecurity-app .
Run the container
bash
Copy code
docker run -p 8000:8000 networksecurity-app
Access the app at http://localhost:8000

📊 MLflow Tracking
All model training runs, metrics, and artifacts are logged in MLflow.
You can start the MLflow UI locally:

bash
Copy code
mlflow ui
Then open http://localhost:5000 in your browser to explore experiment results.

☁️ Cloud Storage
Model artifacts and data are automatically pushed to AWS S3 for backup and versioning.

🧩 Future Enhancements
Add real-time phishing detection API endpoints

Integrate advanced deep learning models

Enable CI/CD for automated retraining and deployment

🧑‍💻 Author
Kelvin Benjamin
Machine Learning Engineer | Data Scientist

📝 License
This project is open-source under the MIT License.
