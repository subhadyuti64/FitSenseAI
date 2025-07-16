# 👕 FitSense – AI Outfit Classifier

**FitSense** is a lightweight AI-powered web application that classifies outfit images into three categories: **Casual**, **Elegant**, or **Sportswear**. It combines the power of a PyTorch-trained deep learning model, a FastAPI backend, and a Streamlit frontend to deliver real-time predictions with a simple interface.

---

## 🚀 Features

- 🎯 Classifies outfits into 3 categories: **Casual**, **Elegant**, or **Sports**
- ⚡ FastAPI backend for serving model predictions
- 🖥️ Streamlit frontend for user interaction and image uploads
- 🔁 Realtime image processing and response
- 🧠 Powered by a fine-tuned **ResNet18** model

---

## 🗂️ Project Structure

<pre> ```bash fitsense/ ├── backend/ │ ├── main.py │ ├── utils.py │ └── model.pth ├── frontend/ │ └── streamlit_app.py ├── requirements.txt └── README.md ``` </pre>

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fitsense.git
cd fitsense

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt

Step 1: Start the FastAPI Backend
uvicorn backend.main:app --reload
FastAPI server runs on http://localhost:8000

Predict endpoint: POST http://localhost:8000/predict

Step 2: Run the Streamlit Frontend
In a new terminal (while backend is running):
streamlit run frontend/streamlit_app.py
Opens in browser at http://localhost:8501
```

Upload an image to classify your outfit!
🧪 API Usage
📤 POST /predict
Input: Image file (JPEG/PNG)
Output: JSON with predicted label



✅ To-Do
 Add Grad-CAM explainability
 Add confidence scores for predictions
 Dockerize for production
 Batch upload and multi-image support

📄 License
This project is licensed under the MIT License.

👤 Author
Built with ❤️ by Subhadyuti Rath

