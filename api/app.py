from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/health")
def health():
    return jsonify(status="ok", service="unity-api")


@app.get("/api/assets")
def assets():
    return jsonify(items=["terrain-pack", "character-rig", "vfx-smoke"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
