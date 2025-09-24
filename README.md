# ❤️ CardioCheck AI: Heart Disease Prediction App
---
An intelligent web application that leverages machine learning to predict the risk of heart disease based on key health indicators.
---

## 📋 Table of Contents
- [About The Project](#about-the-project)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

---


## 📖 About The Project

This project is a comprehensive machine learning pipeline designed to predict heart disease. It utilizes the well-known Cleveland Heart Disease dataset from the UCI Machine Learning Repository. The entire workflow, from data preprocessing and feature engineering to model training and hyperparameter tuning, is implemented. The final, optimized model is deployed as an interactive web application using Streamlit.

The primary goal is to provide a simple, user-friendly interface where users can input their health data and receive a real-time risk assessment, helping to raise awareness about cardiovascular health.

---

## ✨ Key Features

- **Data Preprocessing & Cleaning**: Handles missing values, encodes categorical data, and scales features.
- **Feature Selection**: Uses Recursive Feature Elimination (RFE) to identify the most impactful predictors.
- **Model Training**: Implements and evaluates multiple classification models, including Logistic Regression, Random Forest, and SVM.
- **Hyperparameter Tuning**: Optimizes the best-performing model (Random Forest) using `RandomizedSearchCV`.
- **Interactive UI**: A user-friendly web interface built with Streamlit for real-time predictions.

---

## 🛠️ Tech Stack

- **Backend & Modeling**: Python
- **Libraries**:
    - Scikit-learn (for machine learning models and preprocessing)
    - Pandas (for data manipulation)
    - NumPy (for numerical operations)
- **Web Framework**: Streamlit (for the interactive UI)

---

## 📂 Project Structure

```

Heart-Disease-Predictor/
├── README.md             \# Project documentation (this file)
├── app.py                \# The Streamlit application script
├── final\_model.pkl       \# The serialized trained model and scaler
└── requirements.txt      \# Python dependencies

````

---

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites
- Python 3.9 or higher
- Git for version control

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YourUsername/Heart-Disease-Predictor.git](https://github.com/YourUsername/Heart-Disease-Predictor.git)
    cd Heart-Disease-Predictor
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .\.venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

---

## 🏃 Usage

To launch the application, run the following command from the project's root directory:

```bash
streamlit run app.py
````

Your web browser will automatically open to the application's interface. Enter the required health metrics in the sidebar and click the "Predict" button to see the result.

-----

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

-----

## 👤 Contact

[Yousseif] - [yousseifmustafa2296@gmail.com]



Project Link: [https://github.com/yousseifmustafa/Heart-Disease-Predictor.git](https://www.google.com/search?q=https://github.com/YourUsername/Heart-Disease-Predictor)

