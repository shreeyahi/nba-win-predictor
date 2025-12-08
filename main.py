import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# --- 1. Toy NBA-like dataset (fake but realistic numbers) ---
data = [
    # home_ppg, away_ppg, home_opp_ppg, away_opp_ppg, home_win
    [118, 110, 111, 114, 1],
    [112, 115, 109, 110, 0],
    [120, 108, 112, 115, 1],
    [109, 113, 107, 108, 0],
    [122, 117, 110, 116, 1],
    [111, 119, 113, 112, 0],
    [116, 109, 108, 114, 1],
    [108, 112, 110, 109, 0],
    [121, 114, 109, 115, 1],
    [113, 118, 112, 111, 0],
    [117, 111, 110, 113, 1],
    [110, 116, 112, 110, 0],
    [119, 112, 109, 114, 1],
    [111, 117, 113, 109, 0],
    [123, 115, 111, 116, 1],
    [112, 120, 114, 112, 0],
]

df = pd.DataFrame(
    data,
    columns=["home_ppg", "away_ppg", "home_opp_ppg", "away_opp_ppg", "home_win"],
)

X = df[["home_ppg", "away_ppg", "home_opp_ppg", "away_opp_ppg"]]
y = df["home_win"]

# --- 2. Train/test split ---
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0
)

# --- 3. Train model ---
model = LogisticRegression()
model.fit(X_train, y_train)

# --- 4. Evaluate model ---
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("NBA Home Win Predictor")
print("----------------------")
print("Accuracy on test games:", round(accuracy, 3))
print("\nClassification report:")
print(classification_report(y_test, y_pred))
print("Confusion matrix:")
print(confusion_matrix(y_test, y_pred))

# --- 5. Let the user try their own matchup ---
print("\nTry your own matchup (enter season averages).")
print("All values are points per game (PPG).")

try:
    home_ppg = float(input("Home team: average points scored per game: "))
    away_ppg = float(input("Away team: average points scored per game: "))
    home_opp_ppg = float(input("Home team: average points allowed (opponent PPG): "))
    away_opp_ppg = float(input("Away team: average points allowed (opponent PPG): "))

    sample = [[home_ppg, away_ppg, home_opp_ppg, away_opp_ppg]]

    win_prob = model.predict_proba(sample)[0][1]  # probability home_win = 1
    prediction = model.predict(sample)[0]

    print("\nModel prediction:")
    if prediction == 1:
        print("→ The model thinks the HOME team is more likely to win.")
    else:
        print("→ The model thinks the AWAY team is more likely to win.")

    print("Estimated probability home team wins:", round(win_prob * 100, 1), "%")

except ValueError:
    print("\nInvalid input. Please enter numbers only next time.")
