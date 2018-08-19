class AdaBoost:
    def __init__(self):
        return

    def train(self, X, Y, S):
        for i in range(len(X)):
            S = (X[i] + X[i+1]) / 2
            c1 =
        return

    def predict(self, X):
        return

if __name__ == "__main__":
    X = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Y = [5.56, 5.70, 5.91, 6.40, 6.80, 7.05, 8.90, 8.70, 9.00, 9.05]
    S = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5]
    a = new AdaBoost()
    loss = a.train(X, Y, S)
    print(loss)
