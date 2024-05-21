# Tennis score calculator
This is a simple tennis score calculator that can be used to figure out who won a tennis match based on the score.

## How to use
This is a python based api endpoint using flask. To run the server make sure you have python installed. 

### Prerequisites
- Python 3.10
- Flask
- Flask-Testing

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/mbauer575/CS361_ScoreManager
    ```
2. Install the required packages I recommend using a virtual environment
    ```sh
    python -m venv venv
    .\venv\Scripts\activate
    ```
    ```sh
    pip install -r requirements.txt
    ```
3. Run the tests
    ```sh
    python -m unittest test_scorekeeper.py
    ```
4. Run the server
    ```sh
    python app.py
    ```

## API Endpoints
* POST /match_results: Accepts a Json object with the 'scores' key. The value should be a list of lists, where each inner list contains two integers representing the scores of player 1 and player 2 respectively. Each inner list represents a game. The endpoint will return the winner of the match.
### Example
POST request to /match_results
```
{
    "scores": [[7, 6], [2, 6], [6, 3]]
}
```
Response
```
{
   "result": "1"
}
```

