<<<<<<< HEAD
from flask import Flask, render_template, request
from dotenv import load_dotenv
import openai
import os
import markdown
import html
import re
=======
from flask import Flask, render_template
import os
>>>>>>> 58b07f269d86dee87184eaaf1ba14a1f24a4469c

load_dotenv()
# Set up OpenAI client using the API key from env.
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

<<<<<<< HEAD
def format_code_output(raw_text):
    def replace_code_blocks(match):
        lang = match.group(1) or "plaintext"
        code = match.group(2)
        escaped_code = html.escape(code)
        return f'<pre class="code-box"><code class="language-{lang}">{escaped_code}</code></pre>'
    
    return re.sub(r"```(\w+)?\n(.*?)```", replace_code_blocks, raw_text, flags=re.DOTALL)
=======
@app.route('/')
def home():
    return render_template('index.html')  # or just return "Hello, World!"
>>>>>>> 58b07f269d86dee87184eaaf1ba14a1f24a4469c

@app.route("/", methods=["GET", "POST"])
def index():
    code_output = ""
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that writes code."},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.2,
                max_tokens=1000
            )
            raw_output = response.choices[0].message.content
            code_output = format_code_output(raw_output)
        except Exception as e:
            code_output = f"<p>Error: {str(e)}</p>"

    return render_template("index.html", code_output=code_output)

if __name__ == '__main__':
<<<<<<< HEAD
    # Bind to PORT environment variable.
=======
    # Bind to PORT environment variable if defined (e.g. GalaxyCloud, Heroku)
>>>>>>> 58b07f269d86dee87184eaaf1ba14a1f24a4469c
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
