from flask import Flask, request, jsonify, render_template
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

app = Flask(__name__, template_folder='templates')

# Load GPT-2 model using the absolute path
model = GPT2LMHeadModel.from_pretrained('/Users/audrey/H-1B Insights AI/fine_tuned_gpt2')
tokenizer = GPT2Tokenizer.from_pretrained('/Users/audrey/H-1B Insights AI/fine_tuned_gpt2')
model.eval()  # Set the model to evaluation mode

device = 'cuda' if torch.cuda.is_available() else 'cpu'
model.to(device)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask_gpt():
    data = request.json
    question = data.get('question')

    if question:
        # Tokenize input
        inputs = tokenizer(question, return_tensors='pt', padding=True, truncation=True, max_length=512).to(device)

        # Generate response from the model
        outputs = model.generate(inputs['input_ids'], max_length=150, num_return_sequences=1, pad_token_id=tokenizer.eos_token_id)

        # Decode the generated response
        answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return jsonify({"response": answer})  # Return the response as JSON

    return jsonify({"error": "No question provided."}), 400

if __name__ == "__main__":
    app.run(debug=True)
