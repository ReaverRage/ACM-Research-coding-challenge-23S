
# ACM Challenge: Using Machine Learning to predict Star Type

This was my first time using Python for machine learning!

This project uses the dataset from https://www.kaggle.com/datasets/deepu1109/star-dataset. 

I used the Python machine learning tutorial at https://www.youtube.com/watch?v=7eh4d6sabA0.
## Accuracy

To evaluate the accuracy of the model, I trained and tested the model 30 times with a random split of the data: 80% for training and 20% for testing.

The average proportion of correct predictions was **99.722%**. At 95% confidence, the Wilson score interval with continuity correction is **[0.8543 , 0.998]**. The true accuracy of the model is likely within this interval.

Considering that I didn't touch any parameters on the model, it's extremely accurate.
## Run Locally

To run my project, you'll need the packages **pandas** and **scikit-learn**.

Clone the project

```bash
  git clone https://github.com/ReaverRage/ACM-Research-coding-challenge-23S
```

Run main.py with Python 3.10