from sklearn import datasets, linear_model

class LinearModel(object):
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def fit(self, X, y):
        reg = linear_model.LinearRegression()
        reg.fit(X.reshape(-1, 1), y)
        self.a = reg.coef_[0]
        self.b = reg.intercept_

    def serialise(self):
        return {
            'a': self.a,
            'b': self.b,
            'model_module': 'linear_model',
            'model_class': 'LinearModel',
        }
    def predict(self, X):
        return self.a * X + self.b

