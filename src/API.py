from samgeo.text_sam import LangSAM
import os
import numpy as np
import pandas as pd
from flask import Flask, jsonify, request, send_file

# Create a Flask application
app = Flask(__name__)

os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
sam = LangSAM()
text_prompt = "tree"

def calculate_centroid(mask, file_name):
    list_rows = []
    numpy_array = mask.numpy()
    for each in numpy_array:
        rows, cols = np.where(each == True)
        # Calculate the centroid
        centroid_x = np.mean(cols)
        centroid_y = np.mean(rows)
        print(centroid_x, centroid_y)

        list_rows.append({'x': centroid_x, 'y': centroid_y})
    return list_rows


"""
Take an input image
"""


@app.route("/api/upload", methods=["POST"])
def upload_image():
    if "file" not in request.files:
        return "No file part"

    file = request.files["file"]

    if file.filename == "":
        return "No selected file"

    # Process the file here (e.g., save it, perform operations, etc.)
    # For example, you can save it to a specific location
    print("Saving file")
    file.save("uploaded_image.jpg")
    print("Starting prediction")
    sam.predict(
        "uploaded_image.jpg", text_prompt, box_threshold=0.24, text_threshold=0.24
    )
    mask_final = sam.masks
    print("Done predicting")
    print("Calculating centroids")
    masks = calculate_centroid(mask_final, "data")
    print("Done!")
    return masks

if __name__ == "__main__":
    # Run the Flask app on a local development server
    app.run(debug=True)
