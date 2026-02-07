from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from scraper import fetch_insta_data 

app = Flask(__name__)
CORS(app) 

@app.route('/')
def home():
    return render_template('index.html')

# --- NEW PAGES ---
@app.route('/privacy')
def privacy():
    return render_template('privacy.html')

@app.route('/terms')
def terms():
    return render_template('terms.html')

@app.route('/about')
def about():
    return render_template('about.html')
# -----------------

@app.route('/download', methods=['POST'])
def download():
    data = request.get_json()
    user_input = data.get('url')
    
    if not user_input:
        return jsonify({"error": "No URL provided"}), 400

    result = fetch_insta_data(user_input)
    
    if "error" in result:
        return jsonify(result), 500
        
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)