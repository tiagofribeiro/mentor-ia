from langchain_openai import ChatOpenAI
from .settings import OPENROUTER_API_KEY, OPENROUTER_BASE_URL, OPENROUTER_MODEL

model = ChatOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url=OPENROUTER_BASE_URL,
    model=OPENROUTER_MODEL,
)

def send_prompt(message, system_prompt=None, history=None):
    """
    Envia uma mensagem ao modelo (com o histórico) e retorna a resposta.
    """
    
    # TODO: avaliar melhor opção para memória
    messages = [] # history if history else []

    if system_prompt and (not messages or messages[0].get("role") != "system"):
        messages.insert(0, {"role": "system", "content": system_prompt})
    messages.append({"role": "user", "content": message})
    response = model.invoke(messages)

    return response.content