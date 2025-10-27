import sqlite3

USER_DB = "users.db"
RULES_DB = "rules.db"

def get_all_users():
    conn = sqlite3.connect(USER_DB)
    cur = conn.cursor()
    cur.execute("SELECT id, name, level FROM users")
    users = [{"id": u[0], "name": u[1], "level": u[2]} for u in cur.fetchall()]
    conn.close()
    return users

def get_user(user_id):
    conn = sqlite3.connect(USER_DB)
    cur = conn.cursor()

    cur.execute("SELECT id, name, level FROM users WHERE id = ?", (user_id,))
    row = cur.fetchone()
    if not row:
        return None
    user = {"id": row[0], "name": row[1], "level": row[2]}

    cur.execute("SELECT preference FROM preferences WHERE user_id = ?", (user_id,))
    user["preferences"] = [r[0] for r in cur.fetchall()]

    cur.execute("SELECT avg_score, attempts, success_rate FROM performance WHERE user_id = ?", (user_id,))
    perf = cur.fetchone()
    user["performance"] = {"avg_score": perf[0], "attempts": perf[1], "success_rate": perf[2]} if perf else {}

    conn.close()
    return user

def get_rules():
    conn = sqlite3.connect(RULES_DB)
    cur = conn.cursor()
    cur.execute("SELECT rule_id, condition, adaptation FROM rules")
    rules = [{"rule_id": r[0], "condition": r[1], "adaptation": r[2]} for r in cur.fetchall()]
    conn.close()
    return rules
