# This file is just for prediction_page.py
import sys
import subprocess
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'streamlit==0.84.0'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pickle-mixin'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn==0.24.2'])
subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'nltk'])
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

