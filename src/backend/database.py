"""
Configuração e setup do database MongoDB para a API da Mergington High School
"""

from pymongo import MongoClient
from argon2 import PasswordHasher

# Conectar ao MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['mergington_high']
activities_collection = db['activities']
teachers_collection = db['teachers']

# Methods
def hash_password(password):
    """Hash da password usando Argon2"""
    ph = PasswordHasher()
    return ph.hash(password)

def init_database():
    """Inicializar database se estiver vazio"""

    # Inicializar activities se estiver vazio
    if activities_collection.count_documents({}) == 0:
        for name, details in initial_activities.items():
            activities_collection.insert_one({"_id": name, **details})
            
    # Inicializar contas de teacher se estiver vazio
    if teachers_collection.count_documents({}) == 0:
        for teacher in initial_teachers:
            teachers_collection.insert_one({"_id": teacher["username"], **teacher})

# Database inicial se estiver vazio
initial_activities = {
    "Chess Club": {
        "description": "Aprender estratégias e competir em torneios de xadrez",
        "schedule": "Segundas e sextas, 15:15 - 16:45",
        "schedule_details": {
            "days": ["Monday", "Friday"],
            "start_time": "15:15",
            "end_time": "16:45"
        },
        "max_participants": 12,
        "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
    },
    "Programming Class": {
        "description": "Aprender fundamentos de programação e construir projetos de software",
        "schedule": "Terças e quintas, 7:00 - 8:00",
        "schedule_details": {
            "days": ["Tuesday", "Thursday"],
            "start_time": "07:00",
            "end_time": "08:00"
        },
        "max_participants": 20,
        "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
    },
    "Morning Fitness": {
        "description": "Treinamento físico e exercícios matinais",
        "schedule": "Segundas, quartas, sextas, 6:30 - 7:45",
        "schedule_details": {
            "days": ["Monday", "Wednesday", "Friday"],
            "start_time": "06:30",
            "end_time": "07:45"
        },
        "max_participants": 30,
        "participants": ["john@mergington.edu", "olivia@mergington.edu"]
    },
    "Soccer Team": {
        "description": "Junte-se ao time de futebol da escola e compita em partidas",
        "schedule": "Terças e quintas, 15:30 - 17:30",
        "schedule_details": {
            "days": ["Tuesday", "Thursday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 22,
        "participants": ["liam@mergington.edu", "noah@mergington.edu"]
    },
    "Basketball Team": {
        "description": "Praticar e competir em torneios de basquete",
        "schedule": "Quartas e sextas, 15:15 - 17:00",
        "schedule_details": {
            "days": ["Wednesday", "Friday"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["ava@mergington.edu", "mia@mergington.edu"]
    },
    "Art Club": {
        "description": "Explorar várias técnicas de arte e criar obras-primas",
        "schedule": "Quintas, 15:15 - 17:00",
        "schedule_details": {
            "days": ["Thursday"],
            "start_time": "15:15",
            "end_time": "17:00"
        },
        "max_participants": 15,
        "participants": ["amelia@mergington.edu", "harper@mergington.edu"]
    },
    "Drama Club": {
        "description": "Atuar, dirigir e produzir peças e apresentações",
        "schedule": "Segundas e quartas, 15:30 - 17:30",
        "schedule_details": {
            "days": ["Monday", "Wednesday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 20,
        "participants": ["ella@mergington.edu", "scarlett@mergington.edu"]
    },
    "Math Club": {
        "description": "Resolver problemas desafiadores e se preparar para competições de matemática",
        "schedule": "Terças, 7:15 - 8:00",
        "schedule_details": {
            "days": ["Tuesday"],
            "start_time": "07:15",
            "end_time": "08:00"
        },
        "max_participants": 10,
        "participants": ["james@mergington.edu", "benjamin@mergington.edu"]
    },
    "Debate Team": {
        "description": "Desenvolver habilidades de falar em público e argumentação",
        "schedule": "Sextas, 15:30 - 17:30",
        "schedule_details": {
            "days": ["Friday"],
            "start_time": "15:30",
            "end_time": "17:30"
        },
        "max_participants": 12,
        "participants": ["charlotte@mergington.edu", "amelia@mergington.edu"]
    },
    "Weekend Robotics Workshop": {
        "description": "Construir e programar robôs em nosso workshop de última geração",
        "schedule": "Sábados, 10:00 - 14:00",
        "schedule_details": {
            "days": ["Saturday"],
            "start_time": "10:00",
            "end_time": "14:00"
        },
        "max_participants": 15,
        "participants": ["ethan@mergington.edu", "oliver@mergington.edu"]
    },
    "Science Olympiad": {
        "description": "Preparação para competição de ciências de fim de semana para eventos regionais e estaduais",
        "schedule": "Sábados, 13:00 - 16:00",
        "schedule_details": {
            "days": ["Saturday"],
            "start_time": "13:00",
            "end_time": "16:00"
        },
        "max_participants": 18,
        "participants": ["isabella@mergington.edu", "lucas@mergington.edu"]
    },
    "Sunday Chess Tournament": {
        "description": "Torneio semanal para jogadores sérios de xadrez com rankings",
        "schedule": "Domingos, 14:00 - 17:00",
        "schedule_details": {
            "days": ["Sunday"],
            "start_time": "14:00",
            "end_time": "17:00"
        },
        "max_participants": 16,
        "participants": ["william@mergington.edu", "jacob@mergington.edu"]
    }
}

initial_teachers = [
    {
        "username": "mrodriguez",
        "display_name": "Ms. Rodriguez",
        "password": hash_password("art123"),
        "role": "teacher"
     },
    {
        "username": "mchen",
        "display_name": "Mr. Chen",
        "password": hash_password("chess456"),
        "role": "teacher"
    },
    {
        "username": "principal",
        "display_name": "Principal Martinez",
        "password": hash_password("admin789"),
        "role": "admin"
    }
]

