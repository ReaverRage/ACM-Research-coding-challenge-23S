
# ACM Challenge: Using Machine Learning to predict Star Type

This was my first time using Python for machine learning!

This project uses the dataset from https://www.kaggle.com/datasets/deepu1109/star-dataset. 

I used the Python machine learning tutorial at https://www.youtube.com/watch?v=7eh4d6sabA0.
## Accuracy

To evaluate the accuracy of the model, I trained and tested the model 30 times with a random split of the data: 80% for training and 20% for testing.

The average proportion of correct predictions was **99.722%**. Considering that I didn't touch any parameters on the model, it's extremely accurate.
## Visualization

![decision tree](https://github.com/ReaverRage/ACM-Research-coding-challenge-23S/blob/main/visualization.png?raw=true)

The star type, denoted as integers, are translated as the following:
- Brown Dwarf -> Star Type = 0
- Red Dwarf -> Star Type = 1
- White Dwarf -> Star Type = 2
- Main Sequence -> Star Type = 3
- Supergiant -> Star Type = 4
- Hypergiant -> Star Type = 5
## Run in Colab

Go to [ML_stars.ipynb](https://github.com/ReaverRage/ACM-Research-coding-challenge-23S/blob/main/ML_stars.ipynb)
## Run Locally

To run my project, you'll need the packages **pandas** and **scikit-learn**.

Clone the project

```bash
  git clone https://github.com/ReaverRage/ACM-Research-coding-challenge-23S
```

Run main.py with Python 3.10
