import speech_recognition as sr

# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Função para capturar e reconhecer a voz
def listen_and_recognize(prompt="Diga algo:", lang="pt-BR"):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(prompt)
        audio = recognizer.listen(source)
        try:
            return recognizer.recognize_google(audio, language=lang).lower()
        except sr.UnknownValueError:
            print("Aurora: Não consegui entender o que você disse.")
            return None
        except sr.RequestError as e:
            print(f"Aurora: Erro no serviço de reconhecimento de voz: {e}")
            return None

# Função principal para o fluxo de conversação
def recognize_speech():
    while True:
        command = listen_and_recognize("Aguardando o comando 'Oi Aurora'...")
        if command and "oi aurora" in command:
            print("Aurora: Oi")
            break
    
    while True:
        user_input = listen_and_recognize("Ajustando o ruído ambiente... Diga algo:")
        if user_input:
            if "obrigado aurora" in user_input:
                print("Aurora: Eu quem agradeço você aqui.")
                break
            else:
                # Transcreve o que foi dito
                print(f"Aurora transcreve: {user_input}")

# Chama a função para iniciar o reconhecimento de voz
recognize_speech()