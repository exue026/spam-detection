# Notes

## Should I use feature scaling?

Feature scaling is not applicable. Feature scaling is used when features are order of magnitudes different. In this classification problem, our features only take on the values of 0 or 1.

## What value(s) should I initialize the parameters of the hypothesis to?

Doesn't matter. The cost function is convex, so we will always ending up finding min(J)

## How should I split my dataset into the training set, cross validation set, and testing set?

## Declaring convergence

Declare convergence of if cost decreases by less than 1E-3 in one iteration of gradient descent