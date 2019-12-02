class Aluno(BaseModel):
    matricula = PrimarykeyField()
    escolaridade = CharField()
    caracteristica = Foreignkey(Pessoa)

class Endereco(BaseModel):
    rua = CharField()
    num = CharField()
    CEP = PrimarykeyField()
    cidade = CharField()
    bairro = CharField()

class Pessoa(BaseModel):
    nome = CharField()
    CPF = PrimarykeyField()
    endereco= Foreignkey(Endereco)
    sexo= CharField()

class Professor(BaseModel):
    registro = PrimarykeyField()
    especialidade = CharField()
    escolaridade = CharField()
    caracteristica = Foreignkey(Pessoa)

class Escola(BaseModel):
    nome = PrimarykeyField()
    endereco= Foreignkey(Endereco)

class Turma(BaseModel):
    nomturma = PrimarykeyField()
    sala = ForeignkeyField(Sala)  
    numalunos = CharField()
    turno = CharField()
    datinicio = CharFieldField()
    datfim = CharFieldField()
    curso = Foreignkey(Curso)
    aluno = Foreignkey(Aluno)
    professor = Foreignkey(Professor)

class Sala(BaseModel):
    num = PrimarykeyField()  
    capacidade= CharField()
    escola = Foreignkey(escola)

class Curso(BaseModel):
    nome = PrimarykeyField()  
    cargahor = CharField()
    area = CharField()
    materia = Foreignkey(Materia)

class Materia(BaseModel):
    nome = PrimarykeyField()
    cargahor = CharField()
    avaliacao = Foreignkey(Avaliacao)

class Avaliacao(BaseModel):
    nome = PrimarykeyField()
    peso = CharField()
    tipo = CharField()


av1= Avaliacao.create(nome= "P1 LINGUAS", peso= "5", tipo= "prova")
materia1= Materia.create(nome= "diccao", cargahor= "20 horas", materia= av1)
curso1= Curso.create(nome= "Ingles", cargahor= "600 horas", area= "linguas", materia= materia1)
ende1= Endereco.create(rua= "2250", num= "340", CEP= "89.330-000", cidade= "Blumenau", bairro= "Itopava Seca")
ende2= Endereco.create(rua= "Paulina", num= "180", CEP= "89.330-000", cidade= "Blumenau", bairro= "Itopava Seca")
ende3= Endereco.create(rua= "Flamengo", num= "490", CEP= "89.330-000", cidade= "Blumenau", bairro= "Itopava Seca")
escola1= Escola.create(nome= "Fisk entendi", endereco= ende1)
sala1= Sala.create(num= "001", capacidade= "40", escola= escola1)
pessoa1= Pessoa.create(nome= "Matheus", CPF= "099.570.532-21", endereco= ende2, sexo= "masculino")
pessoa2= Pessoa.create(nome= "Rafael", CPF= "083.923.483-29", endereco= ende3, sexo= "masculino")
aluno1= Aluno.create(matricula= "2019.55", escolaridade= "Ensino Medio", caracteristica= pessoa1)
professor1= Professor.create(especialidade= "Linguas", escolaridade= "Doutorado", caracteristica= pessoa2, matricula= "2007.04")
turma= Turma.create(nomturma = "Turma 001", sala= sala1, numalunos= "33", turno= "vespertino", datinicio= "19/04/2019", datfim= "19/11/2019", curso= curso1, aluno= aluno1, professor= professor1)


{
    "turma" : {
        "nomturma" : "Turma 001",
        "sala" : {
            "num" : "001",
            "capacidade" : "40",
            "escola" : {
                "nome" : "Fisk entendi",
                "endereco" : {
                    "rua" : "2250",
                    "num" : "340",
                    "CEP" : "89.330-000",
                    "cidade" : "Blumanau",
                    "bairro" : "Itopava Seca",
                    }
                }
            }
        "numalunos" : "33",
        "turno" : "vespertino",
        "datinicio" : "19/04/2019",
        "datfim" : "19/11/2019",
        "curso" : {
            "nome" : "Ingles",
            "cargahor" : "600 horas",
            "area" : "Linguas",
            "materia" : {
                "nome" : "diccao",
                "cargahor" : "20 horas",
                "materia" : {
                    "nome" = "P1 LINGUAS",
                    "peso" : "5",
                    "tipo" : "prova",
                    }
                }
            }    
        "aluno" : {
           "matricula" : "2019.55",
           "escolaridade" : "Ensino Medio",
           "caracteristica" : {
                "nome" : "Matheus",
                "CPF" : "099.570.532-21",
                "endereco" : {
                    "rua" : "Paulina",
                    "num" : "180",
                    "CEP" : "89.330-000",
                    "cidade" : "Blumanau",
                    "bairro" : "Itopava Seca",
                    }
                "sexo" : "Masculino",
                }
            }
        "professor" : {
           "especialidade" : "Linguas",
           "escolaridade" : "Doutorado",
           "caracteristica" : {
                "nome" : "Rafael",
                "CPF" : "083.923.483-29",
                "endereco" : {
                    "rua" : "Flamengo",
                    "num" : "490",
                    "CEP" : "89.330-000",
                    "cidade" : "Blumanau",
                    "bairro" : "Itopava Seca",
                    }
                "sexo" : "Masculino",
            "registro" : "2007.04",
                }                  
            }
        }    
    }   