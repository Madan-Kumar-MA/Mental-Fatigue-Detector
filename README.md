# Mental Fatigue Detector

This project is a machine learning-based application designed to detect mental fatigue using a trained model. It includes scripts for training the model, running predictions, and a simple app interface.

## Project Structure

- `app.py` - Main application file to run the fatigue detector app.
- `main.py` - Script to run the model and make predictions.
- `train_model.py` - Script to train the machine learning model.
- `fatigue_model.joblib` - Pre-trained model file.
- `requirements.txt` - List of required Python packages.
- `backup/` - Backup copies of main scripts and model.

## Getting Started

### Prerequisites
- Python 3.7+
- All required packages listed in `requirements.txt`

### Installation
1. Clone the repository or download the project files.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### Usage
- To run the app:
  ```bash
  python app.py
  ```
- To train the model:
  ```bash
  python train_model.py
  ```
- To make predictions:
  ```bash
  python main.py
  ```

## License
This project is for educational purposes.
