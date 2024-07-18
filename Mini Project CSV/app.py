from flask import Flask, jsonify, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/groups')
def data1():
    return render_template('groups.html')

@app.route('/softwares')
def data2():
    return render_template('softwares.html')

@app.route('/techniques')
def data3():
    return render_template('techniques.html')


# Define API endpoints for each CSV file
@app.route('/api/data1')
def get_data1():
    return jsonify(read_csv('data/group_info.csv'))

@app.route('/api/data2')
def get_data2():
    return jsonify(read_csv('data/software_info.csv'))

@app.route('/api/data3')
def get_data3():
    return jsonify(read_csv('data/technique_info.csv'))

# Helper function to read and process CSV files
def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        df = df.where(pd.notnull(df), None)  # Replace NaN with None
        return df.to_dict(orient='records')
    except Exception as e:
        return {'error': str(e)}

if __name__ == '__main__':
    app.run(debug=True)