from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My First Flask Website</title>
        <style>
            body{
                font-family: Arial, sans-serif;
                background-color:#f4f4f4;
                text-align:center;
                margin:0;
                padding:0;
            }

            header{
                background:#007BFF;
                color:white;
                padding:20px;
            }

            .container{
                width:80%;
                margin:auto;
                padding:30px;
            }

            .card{
                background:white;
                padding:20px;
                margin:20px;
                border-radius:10px;
                box-shadow:0 0 10px gray;
            }

            button{
                background:green;
                color:white;
                padding:12px 25px;
                border:none;
                border-radius:5px;
                cursor:pointer;
                font-size:16px;
            }

            button:hover{
                background:darkgreen;
            }

            footer{
                background:#222;
                color:white;
                padding:15px;
                margin-top:30px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Welcome to My Flask Website</h1>
        </header>

        <div class="container">

            <div class="card">
                <h2>About</h2>
                <p>This website is created using Python Flask.</p>
                <p>Flask is a lightweight web framework used to build web applications.</p>
            </div>

            <div class="card">
                <h2>Features</h2>
                <ul style="list-style:none;">
                    <li>✔ Python Flask</li>
                    <li>✔ HTML</li>
                    <li>✔ CSS</li>
                    <li>✔ Responsive Design</li>
                </ul>

                <button onclick="message()">Click Here</button>
            </div>

        </div>

        <footer>
            <p>© 2026 My Flask Website</p>
        </footer>

        <script>
            function message(){
                alert("Welcome to My Flask Website!");
            }
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
