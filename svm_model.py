from sklearn import svm
import numpy as np

# training data
X_train = np.array([
    [30, 2, 5],   # normal
    [40, 3, 8],   # normal
    [80, 20, 30], # congested
    [100, 25, 50] # congested
])

y_train = [0, 0, 1, 1]

# create model
model = svm.SVC(kernel='rbf')

model.fit(X_train, y_train)

def detect_congestion(mean_rtt, std_dev, elevation):

    features = [[mean_rtt, std_dev, elevation]]

    prediction = model.predict(features)

    return prediction[0]