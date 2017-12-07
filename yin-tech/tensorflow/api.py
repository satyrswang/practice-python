cross_validation.train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

feature_columns = tf.contrib.learn.infer_real_valued_columns_from_input(x_train)

score = metrics.accuracy_score(y_test,predictions)

classifier = tf.contrib.learn.DNNClassifier(feature_columns = feature_columns, hidden_units = [10,20,10],n_classes =3)
predictions = list(classifier.predict(x_test,as_iterable = True))
print('Accuracy: {0:f}'.format(score))

