from flask import Flask, jsonify
from LCK_teams_scraper import scrape_and_store_data

app = Flask(__name__)

@app.route('/fetch-stats', methods=['GET'])
def fetch_stats():
    scrape_and_store_data()
    return jsonify({'message': 'LCK teams stats fetched and stored in S3'}), 200

if __name__ == '__main__':
    app.run(debug=True)
