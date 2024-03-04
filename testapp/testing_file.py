class Question:
    def __init__(self, question_text, answers: dict, correct_answer):
        self.question_text = question_text
        self.answers = answers
        self.correct_answer = correct_answer


questions = ['What does "hola" mean in English?', 'How do you say "thank you" in Spanish?',
             'Which phrase means "How are you?" in Spanish?', 'What is the Spanish word for "house"?',
             'How do you say "I am hungry" in Spanish?', 'What does "perro" mean in English?',
             'Which phrase means "Where is the bathroom?" in Spanish?', 'How do you say "I love you" in Spanish?',
             'What is the Spanish term for "school"?', 'How do you say "goodbye" in Spanish?']

probable_answers = [
    {'a': 'Hello', 'b': 'Goodbye', 'c': 'Thank you', 'd': 'Please'},
    {'a': 'Por favor', 'b': 'Gracias', 'c': 'Perdón', 'd': 'Lo siento'},
    {'a': '¿Cómo te llamas?', 'b': '¿Cómo estás?', 'c': '¿Qué hora es?', 'd': '¿Dónde está el baño?'},
    {'a': 'Casa', 'b': 'Coche', 'c': 'Perro', 'd': 'Comida'},
    {'a': 'Tengo hambre', 'b': ' Tengo sed', 'c': 'Tengo frío', 'd': 'Tengo calor'},
    {'a': 'Dog', 'b': 'Cat', 'c': 'Fish', 'd': 'Bird'},
    {'a': '¿Cómo te llamas?', 'b': '¿Dónde está el baño?', 'c': '¿Qué hora es?', 'd': '¿Cuánto cuesta?'},
    {'a': 'Te amo', 'b': 'Te quiero', 'c': 'Te extraño', 'd': 'Te odio'},
    {'a': 'Casa', 'b': 'Escuela', 'c': 'Parque', 'd': 'Trabajo'},
    {'a': 'Hola', 'b': 'Buenas noches', 'c': 'Adiós', 'd': ' Por favor'}]

correct_answers = ['a', 'b', 'b', 'a', 'a', 'a', 'b', 'a', 'b', 'c']

all_questions = []

for i in range(10):
    all_questions.append(Question(questions[i], probable_answers[i], correct_answers[i]))

user_points = 0

# for i in all_questions:
#     print(i.question_text)
#     for k, v in i.answers.items():
#         print(k, v)
#     user_answer = input('Enter the correct answer: ')
#     print()
#     if user_answer == i.correct_answer:
#         user_points += 1
#
#
# if user_points >= 7:
#     print('You have passed the test!')


