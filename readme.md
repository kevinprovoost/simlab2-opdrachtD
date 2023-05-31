## Opdracht D: automatisatie
#### Kevin Provoost - Simlab 2
<br>


### Opdracht
Automatisatie van de creatie van gebruikersaccounts via een script (alleen mogelijk als dit nodig is naast de Linux systeemaccounts). Minstens een account kunnen aanmaken en verwijderen via CLI oproepbaar script.<br>
<br>
### Oplossing
Managen van user accounts via geautomatiseerde ansible playbooks.  

Via create_users.yml kan je een gebruiker aanmaken via een zelfgekozen gebruikersnaam & wachtwoord.
```bash
ansible-playbook create_users.yml -K
```

Met delete_users.yml krijg je een lijst van users waaruit je een gebruikersnaam kan kiezen om te verwijderen.  
```bash
ansible-playbook delete_users.yml -K
```