## Opdracht D: automatisatie
#### Kevin Provoost - Simlab 2

### Vraag
Elke student kan één van volgende automatisatieopdrachten kiezen:
•	de automatisatie van de creatie van gebruikersaccounts via een script (alleen mogelijk als dit nodig is naast de Linux systeemaccounts) (minstens een account kunnen aanmaken en verwijderen via CLI oproepbaar script)

### Oplossing
Ik heb gekozen voor het managen van user accounts via geautomatiseerde ansible playbooks.
Via create_users.yml kan je een gebruiker aanmaken via een zelfgekozen gebruikersnaam & wachtwoord.
Met delete_users.yml krijg je een lijst van users waaruit je een gebruikersnaam kan kiezen om te verwijderen.