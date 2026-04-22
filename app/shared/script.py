from app.models.context import Context

def handle_contexts(context: Context) -> str:
    match context:
        case Context.WAITING_MESSAGE_1:
            return """Olá, bem-vindo à Mitsunaka Engenharia! 🏢"""
        case Context.WAITING_MESSAGE_2:
            return """Qual o tamanho da reforma (em m²)? 🤔"""
        
        case _:
            return """"""