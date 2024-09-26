# Fine-Tuned GPT-2 on H-1B Visa Data

This repository contains a fine-tuned **GPT-2** model focused on **H-1B visa application data**, designed to generate context-specific responses related to visa processes, trends, and insights. The model was fine-tuned using the **Hugging Face Transformers** library and deployed via a **Flask web application** for real-time user interaction.

<img width="744" alt="Screenshot 2024-09-26 at 4 48 56 AM" src="https://github.com/user-attachments/assets/5d0d56c4-eaf5-42ba-aa59-6fbb11972ce8">



## Key Features
- **Fine-Tuned GPT-2 Model**: This project demonstrates the fine-tuning of **GPT-2**, an open source **Large Language Models (LLMs)**, on specific data related to H-1B visa applications.
- **Custom Dataset Processing**: Preprocessing of real-world H-1B data, including data cleaning.
- **Real-Time Deployment with Flask**: The model is deployed using a **Flask** backend, allowing users to query the model in real-time.
- **Controlled Text Generation**: Implemented settings for text generation, including **top-k sampling**, **nucleus sampling (top-p)**, **temperature scaling**, and **repetition penalty**.
- **Interactive Interface**: Users can interact with the model through a user-friendly interface.
- **Model Training and Optimization**: Utilized **PyTorch** and **Hugging Face** frameworks for model training, with techniques such as **gradient accumulation** and loss minimization to optimize performance.

## Project Workflow

1. **Data Collection & Preprocessing**:
   - H-1B visa data was sourced from Kaggle.
   - The dataset was cleaned, and essential fields such as **case status**, **employer name**, **prevailing wage**, and **visa class** were extracted.
   - Data was transformed into a format suitable for language model training, generating over 150,000 structured sentences.

2. **Fine-Tuning the GPT-2 Model**:
   - The GPT-2 model was fine-tuned on H-1B visa sentences using **transfer learning**.
   - Training was conducted using **PyTorch**, with techniques like **learning rate scheduling** and **AdamW optimizer**.
   - Model checkpoints and final versions were saved for deployment.

3. **Deployment with Flask**:
   - A Flask web application was built to display the fine-tuned model.
   - The model is queried in real-time.
   - The application is structured for scalability and deployment to cloud services such as **AWS** or **Google Cloud**.

## Getting Started

### Prerequisites

Ensure that you have the following packages installed:

```bash
pip install transformers datasets torch flask
```

### Data Setup

- Place the cleaned H-1B visa dataset (`Cleaned_H1B_Visa_Data.xlsx`) in the root directory.
- Generate the training sentences using the `HB-1TrainingNotebook.ipynb`.

### Model Training

1. **Train the model** by running the following notebook:
   - `HB-1TrainingNotebook.ipynb`

2. **Save the fine-tuned model**:
   - Once the model has been fine-tuned, it will be saved in the `./fine_tuned_gpt2/` directory.

### Running the Flask App

Start the Flask web application to query the model in real-time:

```bash
python main.py
```

Navigate to `http://localhost:5000` to interact with the model.



## Key Technologies

- **Transformers**: **Hugging Face Transformers** library for model fine-tuning and deployment.
- **PyTorch**: Used as the core framework for model training and optimization.
- **Flask**: Developed a lightweight web app for real-time interaction with the model.

## Data Source:
The data used for fine-tuning the GPT-2 model comes from the H-1B Visa Applications dataset. This dataset provides detailed information on H-1B visa applications spanning multiple years. You can access the dataset here: https://www.kaggle.com/datasets/nsharan/h-1b-visa

## Future Enhancements

- **Cloud Deployment**: Deploy the model to **AWS Lambda**, **Google Cloud**, or **Azure**
- **Expanded Dataset**: Fine-tune the model on a broader range of visa-related data
