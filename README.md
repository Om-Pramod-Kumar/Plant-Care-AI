PlantCare AI: Advanced Plant Disease Detection Using Transfer Learning

Live Demo: https://omkumar04-plant-care-ai.hf.space

PlantCare AI aims to develop an accurate and efficient model for classifying plant diseases by employing transfer learning techniques. Utilizing the New Plant Diseases Dataset containing over 87,000 annotated plant leaf images categorized into 38 distinct classes including various diseases affecting crops like Apple, Corn, Grape, Potato, Tomato, and others, the project leverages the pre-trained MobileNetV2 convolutional neural network (CNN) to expedite training and improve classification accuracy. Transfer learning allows the model to benefit from pre-existing knowledge of image features, significantly enhancing its performance and reducing computational costs. This approach provides a reliable and scalable tool for farmers, agricultural professionals, and gardeners, ensuring precise and efficient plant disease identification.


🚀 Overview

The user interacts with the web interface following this flow:

User Interface Interaction: User accesses the web application and navigates to the upload page

Image Selection: User selects or captures an image of a plant leaf

Image Processing: The uploaded image is preprocessed and resized to match model requirements

Model Prediction: The integrated MobileNetV2 model analyzes the image

Result Display: Prediction results with disease classification and recommendations are displayed.

🚀 Transfer Learning
Transfer learning is a machine learning technique where a model developed for one task is reused as the starting point for a model on a second task. It's a popular approach in deep learning where pre-trained models are used as the starting point on computer vision and natural language processing tasks.
🚀 MobileNetV2 is specifically designed for mobile and embedded vision applications.It features:

● Efficient Architecture: Uses depthwise separable convolutions

● Inverted Residuals: Linear bottleneck layers

● Lightweight: Fewer parameters compared to other architectures

● High Accuracy: Maintains competitive accuracy despite smaller size

● Pre-trained Weights: Trained on ImageNet with 1000 classes.


🚀 Architecture Explanation:

Input Layer: Accepts 224x224x3 RGB images

MobileNetV2 Base: Pre-trained feature extractor (partially frozen)

GlobalAveragePooling2D: Reduces spatial dimensions to 1D

Dropout (0.35): Regularization to prevent overfitting

Dense (256): Fully connected layer with ReLU activation

Dropout (0.25): Additional regularization

Output Dense (38): Final classification layer with softmax
