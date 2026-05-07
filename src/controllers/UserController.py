from models.UsersModel import UsuarioModel
from models.schemasModel import UsuarioShema
from pydantic import ValidationError

class AuthController:
    def __init__(self):
        self.model = UsuarioModel()

    def registrar_Usuario(self, nombre, apellido, email, contrasena, telefono, fecha):
        try:
            nuevo = UsuarioShema(nombre=nombre, apellido=apellido, email=email,
                                 password=contrasena, telefono=telefono, fecha=fecha)
            success = self.model.registrar(nuevo)
            return success, "Usuario creado correctamente"
        except ValidationError as e:
            return False, e.errors()[0]['msg']
        except Exception as e:
            return False, str(e)

    def login(self, email, password):
        try:
            user = self.model.validar_login(email, password)
            return (user, "Login correcto") if user else (False, "Credenciales incorrectas")
        except Exception as e:
            return False, str(e)