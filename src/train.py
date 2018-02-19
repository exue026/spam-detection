from compute import cost, gradient, H

def gradient_descent(X, y, theta, reg_const, alpha, epsilon):
    prev_error = float('inf') 
    error = cost(H, X, theta, y, reg_const)
    while abs(prev_error - error) > epsilon:
        theta = theta - alpha * gradient(H, X, theta, y, reg_const)
        prev_error = error
        error = cost(H, X, theta, y, reg_const)
    return (theta, error)