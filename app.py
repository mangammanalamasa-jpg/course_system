from flask import Flask

app = Flask(__name__)

# Google Drive Links Variables
stage1_link = "https://drive.google.com/drive/folders/1zldeYaFjmwFWUFhbQFm3zcj3sUCIdD_8?usp=sharing"
stage2_link = "https://drive.google.com/drive/folders/1bOBXTMPLBcIH7pL2BN2Flu4ezs33ScXC?usp=sharing"
stage3_link = "https://drive.google.com/drive/folders/1nPCQxa0_35whcJ0PV2LxXvKECGzZGomO?usp=sharing"
stage4_link = "https://drive.google.com/drive/folders/1NtrD2MBDsM2vzyu1EZScxu5OU7YM5hRs?usp=sharing"
stage5_link = "https://drive.google.com/drive/folders/1wRhGOoeB2aexQGGk1_HAzfepJaxraSza?usp=sharing"
stage6_link = "https://drive.google.com/drive/folders/1vsN3QLptdo21ArLe2nDYCVc1E5jhSnVY?usp=sharing"
stage7_link = "https://drive.google.com/drive/folders/1DmvLwgR09PrxHbVIOlL8tK547XC6tsE8?usp=sharing"

permissions = {
    "s1": [
        ("Stage 1", stage1_link)
    ],

    "s2": [
        ("Stage 1", stage1_link),
        ("Stage 2", stage2_link)
    ],

    "s3": [
        ("Stage 1", stage1_link),
        ("Stage 2", stage2_link),
        ("Stage 3", stage3_link)
    ],

    "s4": [
        ("Stage 1", stage1_link),
        ("Stage 2", stage2_link),
        ("Stage 3", stage3_link),
        ("Stage 4", stage4_link)
    ],

    "s5": [
        ("Stage 1", stage1_link),
        ("Stage 2", stage2_link),
        ("Stage 3", stage3_link),
        ("Stage 4", stage4_link),
        ("Stage 5", stage5_link)
    ],

    "s6": [
        ("Stage 1", stage1_link),
        ("Stage 2", stage2_link),
        ("Stage 3", stage3_link),
        ("Stage 4", stage4_link),
        ("Stage 5", stage5_link),
        ("Stage 6", stage6_link)
    ],

    "s7": [
        ("Stage 1", stage1_link),
        ("Stage 2", stage2_link),
        ("Stage 3", stage3_link),
        ("Stage 4", stage4_link),
        ("Stage 5", stage5_link),
        ("Stage 6", stage6_link),
        ("Stage 7", stage7_link)
    ]
}

@app.route("/<level>")
def home(level):
    data = permissions.get(level, [])
    
    if not data:
        return "<h1>Stage Not Found</h1><p>Please check your link endpoint (e.g., /s1, /s2...)</p>", 404

    html = "<h1>Let's Speak Materials</h1>"

    for stage, link in data:
        html += f"<h3><a href='{link}' target='_blank'>{stage}</a></h3>"

    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)