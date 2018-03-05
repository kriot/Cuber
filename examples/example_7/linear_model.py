from sklearn import datasets, linear_model

class LinearModel(object):
    def __init__(self, a = 0, b = 0):
        self.a = a
        self.b = b

    def fit(self, X, y):
        reg = linear_model.LinearRegression()
        reg.fit(X.reshape(-1, 1), y)
        models_list = []
        models_list.append(LinearModel(
            a = reg.coef_[0],
            b = reg.intercept_
        ))
        for alpha in [0.1, 0.2, 0.5, 1.0, 10., 100.]:
            reg = linear_model.Lasso(alpha = alpha)
            reg.fit(X.reshape(-1, 1), y)
            models_list.append(LinearModel(
                a = reg.coef_[0],
                b = reg.intercept_
            ))
        return models_list

    def serialise(self):
        return {
            'model_params': {
                'a': self.a,
                'b': self.b,
            },
            'model_module': 'linear_model',
            'model_class': 'LinearModel',
        }
    def predict(self, X):
        return self.a * X + self.b

