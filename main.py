from flask import Flask, render_template, Blueprint, request
from controllers import usuario_controller, cliente_controller, producto_controller, venta_controller
from database import db

# Crea la aplicación principal
app = Flask(__name__)

# Rutas principales de la aplicación
@app.route('/')
def home():
  return render_template('index.html')

@app.route('/quienes')
def quienes():
  return render_template('quienes.html')

@app.route('/servicios')
def servicios():
  return render_template('servicios.html')

@app.route('/noticias')
def noticias():
  return render_template('noticias.html')

@app.route('/contactos')
def contactos():
  return render_template('contactos.html')

@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/iniciar')
def iniciar():
  return render_template('iniciar.html')

@app.route('/base')
def base():
  return render_template('usuarios.html')

# ruuuuuuuuuuuuuuuuuuuun

# Configura la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ventas.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la base de datos
db.init_app(app)

# Registra los blueprints de los controladores
app.register_blueprint(usuario_controller.usuario_bp)
app.register_blueprint(cliente_controller.cliente_bp)
app.register_blueprint(producto_controller.producto_bp)
app.register_blueprint(venta_controller.venta_bp)

# Crea el Blueprint para "admin", con la carpeta templates correcta
admin_app = Blueprint('admin_app', __name__, template_folder='templates')

# Procesador de contexto
@app.context_processor
def inject_activar_path():
  def is_activado(path):
    return 'active' if request.path == path else ''
  return dict(is_activado=is_activado)

if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(debug=True)