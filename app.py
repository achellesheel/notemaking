from flask import Flask, request, render_template, jsonify
import os

app = Flask(__name__)

# Ensure the 'notes' directory exists
if not os.path.exists('./notes'):
    os.makedirs('./notes')

# Home route to display notes
@app.route("/")
def home():
    notes = []
    for filename in os.listdir('./notes'):
        if filename.endswith('.txt'):
            with open(f'./notes/{filename}', 'r') as file:
                notes.append({"title": filename[:-4], "content": file.read()})
    return render_template('index.html', notes=notes)

# API to add a new note
@app.route("/add", methods=["POST"])
def add_note():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    file_path = f'./notes/{title}.txt'

    if os.path.exists(file_path):
        return jsonify({"error": "Note already exists!"}), 400

    with open(file_path, 'w') as file:
        file.write(content)
    return jsonify({"message": "Note added successfully!"})

# API to edit an existing note
@app.route("/edit", methods=["POST"])
def edit_note():
    data = request.get_json()
    title = data.get("title")
    content = data.get("content")
    file_path = f'./notes/{title}.txt'

    if not os.path.exists(file_path):
        return jsonify({"error": "Note not found!"}), 404

    with open(file_path, 'w') as file:
        file.write(content)
    return jsonify({"message": "Note updated successfully!"})

if __name__ == "__main__":
    app.run(debug=True)
