# Fine-Tuned GPT-2 on H-1B Visa Data



This repository contains a fine-tuned **GPT-2** model focused on **H-1B visa application data**, designed to generate coherent and context-specific responses related to visa processes, trends, and insights. The model was fine-tuned using the **Hugging Face Transformers** library and deployed via a **Flask web application** for real-time user interaction.


![Uploading Screenshot 2024-09-26 at 4.48.56 AM.png…]()



## Key Features
- **Fine-Tuned GPT-2 Model**: This project demonstrates the fine-tuning of **GPT-2**, one of the most widely used **Large Language Models (LLMs)**, on domain-specific data related to H-1B visa applications.
- **Custom Dataset Processing**: Extensive preprocessing of real-world H-1B data, including data cleaning, normalization, and transformation into structured sentences for efficient training.
- **Real-Time Deployment with Flask**: The model is deployed using a **Flask** backend, allowing users to query the fine-tuned GPT-2 model in real-time.
- **Controlled Text Generation**: Implemented advanced settings for text generation, including **top-k sampling**, **nucleus sampling (top-p)**, **temperature scaling**, and **repetition penalty** to ensure diverse, meaningful responses.
- **Interactive Interface**: Users can interact with the model through a user-friendly interface.
- **Model Training and Optimization**: Utilized **PyTorch** and **Hugging Face** frameworks for efficient model training, with techniques such as **gradient accumulation** and loss minimization to optimize performance.

## Project Workflow

1. **Data Collection & Preprocessing**:
   - H-1B visa data was sourced from publicly available datasets.
   - The dataset was cleaned, and essential fields such as **case status**, **employer name**, **prevailing wage**, and **visa class** were extracted.
   - Data was transformed into a format suitable for language model training, generating over 150,000 structured sentences.

2. **Fine-Tuning the GPT-2 Model**:
   - The GPT-2 model was fine-tuned on domain-specific H-1B visa sentences using **transfer learning**.
   - Training was conducted using **PyTorch**, with techniques like **learning rate scheduling** and **AdamW optimizer** for efficient convergence.
   - Model checkpoints and final versions were saved for deployment.

3. **Deployment with Flask**:
   - A Flask web application was built to serve the fine-tuned model.
   - The model is queried in real-time.
   - The application is structured for easy scalability and potential deployment to cloud services such as **AWS** or **Google Cloud**.

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

## Example Queries

- *"Can you tell me about the H-1B visa process?"*
- *"What are the trends in H-1B visa approvals over the last five years?"*
- *"What are the common job titles for H-1B visa holders?"*

## Key Technologies

- **Transformers**: Leveraged the **Hugging Face Transformers** library for model fine-tuning and deployment.
- **PyTorch**: Used as the core framework for model training and optimization.
- **Flask**: Developed a lightweight web app for real-time interaction with the fine-tuned GPT-2 model.
- **Git LFS**: Used for tracking large files like the fine-tuned model weights.
- **Data Preprocessing**: Performed advanced data cleaning and feature engineering for generating training data.

## Future Enhancements

- **Cloud Deployment**: Deploy the model to **AWS Lambda**, **Google Cloud**, or **Azure** for scalable real-time interaction.
- **Expanded Dataset**: Fine-tune the model on a broader range of visa-related data to enhance response diversity.
- **Enhanced Query Processing**: Implement NLP techniques for more sophisticated question understanding and response generation.
