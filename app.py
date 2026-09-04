from flask import Flask,request,redirect,url_for ,send_from_directory, render_template_string
import os
from werkzeug.utils import secure_filename

app=Flask(__name__)

UPLOAD_FOLDER="uploads"
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER,exist_ok=True)

@app.route("/")
def home():

    files=os.listdir(UPLOAD_FOLDER)

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
          <title>My Handwritten Notes</title>
          <style>
          body{
                font-family:Arial,sans-serif;
                margin:40x;
                background-color:#f5f5f5;
                }        
h1 {
     color:#333;
     }
.box {
       background:pink;
       padding:25px;
       border-redius: 10px;
       max-width: 700px;
       }

button {
        panding: 8px 15px;
        cursor: pointer;
        }
 li {
     margin: 10px 0;
     }
a {
    text-decoration: none;
    color: blue;
    } 
    </style>
  </head>
  <body>

  <div class="box">

  <h1>My handwritten Notes</h1>
  <p>Welcome to my notes website!</p>
  <h2>Upload Your Notes</h2>
  <from action="/upload" method="POST" enctype="multipart/from-data">
   <input type="file" name="note" required>
   <button type="submit"> Upload Note</button>
   </from>

   <h2>Uploaded Notes</h2>

   {% if files %}
   <ul>
       {% for file in files %}
       <li>
          <a href="{{ url_for('uploaded_file', filename=file) }}" target="_blank">
            {{ file }}
      </a>
   </li> 

  {% endfor %}
  </ul>
  {% else %}
   <p> No notes uploaded yet.</p>
   {% endif %}
</div>
</body.
</html>
""",files=files)

@app.route("/upload",methods=["POST"])
def upload():
    file=request.files.get("note")  

    if file and file.filename !="":
        filename= secure_filename(file.filename)

        file.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )
        )
    return redirect(url_for("home"))

@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        filename
    )


if __name__=="__main__": 
    app .run(debug=True)