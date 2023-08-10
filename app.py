import os
import pandas as pd
import openai
from flask import Flask, render_template, request
from chat2plot import chat2plot

app = Flask(__name__)

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your api_key"  # Replace with your actual OpenAI API key

#Load the excel file into a DataFrame (replace 'reduced_data1.xlsx' with your file name)

data = pd.read_csv('forecasting2.csv')

# Initialize the chat2plot object
c2p = chat2plot(data)


@app.route('/', methods=['GET', 'POST'])
def index():
    plot_url = None
    config = None
    explanation = None

    if request.method == 'POST':
        prompt = request.form['prompt']
        if prompt:
            # Generate the plot and get config and explanation
            result = c2p(prompt)
            plot_url = result.figure.to_html()
            config = result.config
            explanation = result.explanation

    return render_template('index.html', plot_url=plot_url, config=config, explanation=explanation)


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
