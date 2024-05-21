from flask import Flask,render_template,url_for, flash, redirect
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

# Pour assurer la securité du site
app.config[
    "SECRET_KEY"
] = "62913a7dac3933f87a84626fcdeaaf9e2653f0a000843efd9bf2b31ba4767402"

films =[{ 
    'poster': 'kp.jpeg',
    'title': 'Kung Fu Panda 4',
    },
    { 
    'poster':'mig.jpeg',
    'title' : 'Migration',
    },
    { 
    'poster': 'toy.jpeg',
    'title' : 'Toy Story', 
    }
    ]

@app.route("/")
@app.route("/home")
def home(): 
    return render_template('home.html', films=films) # cela correspond à notre boucle

@app.route("/about")
def about():
    return render_template('about.html',title = 'Accueil') # title -> pour notre titre de de page

# chemin pour l'onglet inscription
@app.route("/register",methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Compte créé avec succès pour {form.username.data}", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

# chemin pour l'onglet connexion
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit(): 
        if (
            form.email.data == "omar@email.com" # un exemple dd'adresse mail
            and form.password.data == "PASS!!word123"
        ):
            flash("Vous avez été connecté !", "success")
            return redirect(url_for("home"))
        else:
            flash("Connexion non réussie. Veuillez vérifier vos informations d'identification", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)