import os
import speech_recognition as sr

# Inicializa o reconhecedor
recognizer = sr.Recognizer()

# Função para capturar e salvar o áudio em formato WAV apenas
def listen_and_save(prompt="Diga algo:", lang="pt-BR"):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(prompt)
        audio = recognizer.listen(source)
        
        try:
            # Tentar reconhecer o áudio
            recognized_text = recognizer.recognize_google(audio, language=lang).lower()
            return recognized_text, audio
        except sr.UnknownValueError:
            print("Aurora: Não consegui entender o que você disse.")
            return None, None
        except sr.RequestError as e:
            print(f"Aurora: Erro no serviço de reconhecimento de voz: {e}")
            return None, None

# Função para o cadastro do colaborador
def register_collaborator():
    print("Aurora: Por favor, diga seu nome completo.")
    
    # Capturar o nome completo do colaborador
    name, audio = listen_and_save()
    if name and audio:
        formatted_name = name.replace(" ", "_")
        folder_path = r"C:\Users\rmarv\OneDrive\Área de Trabalho\Sevent\Colaboradores_Reconhecimento"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, f"{formatted_name}.wav")
        
        # Salvar o áudio como WAV
        with open(file_path, "wb") as f:
            f.write(audio.get_wav_data())
        
        print(f"Aurora: Cadastro concluído {name.capitalize()}. Até logo!")
        print(f"Áudio salvo em {file_path}")
        return

# Função principal para o fluxo de conversação
def recognize_speech():
    # Esperar o usuário iniciar com "Oi Aurora"
    while True:
        command, _ = listen_and_save(prompt="Diga 'Oi Aurora' para começar:")
        if command and "oi aurora" in command:
            print("Aurora: Olá, como posso te ajudar hoje?")
            break

    # Continuar a partir da resposta do usuário
    user_response, _ = listen_and_save(prompt="Você: ")
    
    if user_response and "cadastramento de colaborador" in user_response:
        register_collaborator()
    else:
        print("Aurora: Desculpe, não entendi sua solicitação.")

# Chama a função para iniciar o reconhecimento de voz
recognize_speech()