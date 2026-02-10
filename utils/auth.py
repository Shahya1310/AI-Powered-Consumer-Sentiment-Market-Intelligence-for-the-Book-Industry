import pandas as pd
from pathlib import Path

USERS = Path("users.csv")

def login(username, password):
    if not USERS.exists():
        return None

    df = pd.read_csv(USERS, dtype=str)

    df["username"] = df["username"].str.strip()
    df["password"] = df["password"].str.strip()

    username = username.strip()
    password = password.strip()

    match = df[
        (df["username"] == username) &
        (df["password"] == password)
    ]

    if match.empty:
        return None

    # ✅ return persona string instead of True
    return match.iloc[0]["persona"]
