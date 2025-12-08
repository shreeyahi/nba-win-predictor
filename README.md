# 🏀 NBA Win Predictor (Machine Learning & Basketball Analytics)

I built a machine learning model that predicts NBA home-game outcomes based on offensive and defensive averages (points scored vs points allowed). The cool part is that I actually tested these predictions on real Warriors games instead of just running code and assuming it’s correct. I’m a huge Golden State fan, so of course I tested the model on Warriors matchups first !!

Since this morning, (7th December 2025). Well, morning in UAE at least was the Golden State vs Cleveland matchup, I decided to put this model to the test and see how accurate it was. Golden State won (🥳), howeverrr, the model said that we had only a 3.6% chance of winning 😗... 
That was when I spotted a limitation. Star players like Steph Curry, Jimmy Butler, Draymond Green (and 9 others on both teams)  were out, and the model didn't acknowledge/account for those players. So, it just uses the full-strength scoring stats. That instantly showed me one of the biggest weaknesses in sports analytics: *player availability changes everything.*

So instead of taking the result as “model was wrong,” I realized this is something I want to improve (and it's actually really realistic). In the future, I want to include things like injuries, starters vs bench lineups, player offensive impact, etc.

---

## 🔥 What the model does right now
- trains a Logistic Regression classifier
- utilizes sample NBA-style scoring data
- evaluates accuracy using scikit-learn
- predicts whether the HOME team is more likely to win
- gives probability (e.g., “Estimated probability home team wins: 72%”)
- lets me type in two teams and compare them

---

## 🚀 How to run it

Activate your venv and run:

```bash
python main.py
```



## 🧠 Why I’m interested in this
I love the NBA (especially the Warriors), and this was a way for me to mix basketball with machine learning. I think sports analytics is such a fun way of learning and experimenting with data science because I can actually compare results with real games instead of solving random equations.

---

## ✨ What I learned
- how Logistic Regression works
- how accuracy/testing works in ML
- how different features change predictions
- simple data pre-processing
- evaluating models beyond just accuracy
- that real basketball isn’t only numbers — players matter a LOT (especially star players)

---

## 🔮 Next steps / Future improvements
- account for injured or missing players
- compare multiple ML models (Random Forest, XGB, etc.)
- add playoff matchups
- add lineup/offensive-rating impact (Curry off court, Draymond defense, etc.)
- maybe build a Streamlit web app later

---

## 🛠 Tools used
- Python  
- scikit-learn  
- pandas  
- VS Code  
- GitHub  

---

## 🏆 Personal note
This project is part of my AI portfolio for university and something I want to keep improving. I also want to try predicting Warriors playoff matchups later and compare model probabilities with real outcomes, especially when Curry or key starters/contributors are out.

