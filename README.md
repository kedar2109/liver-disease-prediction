# Liver Disease Prediction

A full-stack machine learning project that predicts the likelihood of liver disease based on clinical and lifestyle inputs. This solution combines data preprocessing, model training using XGBoost, interpretability with SHAP, and deployment via FastAPI with a custom frontend.

---

## 📁 Dataset

The dataset includes 1,700 patient records with the following features:

| Feature            | Description                       |
| ------------------ | --------------------------------- |
| Age                | Patient age (20 to 80)            |
| Gender             | 0 = Male, 1 = Female              |
| BMI                | Body Mass Index (15 to 40)        |
| AlcoholConsumption | Units per week (0 to 20)          |
| Smoking            | 0 = No, 1 = Yes                   |
| GeneticRisk        | 0 = Low, 1 = Medium, 2 = High     |
| PhysicalActivity   | Hours per week (0 to 10)          |
| Diabetes           | 0 = No, 1 = Yes                   |
| Hypertension       | 0 = No, 1 = Yes                   |
| LiverFunctionTest  | Lab result (20 to 100)            |
| Diagnosis          | 0 = No liver disease, 1 = Disease |

The target variable is `Diagnosis`, a binary classification label.

---

## 📊 Exploratory Data Analysis (EDA)

* Analyzed class balance (slightly imbalanced)
* Used boxplots and histograms to understand distribution and potential outliers
* Checked correlations between features
* Visualized categorical features using count plots
* Performed statistical tests (Chi-square) for categorical relevance

---

## 🧹 Data Preprocessing

* Confirmed no missing/null values
* Removed or managed minor outliers
* All inputs passed through a validation schema (Pydantic)

---

## 🤖 Model Implementation

* **Model used**: XGBoost Classifier
* **Feature importance** shown using built-in and SHAP methods
* **Hyperparameter tuning**: Performed using GridSearchCV and RandomizedSearchCV
* **Evaluation**: 5-fold cross-validation

### Final Results:

* Accuracy: \~90.8%
* ROC-AUC: 0.9591
* F1 Score: 0.9141
* Precision: 0.9483
* Recall: 0.8824
* SHAP analysis confirms interpretability

---

## 🌐 Deployment

* **Backend**: FastAPI
* **Frontend**: HTML, CSS, JavaScript
* **Prediction UI**: User enters 10 features, model returns result in real time
* **Model Loading**: Pipeline saved using `pickle` and served in `/predict` endpoint

---

## 🧠 Model Interpretation

* **SHAP summary plots** show top features:

  * Liver Function Test
  * Genetic Risk
  * Alcohol Consumption
* **Waterfall plot** explains prediction for an individual patient

---

## 🖥️ How to Use

1. Clone the repo:

   ```bash
   git clone https://github.com/kedar2109/liver-disease-prediction
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   uvicorn app:app --reload
   ```

4. Visit `http://127.0.0.1:8000` to access the form
5. Fill patient data and submit to get real-time prediction

---

## 📦 Tech Stack

* Python
* XGBoost
* FastAPI
* SHAP
* HTML/CSS/JS
* Uvicorn

---

## 📂 Project Structure

```
├── app.py              # FastAPI backend
├── main.ipynb          # model training   
├── liver_disease_model.pkl  # Saved ML pipeline
├── templates/
│   └── index.html      # Frontend form
├── static/
│   ├── style.css       # Stylesheet
│   └── script.js       # Form logic
├── README.md           # Documentation
├── requirements.txt    # Requrements 
```

---