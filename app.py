from flask import Flask, render_template, request, redirect

# 🔴 NEW: import os (to read environment variables)
import os

app = Flask(__name__)

students = []
student_names = set()


def calculate_average(marks):
    try:
        return sum(marks) / len(marks)
    except ZeroDivisionError:
        return 0


@app.route('/')
def home():
    return render_template('index.html', students=students)


@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form['name']

        if name in student_names:
            return "Student already exists!"

        try:
            marks = [
                float(request.form['m1']),
                float(request.form['m2']),
                float(request.form['m3'])
            ]
        except ValueError:
            return "Invalid marks!"

        avg = calculate_average(marks)

        student = {
            "name": name,
            "marks": marks,
            "average": avg
        }

        students.append(student)
        student_names.add(name)

        return redirect('/')

    return render_template('add.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    result = None

    if request.method == 'POST':
        name = request.form['name']

        for s in students:
            if s['name'].lower() == name.lower():
                result = s
                break

    return render_template('search.html', result=result)


@app.route('/delete/<name>')
def delete(name):
    global students

    students = [s for s in students if s['name'] != name]
    student_names.discard(name)

    return redirect('/')


# 🔴 UPDATED BLOCK STARTS HERE
if __name__ == "__main__":
    # 🔴 NEW: read port from environment variable
    port = int(os.environ.get("APP_PORT", 5000))

    # 🔴 OPTIONAL (for learning visibility)
    mode = os.environ.get("APP_MODE", "dev")
    print(f"Running in {mode} mode on port {port}")

    app.run(host="0.0.0.0", port=port)
# 🔴 UPDATED BLOCK ENDS HERE
