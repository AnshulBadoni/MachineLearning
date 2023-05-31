import numpy as np

def gradient_descent(x,y) :
    m_curve = b_curve = 0
    learning_rate = 0.008
    iteration = 10000
    n = len(x)
    for i in range(iteration):
        #y=mx+c
        y_predict  = m_curve * x + b_curve
        cost = (1/n) *sum([val**2 for val in (y-y_predict)])
        m_dericative = -(2/n) * sum(x*(y-y_predict))
        b_dericative = -(2/n) * sum(y-y_predict)
        m_curve = m_curve - learning_rate * m_dericative
        b_curve = b_curve -learning_rate * b_dericative
        print("m {}, b {}, cost {}, iteration {}".format(m_curve,b_curve,cost,i))


x = np.array([1,2,3,4,5])
y = np.array([5,7,9,11,13])

gradient_descent(x,y)