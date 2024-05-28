from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/match_result", methods=["POST"])
def match_result():
    scores = request.json["scores"]
    player1_set_wins = 0
    player2_set_wins = 0

    for set_score in scores:
        if set_score[0] > set_score[1]:
            player1_set_wins += 1
        elif set_score[0] < set_score[1]:
            player2_set_wins += 1

    if player1_set_wins > player2_set_wins:
        return jsonify(result=1)
    elif player2_set_wins > player1_set_wins:
        return jsonify(result=2)
    else:
        return jsonify(error="Invalid scores")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
