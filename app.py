from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_required_grades(prelim_grade):
    passing_grade = 75
    prelim_weight = 0.20
    midterm_weight = 0.30
    final_weight = 0.50
    grade_range = (0, 100)

    if not (grade_range[0] <= prelim_grade <= grade_range[1]):
        return "Preliminary grade must be between 0 and 100."

    current_total = prelim_grade * prelim_weight
    required_total = passing_grade - current_total
    midterm_final_weight = midterm_weight + final_weight
    min_required_average = required_total / midterm_final_weight

    if min_required_average > 100:
        return "It is not possible to achieve the passing grade with this preliminary score."

    if min_required_average < grade_range[0]:
        min_required_average = grade_range[0]

    return f"{min_required_average:.2f}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    prelim_grade = float(request.form['prelim_grade'])
    result = calculate_required_grades(prelim_grade)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
