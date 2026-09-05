from flask import Flask, render_template, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
@app.route("/google971a16a12f2883d8.html")
def google_verification():
    return send_from_directory(".","google971a16a12f2883d8.html")
users = {}
app.secret_key = "handwritten-notes-secret-key"

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {
    "pdf", "jpg", "jpeg", "png", "gif", "webp"
}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower()
        in ALLOWED_EXTENSIONS
    )


HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>Handwritten Notes</title>

    <style>

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f8f9ff;
            color: #202124;
        }


        /* ================= HEADER ================= */

        header {
            height: 70px;
            background: white;

            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 0 6%;

            border-bottom: 1px solid #eeeeee;

            position: sticky;
            top: 0;
            z-index: 100;
        }


        .logo {
            display: flex;
            align-items: center;
            gap: 10px;

            font-size: 20px;
            font-weight: bold;

            color: #263b80;
        }


        .logo-icon {
            width: 35px;
            height: 35px;

            display: flex;
            align-items: center;
            justify-content: center;

            background: #eef1ff;

            border-radius: 9px;

            font-size: 19px;
        }


        nav {
            display: flex;
            align-items: center;
            gap: 30px;
        }


        nav a {
            text-decoration: none;
            color: #555;

            font-size: 14px;
            font-weight: 500;
        }


        nav a:hover {
            color: #4d46d8;
        }


        .signup-btn {
            background: #5046e5;
            color: white !important;

            padding: 11px 19px;

            border-radius: 7px;
        }


        /* ================= HERO ================= */

        .hero {
            min-height: 560px;

            display: flex;
            align-items: center;
            justify-content: space-between;

            padding: 70px 8%;

            background: linear-gradient(
                135deg,
                #f5f7ff,
                #ffffff
            );

            gap: 50px;
        }


        .hero-text {
            width: 52%;
        }


        .hero-text h1 {
            font-size: 52px;
            line-height: 1.12;

            color: #202d59;

            margin-bottom: 22px;
        }


        .hero-text h1 span {
            color: #5146df;
        }


        .hero-text p {
            font-size: 18px;
            line-height: 1.7;

            color: #666;

            max-width: 570px;

            margin-bottom: 30px;
        }


        .hero-buttons {
            display: flex;
            gap: 15px;
        }


        .primary-btn {
            display: inline-block;

            text-decoration: none;

            background: #5046e5;
            color: white;

            padding: 14px 25px;

            border-radius: 8px;

            font-size: 15px;
            font-weight: bold;

            border: none;

            cursor: pointer;
        }


        .primary-btn:hover {
            background: #3e35c7;
        }


        .secondary-btn {
            display: inline-block;

            text-decoration: none;

            background: white;
            color: #5046e5;

            border: 1px solid #dcdcff;

            padding: 14px 25px;

            border-radius: 8px;

            font-size: 15px;
            font-weight: bold;
        }


        /* ================= HERO IMAGE ================= */

        .hero-image {
            width: 43%;

            display: flex;
            justify-content: center;
        }


        .note-illustration {
            width: 360px;
            height: 330px;

            background: white;

            border-radius: 25px;

            box-shadow:
                0 20px 50px rgba(50, 50, 100, 0.12);

            display: flex;
            align-items: center;
            justify-content: center;

            position: relative;
        }


        .notebook {
            width: 190px;
            height: 245px;

            background: #fffdf8;

            border: 3px solid #273b78;

            border-radius: 8px;

            transform: rotate(-7deg);

            box-shadow:
                8px 8px 0 #dfe5ff;

            padding: 30px 18px;
        }


        .notebook h3 {
            color: #273b78;
            text-align: center;

            font-size: 19px;

            margin-bottom: 25px;
        }


        .writing {
            height: 7px;
            background: #9aa6d8;

            margin: 12px 0;

            border-radius: 10px;
        }


        .writing.short {
            width: 65%;
        }


        .pen {
            position: absolute;

            right: 40px;
            bottom: 35px;

            font-size: 55px;

            transform: rotate(25deg);
        }


        /* ================= FEATURES ================= */

        .features {
            background: white;

            padding: 45px 8%;

            display: flex;
            justify-content: center;

            gap: 70px;

            border-bottom: 1px solid #eee;
        }


        .feature {
            text-align: center;

            max-width: 180px;
        }


        .feature-icon {
            width: 45px;
            height: 45px;

            margin: auto;
            margin-bottom: 12px;

            border-radius: 50%;

            background: #eef0ff;

            display: flex;
            align-items: center;
            justify-content: center;

            font-size: 20px;
        }


        .feature h3 {
            font-size: 15px;
            margin-bottom: 7px;

            color: #27345e;
        }


        .feature p {
            font-size: 12px;
            color: #777;
        }


        /* ================= UPLOAD ================= */

        .upload-section {
            padding: 70px 20px;

            text-align: center;
        }


        .section-title {
            font-size: 32px;
            color: #27345e;

            margin-bottom: 10px;
        }


        .section-description {
            color: #777;
            margin-bottom: 30px;
        }


        .upload-box {
            width: 90%;
            max-width: 650px;

            margin: auto;

            background: white;

            border: 2px dashed #c9ccf3;

            border-radius: 18px;

            padding: 45px 30px;

            box-shadow:
                0 8px 30px rgba(60, 60, 120, 0.07);
        }


        .upload-icon {
            font-size: 45px;
            margin-bottom: 15px;
        }


        .upload-box h2 {
            color: #27345e;
            margin-bottom: 8px;
        }


        .upload-box p {
            color: #777;
            margin-bottom: 20px;
        }


        input[type="file"] {
            width: 100%;

            padding: 12px;

            border: 1px solid #ddd;

            border-radius: 8px;

            margin-bottom: 18px;

            background: #fafafa;
        }


        /* ================= NOTES ================= */

        .notes-section {
            padding: 60px 7%;

            background: #f8f9ff;
        }


        .notes-header {
            text-align: center;
            margin-bottom: 35px;
        }


        .notes-container {
            max-width: 1100px;

            margin: auto;

            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 25px;
        }


        .note-card {
            background: white;

            border-radius: 14px;

            padding: 18px;

            box-shadow:
                0 5px 20px rgba(40, 40, 100, 0.08);

            transition: 0.2s;
        }


        .note-card:hover {
            transform: translateY(-4px);

            box-shadow:
                0 10px 25px rgba(40, 40, 100, 0.13);
        }


        .file-name {
            display: block;

            font-weight: bold;

            font-size: 16px;

            color: #27345e;

            margin-bottom: 15px;

            word-break: break-word;
        }


        .note-image {
            width: 100%;

            height: 210px;

            object-fit: contain;

            background: #f5f6fa;

            border-radius: 9px;

            border: 1px solid #eee;

            margin-bottom: 12px;
        }


        .pdf-preview {
            height: 210px;

            background: #f1f3ff;

            border-radius: 9px;

            display: flex;

            align-items: center;
            justify-content: center;

            flex-direction: column;

            margin-bottom: 12px;
        }


        .pdf-preview span {
            font-size: 45px;
            margin-bottom: 8px;
        }


        .view-button {
            display: inline-block;

            text-decoration: none;

            background: #5046e5;

            color: white;

            padding: 10px 15px;

            border-radius: 7px;

            font-size: 13px;
        }


        .view-button:hover {
            background: #3e35c7;
        }


        .empty-notes {
            text-align: center;

            color: #777;

            grid-column: 1 / -1;

            padding: 30px;
        }


        /* ================= FOOTER ================= */

        footer {
            background: #172043;

            color: white;

            padding: 40px 20px;

            text-align: center;
        }


        footer h3 {
            margin-bottom: 10px;
        }


        footer p {
            color: #c8cce0;

            font-size: 13px;

            margin: 5px;
        }


        /* ================= MOBILE ================= */

        @media (max-width: 850px) {

            header {
                padding: 0 20px;
            }


            nav {
                gap: 12px;
            }


            nav a {
                font-size: 12px;
            }


            .hero {
                flex-direction: column;

                text-align: center;

                padding: 55px 20px;
            }


            .hero-text {
                width: 100%;
            }


            .hero-text h1 {
                font-size: 38px;
            }


            .hero-text p {
                margin-left: auto;
                margin-right: auto;
            }


            .hero-buttons {
                justify-content: center;
            }


            .hero-image {
                width: 100%;
            }


            .features {
                gap: 25px;

                flex-wrap: wrap;
            }


            .notes-container {
                grid-template-columns:
                    repeat(2, 1fr);
            }

        }


        @media (max-width: 600px) {

            header {
                height: auto;

                padding: 15px;

                flex-direction: column;

                gap: 15px;
            }


            nav {
                flex-wrap: wrap;
                justify-content: center;
            }


            .hero-text h1 {
                font-size: 34px;
            }


            .hero-buttons {
                flex-direction: column;
            }


            .primary-btn,
            .secondary-btn {
                width: 100%;
            }


            .note-illustration {
                width: 290px;
                height: 280px;
            }


            .notes-container {
                grid-template-columns: 1fr;
            }


            .features {
                padding: 35px 15px;
            }

        }

    </style>

</head>


<body>


<!-- ================= HEADER ================= -->

<header>

    <div class="logo">

        <div class="logo-icon">
            📖
        </div>

        Handwritten Notes

    </div>


    <nav>

        <a href="/">
            🏠Home
        </a>

        <a href="/notes">
            📝My Notes
        </a>

        <a href="#upload">
           ⬆ Upload
        </a>
        <a href="/login">
         🔐 Login
       </a>

       <a href="/signup" class="signup-btn">
          🙎‍♂️Sign up
        </a>   

        <a href="#upload"
           class="signup-btn">
           🚀 Get Started
        </a>

    </nav>

</header>



<!-- ================= HERO ================= -->

<section class="hero">


    <div class="hero-text">

        <h1>

            Your Handwritten Notes,

            <span>
                Always Accessible
            </span>

        </h1>


        <p>

            Upload, store and share your handwritten notes
            as PDFs. Keep your study material organized
            and accessible anytime, anywhere.

        </p>


        <div class="hero-buttons">

            <a
                href="#upload"
                class="primary-btn"
            >
                Upload Notes
            </a>


            <a
                href="#notes"
                class="secondary-btn"
            >
                Explore Notes
            </a>

        </div>

    </div>



    <div class="hero-image">

        <div class="note-illustration">

            <div class="notebook">

                <h3>
                    Better Notes
                </h3>

                <div class="writing"></div>

                <div class="writing"></div>

                <div class="writing short"></div>

                <div class="writing"></div>

                <div class="writing short"></div>

            </div>


            <div class="pen">
                🖊️
            </div>

        </div>

    </div>


</section>



<!-- ================= FEATURES ================= -->

<section class="features">


    <div class="feature">

        <div class="feature-icon">
            ⬆️
        </div>

        <h3>
            Easy Upload
        </h3>

        <p>
            Upload your notes quickly.
        </p>

    </div>



    <div class="feature">

        <div class="feature-icon">
            🔒
        </div>

        <h3>
            Secure Storage
        </h3>

        <p>
            Keep your study material organized.
        </p>

    </div>



    <div class="feature">

        <div class="feature-icon">
            🌐
        </div>

        <h3>
            Access Anywhere
        </h3>

        <p>
            Open your notes anytime.
        </p>

    </div>


</section>



<!-- ================= UPLOAD ================= -->

<section
    class="upload-section"
    id="upload"
>


    <h2 class="section-title">
        Upload Your Notes
    </h2>


    <p class="section-description">

        Upload handwritten notes as PDF or image.

    </p>



    <div class="upload-box">


        <div class="upload-icon">
            ☁️
        </div>


        <h2>
            Choose Your File
        </h2>


        <p>
            Supported formats:
            PDF, JPG, JPEG, PNG, GIF, WEBP
        </p>



        <form
            action="/upload"
            method="POST"
            enctype="multipart/form-data"
        >

            <input
                type="file"
                name="note"
                accept=".pdf,.jpg,.jpeg,.png,.gif,.webp"
                required
            >


            <br>


            <button
                type="submit"
                class="primary-btn"
            >
                Upload Note
            </button>

        </form>


    </div>


</section>



<!-- ================= NOTES ================= -->

<section
    class="notes-section"
    id="notes"
>


    <div class="notes-header">

        <h2 class="section-title">
            My Notes
        </h2>


        <p class="section-description">
            Access your uploaded handwritten notes.
        </p>

    </div>



    <div class="notes-container">


        {% if files %}


            {% for file in files %}


                <div class="note-card">


                    <span class="file-name">
                        {{ file }}
                    </span>



                    {% if file.lower().endswith(
                        ('.jpg', '.jpeg', '.png', '.gif', '.webp')
                    ) %}


                        <img
                            src="{{ url_for(
                                'uploaded_file',
                                filename=file
                            ) }}"
                            class="note-image"
                            alt="{{ file }}"
                        >


                        <a
                            href="{{ url_for(
                                'uploaded_file',
                                filename=file
                            ) }}"
                            target="_blank"
                            class="view-button"
                        >
                            Open Image
                        </a>



                    {% elif file.lower().endswith('.pdf') %}


                        <div class="pdf-preview">

                            <span>
                                📄
                            </span>

                            <strong>
                                PDF Note
                            </strong>

                        </div>


                        <a
                            href="{{ url_for(
                                'uploaded_file',
                                filename=file
                            ) }}"
                            target="_blank"
                            class="view-button"
                        >
                            View PDF
                        </a>



                    {% else %}


                        <a
                            href="{{ url_for(
                                'uploaded_file',
                                filename=file
                            ) }}"
                            target="_blank"
                            class="view-button"
                        >
                            View Notes
                        </a>


                    {% endif %}


                </div>


            {% endfor %}


        {% else %}


            <div class="empty-notes">

                No notes uploaded yet.

            </div>


        {% endif %}


    </div>


</section>



<!-- ================= FOOTER ================= -->

<footer>


    <h3>
        📖 Handwritten Notes
    </h3>


    <p>
        Your notes, your future.
    </p>


    <p>
        © 2026 Handwritten Notes. All rights reserved.
    </p>


</footer>



</body>

</html>
"""
NOTES_HTML = """
<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport"
          content="width=device-width, initial-scale=1.0">

    <title>My Notes - Handwritten Notes</title>

    <style>

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f7f8ff;
            color: #222;
        }

        header {
            background: white;
            height: 70px;
            padding: 0 6%;

            display: flex;
            align-items: center;
            justify-content: space-between;

            border-bottom: 1px solid #eeeeee;
        }

        .logo {
            font-size: 20px;
            font-weight: bold;
            color: #263b80;
        }

        nav {
            display: flex;
            gap: 25px;
            align-items: center;
        }

        nav a {
            text-decoration: none;
            color: #555;
            font-size: 14px;
        }

        nav a:hover {
            color: #5046e5;
        }

        .active {
            color: #5046e5 !important;
            font-weight: bold;
        }

        .page {
            padding: 45px 7%;
        }

        .top-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 20px;
            margin-bottom: 30px;
        }

        .heading h1 {
            margin: 0 0 8px;
            color: #26345f;
            font-size: 34px;
        }

        .heading p {
            margin: 0;
            color: #777;
        }

        .upload-btn {
            background: #5046e5;
            color: white;
            text-decoration: none;
            padding: 13px 20px;
            border-radius: 8px;
            font-size: 14px;
            font-weight: bold;
        }

        .search-area {
            background: white;
            padding: 18px;
            border-radius: 12px;
            margin-bottom: 30px;

            box-shadow: 0 4px 15px rgba(0,0,0,0.06);
        }

        .search-box {
            width: 100%;
            padding: 14px 16px;

            border: 1px solid #ddd;
            border-radius: 8px;

            font-size: 15px;
            outline: none;
        }

        .search-box:focus {
            border-color: #5046e5;
        }

        .notes-grid {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 22px;
        }

        .note-card {
            background: white;
            border-radius: 14px;
            padding: 15px;

            box-shadow: 0 5px 20px rgba(40,40,100,0.08);

            transition: 0.2s;
        }

        .note-card:hover {
            transform: translateY(-4px);
        }

        .preview {
            height: 210px;
            width: 100%;

            background: #f1f3ff;
            border-radius: 9px;

            display: flex;
            align-items: center;
            justify-content: center;

            overflow: hidden;

            margin-bottom: 15px;
        }

        .preview img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }

        .pdf-icon {
            text-align: center;
        }

        .pdf-icon div {
            font-size: 55px;
        }

        .pdf-icon p {
            color: #777;
            margin-top: 5px;
        }

        .file-name {
            font-weight: bold;
            color: #27345e;

            display: block;

            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;

            margin-bottom: 8px;
        }

        .file-type {
            color: #888;
            font-size: 12px;
            margin-bottom: 14px;
        }

        .open-btn {
            display: inline-block;

            text-decoration: none;

            background: #5046e5;
            color: white;

            padding: 9px 15px;

            border-radius: 7px;

            font-size: 13px;
        }

        .empty {
            background: white;
            padding: 60px 20px;
            text-align: center;
            border-radius: 14px;

            color: #777;
        }

        footer {
            margin-top: 50px;
            background: #172043;
            color: white;
            padding: 30px;
            text-align: center;
        }

        footer p {
            color: #c8cce0;
            font-size: 13px;
        }

        @media (max-width: 850px) {

            .notes-grid {
                grid-template-columns: repeat(2, 1fr);
            }

        }

        @media (max-width: 600px) {

            header {
                height: auto;
                padding: 15px;
                flex-direction: column;
                gap: 15px;
            }

            nav {
                gap: 12px;
            }

            .top-section {
                flex-direction: column;
                align-items: flex-start;
            }

            .heading h1 {
                font-size: 28px;
            }

            .notes-grid {
                grid-template-columns: 1fr;
            }

        }

    </style>

</head>

<body>


<header>

    <div class="logo">
        📖 Handwritten Notes
    </div>

    <nav>

        <a href="/">
            Home
        </a>

        <a href="/notes" class="active">
            My Notes
        </a>

        <a href="/#upload">
            Upload
        </a>

    </nav>

</header>



<div class="page">


    <div class="top-section">

        <div class="heading">

            <h1>
                My Notes
            </h1>

            <p>
                Manage and access all your uploaded notes in one place.
            </p>

        </div>


        <a
            href="/#upload"
            class="upload-btn"
        >
            + Upload New Note
        </a>

    </div>



    <div class="search-area">

        <input
            type="text"
            id="searchInput"
            class="search-box"
            placeholder="🔍 Search your notes..."
            onkeyup="searchNotes()"
        >

    </div>



    {% if files %}


        <div class="notes-grid" id="notesGrid">


            {% for file in files %}


                <div
                    class="note-card"
                    data-name="{{ file|lower }}"
                >


                    <div class="preview">


                        {% if file.lower().endswith(
                            ('.jpg', '.jpeg', '.png', '.gif', '.webp')
                        ) %}


                            <img
                                src="{{ url_for(
                                    'uploaded_file',
                                    filename=file
                                ) }}"
                                alt="{{ file }}"
                            >


                        {% elif file.lower().endswith('.pdf') %}


                            <div class="pdf-icon">

                                <div>
                                    📄
                                </div>

                                <p>
                                    PDF Document
                                </p>

                            </div>


                        {% else %}


                            <div class="pdf-icon">

                                <div>
                                    📝
                                </div>

                                <p>
                                    Note
                                </p>

                            </div>


                        {% endif %}


                    </div>



                    <span class="file-name">
                        {{ file }}
                    </span>


                    <div class="file-type">

                        {% if file.lower().endswith('.pdf') %}

                            PDF

                        {% else %}

                            Image

                        {% endif %}

                    </div>



                    <a
                        href="{{ url_for(
                            'uploaded_file',
                            filename=file
                        ) }}"
                        target="_blank"
                        class="open-btn"
                    >
                        Open Note
                    </a>
            <a
              href="{{ url_for('delete_file', filename=file) }}"
              class="delete-btn"
              onclick="return confirm('Are you sure you want to delete this note?');"
              >
              delete
              </a>

                </div>


            {% endfor %}


        </div>


    {% else %}


        <div class="empty">

            <h2>
                📚 No Notes Yet
            </h2>

            <p>
                Upload your first handwritten note to see it here.
            </p>

            <br>

            <a
                href="/#upload"
                class="upload-btn"
            >
                Upload Note
            </a>

        </div>


    {% endif %}


</div>



<footer>

    <h3>
        📖 Handwritten Notes
    </h3>

    <p>
        Your notes, your future.
    </p>

</footer>



<script>

function searchNotes() {

    let input =
        document.getElementById("searchInput")
        .value
        .toLowerCase();

    let cards =
        document.querySelectorAll(".note-card");


    cards.forEach(function(card) {

        let name =
            card.getAttribute("data-name");


        if (name.includes(input)) {

            card.style.display = "";

        } else {

            card.style.display = "none";

        }

    });

}

</script>


</body>

</html>
"""
# ================= LOGIN =================

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if (username == "admin" and password == "1234") or users.get(username)== password:
            return redirect(url_for("home"))

        return """
        <h2>Invalid username or password</h2>
        <a href="/login">Try Again</a>
        """

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login - Handwritten Notes</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f8f9ff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .login-box {
                background: white;
                padding: 35px;
                width: 320px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }

            h2 {
                text-align: center;
                color: #263b80;
            }

            input {
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-sizing: border-box;
            }

            button {
                width: 100%;
                padding: 12px;
                background: #263b80;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }

            .signup {
                text-align: center;
                margin-top: 15px;
            }
        </style>
    </head>

    <body>

        <div class="login-box">

            <h2>Login</h2>

            <form method="POST">

                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    required
                >

                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    required
                >

                <button type="submit">
                    Login
                </button>

            </form>

            <div class="signup">
                Don't have an account?
                <a href="/signup" class="signup-btn">
                Sign Up
                </a>
            </div>

        </div>

    </body>
    </html>
    """


# ================= SIGN UP =================

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        users[username] = password

        return redirect(url_for("login"))

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sign Up - Handwritten Notes</title>

        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f8f9ff;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .signup-box {
                background: white;
                padding: 35px;
                width: 320px;
                border-radius: 15px;
                box-shadow: 0 5px 20px rgba(0,0,0,0.15);
            }

            h2 {
                text-align: center;
                color: #263b80;
            }

            input {
                width: 100%;
                padding: 12px;
                margin: 10px 0;
                border: 1px solid #ddd;
                border-radius: 8px;
                box-sizing: border-box;
            }

            button {
                width: 100%;
                padding: 12px;
                background: #263b80;
                color: white;
                border: none;
                border-radius: 8px;
                cursor: pointer;
            }

            .login {
                text-align: center;
                margin-top: 15px;
            }
        </style>
    </head>

    <body>

        <div class="signup-box">

            <h2>Create Account</h2>

            <form method="POST">

                <input
                    type="text"
                    name="username"
                    placeholder="Username"
                    required
                >

                <input
                    type="password"
                    name="password"
                    placeholder="Password"
                    required
                >

                <button type="submit">
                    Sign Up
                </button>

            </form>

            <div class="login">
                Already have an account?
                <a href="/login">Login</a>
            </div>

        </div>

    </body>
    </html>
    """
      
# ================= HOME =================

@app.route("/")
def home():

    files = []

    if os.path.exists(UPLOAD_FOLDER):

        files = os.listdir(UPLOAD_FOLDER)

    files.sort(reverse=True)


    return render_template(
       "index.html",
        files=files
    )

@app.route("/notes")
def notes():
    file = []
    if os.path.exists(UPLOAD_FOLDER):
        files = os.listdir(UPLOAD_FOLDER)

    files.sort(reverse=True)
    return render_template(
        NOTES_HTML,
        files=files
    )    
    

# ================= UPLOAD =================

@app.route("/upload", methods=["POST"])
def upload():

    if "note" not in request.files:

        return redirect(
            url_for("home")
        )


    file = request.files["note"]


    if file.filename == "":

        return redirect(
            url_for("home")
        )


    if allowed_file(file.filename):

        filename = secure_filename(
            file.filename
        )


        file.save(
            os.path.join(
                app.config["UPLOAD_FOLDER"],
                filename
            )
        )


    return redirect(
        url_for("home")
    )



# ================= OPEN UPLOADED FILE =================

@app.route("/uploads/<filename>")
def uploaded_file(filename):

    return (
        app.config["UPLOAD_FOLDER"],
        filename
    )
# delete file
@app.route("/delete/<filename>")
def delete_file(filename):

    file_path =os.path.join(
        app.config["UPLOAD_FOLDER"],
        filename
    )
     
    if os.path.exists(file_path):
        os.remove(file_path)

    return redirect(url_for("notes"))  
@app.route("/google971a16a12f2883d8.html")
def google_verification():
    return send_from_directory("." "google971a16a12f2883d8.html")

# ================= RUN =================

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000, debug=True)