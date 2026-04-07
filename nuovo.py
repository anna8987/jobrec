import pandas as pd
import numpy as np

# Carico il dataset
df = pd.read_csv(r'ds\job_recommendation_dataset.csv')

# 1. Definiamo dei "Profili" coerenti per creare i Cluster
profiles = {
    'Tech': {
        'industries': ['Software', 'IT Services'],
        'skills': ['Python', 'Java', 'AWS', 'SQL', 'Machine Learning', 'React'],
        'base_salary': 70000
    },
    'Healthcare': {
        'industries': ['Healthcare', 'Pharmaceuticals'],
        'skills': ['Patient Care', 'Nursing', 'Medical Research', 'Diagnostics'],
        'base_salary': 60000
    },
    'Finance': {
        'industries': ['Finance', 'Banking'],
        'skills': ['Financial Modeling', 'Risk Analysis', 'SQL', 'Excel'],
        'base_salary': 75000
    },
    'Education': {
        'industries': ['Education', 'EdTech'],
        'skills': ['Curriculum Design', 'Pedagogy', 'E-learning'],
        'base_salary': 40000
    }
}

# 2. Funzione per rendere i dati coerenti
def apply_logic(row):
    # Scegliamo un profilo casuale per ogni riga per creare gruppi distinti
    profile_name = np.random.choice(list(profiles.keys()))
    prof = profiles[profile_name]
    
    # Assegniamo industria e skill coerenti
    row['Industry'] = np.random.choice(prof['industries'])
    num_skills = np.random.randint(1, 4)
    row['Required Skills'] = ", ".join(np.random.choice(prof['skills'], num_skills, replace=False))
    
    # Logica Salariale: Base + Bonus Esperienza + Noise
    exp_multiplier = {'Entry Level': 1.0, 'Mid Level': 1.5, 'Senior Level': 2.2}
    base = prof['base_salary']
    multiplier = exp_multiplier.get(row['Experience Level'], 1.0)
    
    # Aggiungiamo un po' di varianza casuale ma controllata
    random_noise = np.random.normal(1, 0.1) 
    row['Salary'] = round(base * multiplier * random_noise, -2)
    
    return row

# Applichiamo la trasformazione
df = df.apply(apply_logic, axis=1)

# Salviamo il nuovo dataset
df.to_csv('job_recommendation_structured.csv', index=False)
print("Dataset modificato con successo!")