from flask import Flask

app = Flask(__name__)

students = [
    {"name": "Rahul", "marks": [80, 75, 90]}
]

def calculate_avg(marks):
    return sum(marks) / 3

@app.route("/")
def home():
    output = "<h1>Student Report</h1>"

    for s in students:
        avg = calculate_avg(s["marks"])
        output += f"""
        <hr>
        <h3>Name: {s['name']}</h3>
        <p>Marks: {s['marks']}</p>
        <p>Average: {avg:.2f}</p>
        """

    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
