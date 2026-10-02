from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = "events.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def create_database():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS registrations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            department TEXT NOT NULL,
            event TEXT NOT NULL,
            registered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"].strip()
        email = request.form["email"].strip()
        phone = request.form["phone"].strip()
        department = request.form["department"]
        event = request.form["event"]

        conn = get_db()

        conn.execute("""
            INSERT INTO registrations
            (name, email, phone, department, event)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, phone, department, event))

        conn.commit()
        conn.close()

        return redirect(url_for("success"))

    return render_template("register.html")


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/admin")
def admin():

    conn = get_db()

    registrations = conn.execute("""
        SELECT * FROM registrations
        ORDER BY id DESC
    """).fetchall()

    total = conn.execute(
        "SELECT COUNT(*) FROM registrations"
    ).fetchone()[0]

    hackathon = conn.execute(
        "SELECT COUNT(*) FROM registrations WHERE event='Hackathon'"
    ).fetchone()[0]

    cultural = conn.execute(
        "SELECT COUNT(*) FROM registrations WHERE event='Cultural Fest'"
    ).fetchone()[0]

    sports = conn.execute(
        "SELECT COUNT(*) FROM registrations WHERE event='Sports Meet'"
    ).fetchone()[0]

    quiz = conn.execute(
        "SELECT COUNT(*) FROM registrations WHERE event='Quiz Competition'"
    ).fetchone()[0]

    conn.close()

    stats = {
        "total": total,
        "hackathon": hackathon,
        "cultural": cultural,
        "sports": sports,
        "quiz": quiz
    }

    return render_template(
        "admin.html",
        registrations=registrations,
        stats=stats
    )


@app.route("/delete/<int:registration_id>", methods=["POST"])
def delete_registration(registration_id):

    conn = get_db()

    conn.execute(
        "DELETE FROM registrations WHERE id=?",
        (registration_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("admin"))


if __name__ == "__main__":
    create_database()
    app.run(debug=True)