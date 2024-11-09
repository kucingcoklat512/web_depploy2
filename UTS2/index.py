# Nama  : Mohammad Calvin Wiranata
# NIM   : 21.83.0667
# Kelas : S1 21-TK-02

# Tugas 6: Model View Controller (MVC)

from config import app, db
from routes.User_bp import user_bp
from routes.Level_bp import level_bp

app.register_blueprint(user_bp)
app.register_blueprint(level_bp)

db.create_all()

"""if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)"""