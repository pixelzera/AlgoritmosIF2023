 from dataclasses import dataclass
 
 
  # Anotação: @algumacoisa
  # classes iniciam com letra maiúscula
   @dataclass
   class Data:
       dia: int
       mes: int
       ano: int
  
    
  @dataclass
  class Aluno:
        matricula: str
        nome: str
        sexo: str
        data_nascimento: str