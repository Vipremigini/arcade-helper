# Funky Project Generator

This Flask application generates funky, simple project ideas using OpenAI's GPT-3.5-turbo model. The app is designed to respond to POST requests, send a request to the OpenAI API, and return a unique project idea.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Environment Variables](#environment-variables)

## Requirements

- Python 3.7+
- Flask
- Gunicorn
- Requests
- OpenAI

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/funky-project-generator.git
    cd funky-project-generator
    ```

2. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Set your environment variables (see below for required variables).

2. Run the Flask app locally:

    ```bash
    flask run
    ```

3. Send a POST request to the `/api/try` endpoint with a `response_url` parameter to receive a funky project idea.

## Deployment

### Heroku

1. Install the Heroku CLI if you haven't already:

    ```bash
    curl https://cli-assets.heroku.com/install.sh | sh
    ```

2. Login to Heroku:

    ```bash
    heroku login
    ```

3. Create a new Heroku app:

    ```bash
    heroku create your-app-name
    ```

4. Add your environment variables to Heroku:

    ```bash
    heroku config:set OPENAI_API_KEY=your_openai_api_key
    ```

5. Deploy your code to Heroku:

    ```bash
    git add .
    git commit -m "Deploy to Heroku"
    git push heroku master
    ```

6. Scale the web dyno:

    ```bash
    heroku ps:scale web=1
    ```

## Environment Variables

Make sure to set the following environment variables in your Heroku config or your local environment:

- `OPENAI_API_KEY`: Your OpenAI API key.

## File Structure

