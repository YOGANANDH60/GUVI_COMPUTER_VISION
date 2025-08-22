import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets,metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

digits = datasets.load_digits()

x = digits.images
y = digits.target

n_sample = len(x)
x = x.reshape((n_sample,-1))

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5,shuffle=False)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x_train,y_train)

y_pred = knn.predict(x_test)

print("KNN accuracy",metrics.accuracy_score(y_test,y_pred))

image_and_prediction = list(zip(digits.images[n_sample // 2:], y_pred))

for index, (image, prediction) in enumerate(image_and_prediction[:4]):  # only 4 images
    plt.subplot(1, 4, index + 1)
    plt.axis("off")
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation="nearest")
    plt.title(f'Pred: {prediction}')

plt.show()

