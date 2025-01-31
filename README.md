Overview
This project focuses on Visual Question Answering (VQA), which merges computer vision and natural language processing to answer questions based on images. The goal is to develop a model capable of interpreting images and answering textual questions related to them. We utilize the COCO dataset for validation and training and employ pre-trained models like VGG19 for feature extraction, combined with Recurrent Neural Networks (RNN) and Long Short-Term Memory (LSTM) networks for model training.


Project Phases
Step 1: Vocabulary Creation and Preprocessing
Objective: Preprocess and create vocabularies for questions and answers.
Methodology:
Parse JSON files to extract and clean questions and answers.
Tokenize and filter questions and answers, and create a vocabulary from frequent words.
Store the processed vocabularies for training and evaluation.

Step 2: Validation Image Feature Extraction
Objective: Extract features from validation images using the VGG19 model.
Implementation:
Download and preprocess validation images from the COCO dataset.
Use VGG19 to extract features from each image.
Store features as NumPy files for efficient loading during model training.

Step 3: Training Image Feature Extraction
Objective: Extract features from training images to be used for training the VQA model.
Implementation:
Download and preprocess training images.
Use VGG19 to extract image features.
Store these features in a structured format for use during model training.

Step 4: Modeling
Objective: Develop two deep learning models (RNN-based and LSTM-based) for VQA.
Implementation:
Process image features, questions, and answers for model training.
Experiment with RNN and LSTM architectures to process sequential data (questions) and image features.
Train both models and evaluate their performance using accuracy and loss metrics.

Key Technologies and Libraries:
TensorFlow: For model implementation and training.
VGG19: A pre-trained CNN for feature extraction from images.
NumPy: For handling large datasets and storing image features.
COCO Dataset: A large-scale dataset for image captioning and VQA tasks.
Python: The primary programming language for implementation.
Keras: For building and training deep learning models.

Challenges and Solutions
Handling Large Datasets: Managed the large volume of images using batch processing and efficient data handling with TensorFlow's tf.data.Dataset API.
Data Integrity: Carefully handled missing and unknown answers to maintain the integrity of the training process.

Results and Observations
The LSTM-based model outperformed the RNN-based model in terms of accuracy and stability during training.
Both models showed signs of overfitting, particularly the RNN, which struggled with longer sequences due to the vanishing gradient problem.
The models demonstrated promising results, with the LSTM model exhibiting better accuracy and generalizability.

Real-World Applications
Accessibility: Enhances accessibility for the visually impaired by providing verbal answers to visual questions.
Education: Facilitates interactive learning tools, allowing users to ask questions about educational images.
Customer Engagement: Enables intuitive product queries in retail, improving customer interaction with products.
