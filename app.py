from flask import Flask

app = Flask(__name__)

permissions = {
    "s1":[
        ("Stage1","https://drive.google.com/drive/folders/1zldeYaFjmwFWUFhbQFm3zcj3sUCIdD_8?usp=sharing")
    ],

    "s2":[
        ("Stage1","https://drive.google.com/drive/folders/1zldeYaFjmwFWUFhbQFm3zcj3sUCIdD_8?usp=sharing"),
        ("Stage2","https://drive.google.com/drive/folders/1bOBXTMPLBcIH7pL2BN2Flu4ezs33ScXC?usp=sharing")
    ],

    "s3":[
        ("Stage1","https://drive.google.com/drive/folders/1zldeYaFjmwFWUFhbQFm3zcj3sUCIdD_8?usp=sharing"),
        ("Stage2","https://drive.google.com/drive/folders/1bOBXTMPLBcIH7pL2BN2Flu4ezs33ScXC?usp=sharing"),
        ("Stage3","https://drive.google.com/drive/folders/1nPCQxa0_35whcJ0PV2LxXvKECGzZGomO?usp=sharing")
    ]
}

@app.route("/<level>")
def home(level):

    data = permissions.get(level, [])

    html="<h1>Let's Speak Materials</h1>"

    for stage,link in data:
        html += f"<h3><a href='{link}'>{stage}</a></h3>"

    return html

if __name__=="__main__":
   app.run(host="0.0.0.0", port=5000, debug=False)