# 🏠 Nigeria House Price Prediction

Welcome to a machine learning project that predicts house prices across Nigeria based on detailed housing features and location data. Built with real-world listings and trained using powerful models, this project is aimed at helping developers, analysts, and real estate enthusiasts understand pricing dynamics in Nigeria's housing market.

---

## 📊 Project Highlights

- ✅ **Over 24,000 real listings** analyzed
- 🧠 **XGBoost Regressor** for accurate price prediction
- 💡 Custom features like room-to-parking ratios
- 📈 R² Score of **0.71 on unseen data**
- 🌐 Deployed via **Streamlit** for real-time price estimation

---

## 📁 Dataset Overview

Each record includes:

- **Numerical**: `bedrooms`, `bathrooms`, `toilets`, `parking_space`, `price`
- **Categorical**: `title` (e.g. Duplex, Flats), `town`, `state`

Additional engineered features:

- `bed_bath_ratio`, `bath_toilet_ratio`
- `room_total`, `parking_per_room`

---

## 🧠 Model

We're using **XGBoost Regressor** with the following hyperparameters:

```python
XGBRegressor(
    objective='reg:squarederror',
    n_estimators=100,
    learning_rate=0.1,
    max_depth=6,
    random_state=42
)
```

Trained on a log-transformed price (`log_price`) for better prediction stability.

---

## 📈 Evaluation Metrics

| Metric       | Score    |
|--------------|----------|
| MAE          | 0.389    |
| RMSE         | 0.586    |
| R² Score     | 0.709 on test data |

---

## ⚙️ How to Use

### 1. Clone the repository:

```bash
git clone https://github.com/your-username/nigeria-house-price-prediction.git
cd nigeria-house-price-prediction
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit App

You can interact with the model using a simple web interface.

### Please Note that application of Streamlit here is only for example usage

The app interface is already implemented in [`app.py`](./app.py). To launch it:

```bash
streamlit run app.py
```

You’ll be prompted to enter the number of bedrooms, location, house type, etc., and get an instant price prediction.

---

## 📂 Project Structure

```
nigeria-house-price-prediction/
│
├── app.py                 # Streamlit app
├── model.pkl              # Trained XGBoost model
├── nigeria_houses_data.csv
├── requirements.txt       # Dependencies
├── README.md              # This file
```

---

## 🙌 Contribute

Want to help improve the model, enhance the app, or add new features? Contributions are welcome!

### Ideas:
- Add new features (e.g., land size, year built)
- Improve model performance
- Integrate location map or visuals
- Deploy on Streamlit Cloud or Hugging Face Spaces

Fork the repo, open a PR, or just drop a message!

---

## 👤 Author

**ANDREW JOSHUA ADOLE**  
📫 joshuaandrew159@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/joshua-andrew-827018306)
🔗 [GitHub](https://github.com/jobonano)
---

## 📜 License

This project is licensed under the **MIT License** — feel free to use, modify, and share!
