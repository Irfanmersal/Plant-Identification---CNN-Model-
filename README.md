# Plant Identification - CNN Model

This project aims to classify leaves by leveraging both traditional handcrafted features and features extracted from pre-trained deep CNNs. The input to the system is raw leaf images from a dataset, and the output is a predicted label for each species. By the end of this project, the system will be able to identify plant species based on a user-provided leaf image.

## How to Run the Application

1. **Install all the required dependencies**:
   Ensure you have all the necessary Python libraries installed. You can install them using the following command:
   ```
   pip install -r requirements.txt
   ```

2. **Create a Python environment**:
   Set up a virtual environment to run the Python files.
   ```
   python -m venv env
   source env/bin/activate   # For Linux/macOS
   env\Scripts\activate      # For Windows
   ```

3. **Run the application**:
   Open your terminal and run the Streamlit app by typing:
   ```
   streamlit run app.py
   ```

4. **Upload images**:
   Upload only the images provided in the dataset (trained dataset from Kaggle). The model is trained on these specific images for accurate classification.

## Dataset

You can find the dataset used for training the model here:  
[Plant Leaves for Image Classification Dataset](https://www.kaggle.com/datasets/csafrit2/plant-leaves-for-image-classification)

---
