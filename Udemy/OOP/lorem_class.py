from lorem_text import lorem
class Lorem:
    def __init__(self):
        self.generate_lorem(1)
    def generate_lorem(self, length):
      sentence_list = lorem.paragraphs(length)
      print(sentence_list)
        
        