from flask import Flask, render_template, request, redirect, url_for
import pg8000

app = Flask(__name__)

# Database connection parameters
DB_CONFIG = {
    "user": "postgres",
    "password": "aztrein7008",
    "host": "rds_endpoit",
    "port": 5432,
    "database": "postgres"
}

def get_db_connection():
    try:
        conn = pg8000.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        level = request.form["level"]
        return redirect(url_for("timetable", level=level))
    return render_template("time.html")

@app.route("/timetable", methods=["GET"])
def timetable():
    level = request.args.get('level')

    if not level or not level.isdigit() or int(level) not in range(1, 5):
        return "Invalid level provided", 400

    conn = get_db_connection()
    if not conn:
        return "Unable to connect to the database", 500

    cur = conn.cursor()
    try:
        cur.execute("SELECT * FROM Timetable WHERE level = %s;", (level,))
        rows = cur.fetchall()
    except Exception as e:
        print(f"Error executing query: {e}")
        return "Error fetching data", 500
    finally:
        cur.close()
        conn.close()

    if rows:
        return render_template("timetable.html", level=level, data=rows, message="")
    else:
        return render_template("timetable.html", level=level, data=[], message="No data found for this level.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
