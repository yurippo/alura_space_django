from django.db import models

# Create your models here.

class Fotografia(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    descricao = models.TextField(null=False, blank=False)
    foto = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"Fotografia [nome={self.nome}]"

#About ORM 

# A tecnologia do ORM (Object-Relational-Mapper) se faz presente no desenvolvimento de aplicações web independentemente da linguagem utilizada para o desenvolvimento do projeto. O entendimento de seu funcionamento é essencial para um profissional da área.

# Para aprender o que é um ORM basta pensar que o conceito de mapeamento relacional do objeto gira em torno da ideia de conseguirmos escrever queries em código SQL por meio do paradigma da orientação a objetos de uma linguagem de programação.

# Isso é feito através do mapeamento dos parâmetros de um objeto e de sua tradução para a estrutura de tabelas encontradas em um RDBMS (Relational Database, Management System - Sistema de Gerenciamento de Banco de Dados Relacional).

# alt text: Na imagem há um bloco onde está escrito “Aplicação”. Uma seta apontando para ambos os sentidos liga o bloco a um outro em que está escrito “ORM”. Sob a seta, podemos ler “Objetos de OOP”. Outra flecha apontando para ambos os sentidos liga “ORM” a outro bloco, em que está escrito “Banco de dados”. Sob a flecha, lemos “Objetos de banco de dados”.

# Cada linguagem (ou mesmo framework) que suporta orientação a objetos possui um ORM de utilização mais comum:

# Python e Flask: SQLAlchemy;
# Python e Django: Django ORM;
# Java: Hibernate;
# C#: Dapper ORM;
# PHP: Doctrine;
# .NET framework : Microsoft Entity Framework.
# Vantagens da utilização de um ORM:
# Possibilita, para quem programa, construir bancos de dados utilizando sua linguagem de programação de maior fluência, sem ter que se aprofundar nas complexidades do código SQL;
# Torna a aplicação independente do RDBMS utilizado. Isso facilita uma eventual migração de banco de dados, bem como a escrita de queries genéricas que se enquadram nos mais diversos RDBMS (MySQL, PostgreSQL, Microsoft SQL Server, etc);
# A conexão entre a aplicação e o banco de dados se torna robusta, segura e menos sujeita a erros de código, uma vez que poucas intervenções de código são necessárias;
# Alguns ORM como o SQLAlchemy possuem um toolkit completo de ferramentas extras que otimizam a interação com o banco de dados.
# Desvantagens da utilização de um ORM:
# A integração de ORMs com sistemas legados pode ser problemática;
# Pode criar a ilusão, para desenvolvedores iniciantes, que não é necessária uma compreensão básica de linguagem SQL para se tornar um profissional completo de desenvolvimento de aplicações web.
# A utilização de ORMs em desenvolvimento de softwares acaba sendo bem transversal em relação aos possíveis frameworks existentes, ou seja, a presença de um ORM não é específica apenas do Django, mas de outros frameworks variados como o Flask, por exemplo. Inclusive esse mesmo assunto já foi abordado na formação de Flask aqui da plataforma.

#Models no Django

# Um modelo é uma forma única e definitiva de informações sobre seus dados, é ele que contém os campos e comportamentos essenciais dos dados que você está armazenando.

# Sabendo disso, analise as afirmações abaixo e selecione as corretas com relação aos models.

# Cada atributo do modelo representa um campo no banco de dados.

# Veja o seguinte exemplo:

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)

# Ficaria representado no banco como:

# CREATE TABLE myapp_person (
#     "id" serial NOT NULL PRIMARY KEY,
#     "first_name" varchar(30) NOT NULL,

# Todo modelo é uma classe Python, subclasse de django.db.models.Model.

# Todo modelo é uma classe, conforme podemos ver na documentação.

# https://docs.djangoproject.com/pt-br/4.1/topics/db/models/


#Para saber mais: Models

# Vimos que cada modelo é uma classe Python que geralmente é mapeada para ser uma tabela no banco de dados.

# Caso queira saber mais sobre Models do Django, acesse o que diz a documentação oficial do Django sobre Models.

# https://docs.djangoproject.com/pt-br/4.1/topics/db/models/