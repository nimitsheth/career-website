from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'New York, NY',
        'salary': '$120,000',
        'description': 'Analyze data and build predictive models.'
    },
    {
        'id': 2,
        'title': 'Data Analyst',
        'location': 'San Francisco, CA',
        'salary': '$100,000',
        'description': 'Collect and interpret data to help make business decisions.'
    },
    {
        'id': 3,
        'title': 'Frontend Engineer',
        'location': 'Austin, TX',
        'salary': '$110,000',
        'description': 'Develop user interfaces and improve user experience.'
    },
    {
        'id': 4,
        'title': 'Backend Engineer',
        'location': 'Seattle, WA',
        'salary': '$120,000',
        'description': 'Develop server-side applications and APIs.'
    }
]

@app.route('/')
def home():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if(__name__ == '__main__'):
    app.run(debug=True, host='0.0.0.0')