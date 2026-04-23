from app.models.context import Context
from app.shared.ai_requests import gpt_request
from app.repository.message_repository import MessageRepository

def handle_contexts(context: Context, user, repo: MessageRepository) -> str:
    match context:
        case Context.WAITING_MESSAGE_1:
            return """Olá, bem-vindo à Mitsunaka Engenharia! 🏢\nQual o seu nome? 🧐"""
        case Context.WAITING_MESSAGE_2:
            return """Qual o tamanho da reforma (em m²)? 🤔"""
        case Context.WAITING_MESSAGE_3:
            return """Escreva brevemente qual é o tipo da sua reforma (reforma completa no banheiro, trocar piso da cozinha, etc.) 🤔"""
        case Context.WAITING_MESSAGE_4:
            return """4"""
        case Context.WAITING_MESSAGE_5:
            return gpt_request(
                repo.get_by_context(user, Context.WAITING_MESSAGE_3).message_content,
                repo.get_by_context(user, Context.WAITING_MESSAGE_4).message_content,
            )
        
        case _:
            return """"""