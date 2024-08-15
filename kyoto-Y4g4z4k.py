import speech_recognition as sr
import pyttsx3
import wikipedia 
import datetime
import webbrowser

# Inicialização do Recognizer
recognizer = sr.Recognizer()

# Inicialização do Text to Speech
engine = pyttsx3.init()

# Função para falar texto
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Função para reconhecer voz
def recognize_speech():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Escutando...")
        audio = recognizer.listen(source)

        try:
            print("Reconhecendo...")
            query = recognizer.recognize_google(audio, language='pt-BR')
            print("Você disse:", query)
            return query.lower()
        except sr.UnknownValueError:
            print("Não manjei o que você disse.")
            return ""
        except sr.RequestError as e:
            print("Erro ao se comunicar com o serviço de reconhecimento de voz; {0}".format(e))
            return ""

# Função para adicionar tarefas à lista
def add_task(task):
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")

# Função para pesquisar na web
def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

# Função para definir um lembrete
def set_reminder(reminder):
    now = datetime.datetime.now()
    speak(f"Lembrete definido para {reminder}")
    print(f"Lembrete definido para {reminder} em {now.strftime('%H:%M')}")

# Função para fornecer dicas básicas de segurança cibernética
def cybersecurity_tips():
    speak("Aqui estão algumas dicas básicas de segurança cibernética: Mantenha seus programas e sistemas operacionais atualizados regularmente. Use senhas fortes e únicas para suas contas. Tenha cuidado ao clicar em links suspeitos ou baixar anexos de e-mails desconhecidos. E, por fim, faça backup regularmente dos seus dados importantes.")
    
# Função principal
def main():
    speak("Olá! Sr.Fractal, posso ajudá-lo ?")
    while True:
        query = recognize_speech()

        if "sair" in query:
            speak("Estou indo embora por favor não implora por que homen não chora ")
            break

        if "adicionar tarefa" in query:
            speak("O que você gostaria de adicionar à sua lista de tarefas?")
            task = recognize_speech()
            add_task(task)
            speak("Tarefa adicionada com sucesso!")

        elif "pesquisar na web" in query:
            speak("O que você gostaria de pesquisar?")
            search_query = recognize_speech()
            search_web(search_query)

        elif "definir lembrete" in query:
            speak("O que você gostaria de lembrar?")
            reminder = recognize_speech()
            set_reminder(reminder)

        elif "dicas de segurança cibernética" in query:
            cybersecurity_tips()

if __name__ == "__main__":
    main()
