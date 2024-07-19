# What is Classification in Machine Learning?

## Supervised and Unsupervised learning

Machine Learning is made up of **supervised** and **unsupervised** learning.

- Supervised learning means that we will have labeled historical data that we will use to inform our **model**. The thing we are trying to predict is called **target**.
- In unsupervised learning there is no target, we are just trying to find patterns in the data.

> Note: A model is a program that can find patterns or make decisions from a previously unseen dataset

## Classification and Regression

Within supervised learning, there are two main types of problems: **classification** and **regression**.

- **Classification** is a type of supervised learning where the target is a category. For example, we might want to predict whether an email is spam or not spam _(e.g. true or false)_.

- **Regression** is a type of supervised learning where the target is a continuous value _(e.g. a number)_. For example, we might want to predict the price of a house.

## Target and Feature

- **Target** is the thing we are trying to predict. It is also called the dependent variable. In a pandas DataFrame, it is usually the column we are trying to predict
- **Feature** is the data we are using to make the prediction. It is also called the independent variable. In a pandas DataFrame, it is usually the columns we are using to predict the target.

> Note: Features are also called predictors
