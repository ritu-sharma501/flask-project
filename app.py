from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Website - Version 2</title>
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
                background:#333;
                color:white;
                padding:15px;
                margin-top:30px;
            }
        </style>
    </head>

    <body>

        <header>
            <h1>Flask Website - Version 2</h1>
            <p>CI/CD Pipeline using Docker & Jenkins</p>
        </header>

        <div class="container">

            <div class="card">
                <h2>Welcome</h2>
                <p>This Flask application is deployed using Docker and Jenkins Pipeline.</p>

                <button onclick="alert('Deployment Successful!')">
                    Click Me
                </button>
            </div>

        </div>

        <footer>
            © 2026 Flask Docker Jenkins Project | Created by Ritu Sharma
        </footer>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
