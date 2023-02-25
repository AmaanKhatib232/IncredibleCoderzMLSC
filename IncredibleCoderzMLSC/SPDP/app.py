from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input text from the form.
        input_text = request.form.get('text1')

        # Generate a prompt based on the input text.
        output_text = generate_prompt(input_text)

        # Split the prompt into substrings and generate an image for each substring.
        array_of_substrings = output_text.split(".")
        output_img_links = []
        print(len(array_of_substrings))
        for substring in range(len(array_of_substrings)-1):
            img_link = generate_image(array_of_substrings[substring])
            if img_link:
                output_img_links.append(img_link)

        # Render the output template with the image links.
        return render_template('visualize_page.html', output_img_links=output_img_links,)

    # Render the input form.
    return render_template('visualize_page.html')

def generate_prompt(text):
    # Call the API to generate a prompt based on the input text.
    api_url = "https://v1.genr.ai/api/circuit-element/generate-prompt"
    response = requests.post(api_url, json={'text': text})
    print (json.loads(response.text)["output"])
    if response.status_code == 200:
        return json.loads(response.text)["output"]
    else:
        return f"Error generating prompt: {response.text}"

def generate_image(prompt):
    # Call the API to generate an image based on the prompt.
    print("hiiii\n\n")
    print(prompt)
    api_url = "https://v1.genr.ai/api/circuit-element/generate-image"
    response = requests.post(api_url, json={'prompt': prompt, 'model': 'stable-diffusion-2', 'height': '512', 'width': '512'})
    print(json.loads(response.text)["output"])
    if response.status_code == 200:
        return json.loads(response.text)["output"]
    else:
        return f"Error generating image: {response.text}"

if __name__ == '__main__':
    # Run the Flask app.
    app.run(debug=True)
