import warnings

from sklearn.datasets import fetch_lfw_people
from sklearn.decomposition import PCA
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings("ignore")

# Load data
lfw_dataset = fetch_lfw_people(min_faces_per_person=100)

# _, h, w = lfw_dataset.images.shape
X = lfw_dataset.data
y = lfw_dataset.target
target_names = lfw_dataset.target_names

# split into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Compute a PCA 
n_components = 100
pca = PCA(n_components=n_components, whiten=True).fit(X_train)

# apply PCA transformation
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# train a neural network
print("Fitting the classifier to the training set")
clf = MLPClassifier(hidden_layer_sizes=(256), batch_size=256, verbose=True, early_stopping=True).fit(X_train_pca,
                                                                                                     y_train)

# clf1 = RandomForestClassifier(n_estimators=500)
# clf1.fit(X_train_pca, y_train)
y_pred = clf.predict(X_test_pca)
#y_pred1 = clf1.predict(X_test_pca)
print(classification_report(y_test, y_pred, target_names=target_names))
print(accuracy_score(y_test, y_pred))
#print(accuracy_score(y_test, y_pred1))
