# 🤖 AI Fake Job Detection System

An AI-powered web application that detects **fraudulent job postings** using Machine Learning (Logistic Regression + TF-IDF).

## 🚀 Live Demo
🔗[Click here to try it live](https://ai-based-fake-job-detection-system.onrender.com)

## 📌 Features
- Paste any job description and instantly detect if it's **Fake or Legitimate**
- Shows **confidence score** (how sure the AI is)
- Clean and responsive UI
- Powered by Machine Learning (Logistic Regression)

## 🛠️ Tech Stack
| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| ML Model | Scikit-learn (Logistic Regression) |
| Frontend | HTML, CSS, JavaScript |
| Deployment | Render |

## 📂 Project Structure
```
AI_FAKE_JOB/
├── app.py                  # Flask backend
├── fake_job_detection.py   # ML model training script
├── main.py                 # Dataset exploration
├── model.pkl               # Trained ML model
├── vectorizer.pkl          # TF-IDF Vectorizer
├── requirements.txt        # Python dependencies
├── templates/
│   └── index.html          # Frontend UI
└── static/
    ├── style.css           # Styling
    └── script.js           # Frontend logic
```

## ⚙️ Run Locally
```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```
Then open: http://127.0.0.1:5000

## 🧠 How It Works
1. User pastes a job description
2. Text is converted to numerical features using **TF-IDF**
3. **Logistic Regression** model predicts if it's Fake or Real
4. Result + Confidence score is displayed instantly

## 👨‍💻 Author
Kodidasu Veera Venkata Nagavalli

## 📄 License
MIT License
