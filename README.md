# 🏀 NBA Win Predictor (Machine Learning & Basketball Analytics)

I built a machine learning model that predicts NBA home-game outcomes based on offensive and defensive averages (points scored vs points allowed). The cool part is that I actually tested these predictions on real Warriors games instead of just running code and assuming it’s correct. I’m a huge Golden State fan, so of course I tested the model on Warriors matchups first 😅

At one point, I tried Golden State vs Cleveland, and the model predicted Cleveland would win. The funny part is the Warriors actually won that game — but Curry was out, and the model currently has no idea which players are missing, so it just uses the full-strength scoring stats. That instantly showed me one of the biggest weaknesses in sports analytics: *player availability changes everything.*

So instead of taking the result as “model was wrong,” I realized this is something I want to improve (and it's actually really realistic). In the future, I want to include things like injuries, starters vs bench lineups, player offensive impact, etc.

---

## 🔥 What the model does right now
- trains a Logistic Regression classifier
- uses sample NBA-style scoring data
- evaluates accuracy using scikit-learn
- predicts whether the HOME team is more likely to win
- gives probability (e.g., “home team wins with 72% confidence”)
- lets me type in two teams and compare them

---

## 🚀 How to run it
Activate your venv and run:

```bash
python main.py
