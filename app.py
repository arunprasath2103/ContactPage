from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        
        # Handle form submission (you can print, save, or send the data here)
        print(f"Name: {name}, Email: {email}, Message: {message}")
        
        return redirect(url_for("thank_you"))
    
    return render_template("contact.html")

@app.route("/thank-you")
def thank_you():
    return "Thank you for contacting us!"

if __name__ == "__main__":
    app.run(debug=True)