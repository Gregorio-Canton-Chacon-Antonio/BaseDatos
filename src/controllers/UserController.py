from models.UserModel import UsuarioModel
from models.schemasModel import UsuarioSchema 
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_usuario(self, nombre, email, password):
        try: 
            nuevo_usuario = UsuarioSchema(nombre=nombre, email=email, password=password)
            success = self.model.registrar(nuevo_usuario)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']

    def login(self, email, password):
        if not email or not password:
            return None, "Correo y contraseña son obligatorios"
        user = self.model.validar_login(email, password)
        if user:
            return user, "Login exitoso"
        return None, "Correo o contraseña incorrectos"