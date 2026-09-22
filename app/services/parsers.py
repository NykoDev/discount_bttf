from app.models.movie import Movie

class Parser:
    """Parseur pour extraire les titres de films d'une chaîne de caractères (un titre par ligne).
    construit une liste d'objets Movie à partir de l'entrée fournie."""
    def __init__(self, inputText: str):
        self.inputText = inputText

    def parse(self):
        
        inputList = [line.strip().lower() for line in self.inputText.splitlines() if line]
        print(inputList)
        return [Movie(title) for title in inputList]