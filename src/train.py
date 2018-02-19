from compute import cost, gradient, H

def gradient_descent(X, y, theta, reg_const, alpha, epsilon):
    prev_error = float('inf') 
    error = cost(H, X, theta, y, reg_const)
    iterations = []
    iters = 0
    error_history = []
    while abs(prev_error - error) > epsilon:
        theta = theta - alpha * gradient(H, X, theta, y, reg_const)
        prev_error = error
        error = cost(H, X, theta, y, reg_const)
        iters += 1
        iterations.append(iters)
        error_history.append(error)
    return (theta, error, error_history, iterations)