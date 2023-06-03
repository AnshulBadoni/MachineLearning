import numpy as np

def marks(x,y):
    m_curve = b_curve = 0
    alpha = 0.05 #learning rate
    iteration = 1000
    n = len(x)

    for i in range(iteration):
        #y = mx + c
        y_predict = m_curve * x + b_curve
        # error = (1/n) * sum((y-y_predict)**2)
        error = (1/n) *sum([val**2 for val in (y-y_predict)])
        m_derivative = -(2/n) * sum(x*(y-y_predict))
        b_derivative = -(2/n) * sum((y-y_predict))
        m_curve = m_curve - alpha * m_derivative
        b_curve = b_curve - alpha * b_derivative
        print("m {}, b {}, error {}, iteration".format(m_curve,b_curve,error,iteration))  

    #calculating error after loop
    y_predict = m_curve * x + b_curve
    # error = (1/n) * sum((y-y_predict)**2)
    error = (1/n) *sum([val**2 for val in (y-y_predict)])
    print("Final error: {}".format(error))

    
x = np.array([92,56,88,70,80,49,65,35,66,67])
y = np.array([98,68,81,80,83,52,66,30,68,73])

marks(x,y)