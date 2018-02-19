# Notes

## How many features should I have and what should they be?

We will start off with a feature vector of size 5000 X 1, based off of a vocab list of 5000: the top 5000 most common words in our training set. Specifically, index i of the feature vector is 1 if vocab list word i is in the specific email, otherwise 0.

## Should I use feature scaling?

Feature scaling is not applicable. Feature scaling is used when features are order of magnitudes different. In this classification problem, our features only take on the values of 0 or 1.

## What value(s) should I initialize the parameters of the hypothesis to?

Doesn't matter. The cost function for logistic regression is convex, so we will always end up finding min(J) no matter what we initialize parameters to. However, I will initialize them to be all 0's, since I want to avoid the values of theta being too large or too small, as then the sigmoid will output a hypothesis value near 1 or 0, which will cause an error as log(0) is undefined.

## How should I split my dataset into the training set, cross validation set, and testing set?

Generally, the training set, cross validation set, and testing set make up 60%, 20%, and 20% of the overall dataset, respectively.

## What should be the value of our regularization constant?

We determine the most suitable value of the regularization constant by examining evidence of our model tuned using different values of the constant (to avoid premature optimization). We will select maybe 5-10 different values of lambda, and for each value, train a spam classifier. Then, we test each spam classifier on our cross validation set, and choose the model with the lowest model.

## Declaring convergence for gradient descent

Declare convergence if cost decreases by less than 1E-3 in one iteration of gradient descent