def main():
    import pandas as pd
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    star_data = pd.read_csv('stars.csv')
    # Star color column: Strings to integers
    # Red is the lowest, blue is the highest. Intermediary values are mapped as such.
    color_map = {'red': 0, 'orange-red': 1, 'blue white': 1, 'orange': 2, 'pale yellow orange': 3, 'yellowish': 4,
                 'yellow-white': 5, 'yellowish white': 6, 'white-yellow': 7, 'whitish': 8, 'white': 9, 'blue-white': 10,
                 'blue': 11}
    colors = list(star_data['Star color'])
    for i in range(len(colors)):
        colors[i] = color_map[colors[i].lower().strip()]
    star_data.drop(['Star color'], axis=1)
    star_data['Star color'] = colors

    # Spectral Class column: Chars to integers
    classes = list(star_data['Spectral Class'])
    for i in range(len(classes)):
        temp = list()
        temp.extend(classes[i])
        classes[i] = ord(temp[0])
    star_data.drop(['Spectral Class'], axis=1)
    star_data['Spectral Class'] = classes

    # Train and test 30 times and take average accuracy
    x = star_data.drop(columns=['Star type'])
    y = star_data['Star type']
    score = 0.0
    for i in range(30):
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
        model = DecisionTreeClassifier()
        model.fit(x_train, y_train)
        predictions = model.predict(x_test)
        score += accuracy_score(y_test, predictions)
    print(score/30.0)


if __name__ == '__main__':
    main()
