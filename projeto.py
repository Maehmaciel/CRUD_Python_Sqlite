import sqlite3

#Função de inclusão de petshop


def i_petshop():
        
        print("Dados do CLIENTE")
        nome = raw_input("Nome:")
        endereco = raw_input("Endereço:")
        bairro = raw_input("Bairro:")
        cep = raw_input("CEP:")
        cidade = raw_input("Cidade:")
        telefone_res = raw_input("Telefone:")
        telefone_cel = raw_input("Celular:")
        email= raw_input("Email:")
        print("===========================================")
        print("===========================================")
        sql = "insert into pessoa (nome,endereco,bairro,cep,cidade,telefone_res,telefone_cel,email) values (?,?,?,?,?,?,?,?)"
        conn = sqlite3.connect("petshop.db")
        control = conn.cursor()
        control.execute(sql,[nome,endereco,bairro,cep,cidade,telefone_res,telefone_cel,email])
        conn.commit()
        print("Usuario cadastrado com sucesso!")


def raca():
        
        print("Cadastro de raças")
        descricao = raw_input("Nome da raça:")
        porte = raw_input("Porte(Pequeno, medio, grande):")
        especie = raw_input("Especie(ex: Cachorro, gato, tartaruga,):")
        print("===========================================")
        print("===========================================")
        sql = "insert into raca (descricao,porte,especie) values (?,?,?)"
        conn = sqlite3.connect("petshop.db")
        control = conn.cursor()
        control.execute(sql,[descricao,porte,especie])
        conn.commit()
        print("Usuario cadastrado com sucesso!")

def cad_raca():
        conn = sqlite3.connect("petshop.db")
        control = conn.cursor()
        control.execute("select * from raca")
        while (1):
                        row = control.fetchone()
                        if row == None:
                                break
                        print "Raca:" "%s" % (row[1])
                        print "Porte:" "%s" % (row[2])
                        print "Especie:" "%s" % (row[3])
                


def menu():
	print("######Programade cadastro de Petshop######")
	print("#OBS:Cadastre raças e Usuarios, antes de cadastrar o animal, para melhor funcionamento#")
	print("1 Novo usuario")
	print("2 Pesquisa animal/Usuario")	
	print("3 alterar dados")
	print("4 excluir")
	print("5 listar cadastros")
	print("6 novo animal")
	print("7 nova raça")
	print("8 Ver racas cadastradas")
	print("sair do programa digite 0")
	print("===========================================")

def buscar():
        num = int(raw_input("1-pesquisar por ANIMAL/2-Pesquisar por USUARIO"))
        
        if num==1:
                nome = raw_input("Nome do animal:")
                sql = "select * from animal where nome=?"
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                contro = conn.cursor()
                control.execute(sql,[nome])
                while (1):
                        row = control.fetchone()
                        if row == None:
                                break
                                
                        print "resultados encontrados"
                        print "Id:" "%i" % (row[0])
                        print "Nome:" "%s" % (row[1])
                        print "Sexo:" "%s" % (row[2])
                        print "Dono:" "%s" % (row[4])
                        contro.execute("select * from raca where id_raca=?",[row[3]])
                        ro = contro.fetchone()
                        print "Raca:" "%s" % (ro[1])
                        print "Porte:" "%s" % (ro[2])
                        print "Especie:" "%s" % (ro[3])
        if num==2:
                nome= raw_input("Nome do usuario:")
                sql = "select * from pessoa where nome=?"
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                control.execute(sql,[nome])
                contro = conn.cursor()
                while (1):
                        row = control.fetchone()
                        if row == None:
                                break
                        print "resultados encontrados"
                        print "Id:" "%i" % (row[0])
                        print "Nome:" "%s" % (row[1])
                        print "Endereco:" "%s" % (row[2])
                        print "Bairro:" "%s" % (row[3])
                        print "CEP:""%s" % (row[4])
                        print "Cidade:" "%s" % (row[5])
                        print "Telefone:" "%s" % (row[6])
                        print "Celular:" "%s" % (row[7])
                        print "Email:" "%s" % (row[8])
                        contro = conn.cursor()
                        sql="select * from animal where pessoa=?"
                        for ro in contro.execute(sql,[row[1]]):
                                print "Animal:" "%s" % (ro[1])
                       
                        
                        

def listar_tudo():
        num = int(raw_input("1-Listar todos os ANIMAL/2-Listar todos os USUARIO"))
        if num==1:
                 
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                control.execute("select * from animal")
                
                while (1):
                        row = control.fetchone()
                        if row == None:
                                break
                                
                        print "resultados encontrados"
                        print "Id:" "%i" % (row[0])
                        print "Nome:" "%s" % (row[1])
                        print "Sexo:" "%s" % (row[2])
                        print "Dono:" "%s" % (row[4])
                        contro = conn.cursor()
                        contro.execute("select * from raca where id_raca=?",[row[3]])
                        ro = contro.fetchone()
                        print "Raca:" "%s" % (ro[1])
                        print "Porte:" "%s" % (ro[2])
                        print "Especie:" "%s" % (ro[3])
                
                        
                        
        if num==2:
                 
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                contro = conn.cursor()
                control.execute("select * from pessoa")
                while (1):
                        row = control.fetchone()
                        if row == None:
                                break
                                
                      
                        print "resultados encontrados"
                        print "Id:" "%i" % (row[0])
                        print "Nome:" "%s" % (row[1])
                        print "Endereco:" "%s" % (row[2])
                        print "Bairro:" "%s" % (row[3])
                        print "CEP:""%s" % (row[4])
                        print "Cidade:" "%s" % (row[5])
                        print "Telefone:" "%s" % (row[6])
                        print "Celular:" "%s" % (row[7])
                        print "Email:" "%s" % (row[8])
                        contro = conn.cursor()
                        sql="select * from animal where pessoa=?"
                        for ro in contro.execute(sql,[row[1]]):
                                print "Animal:" "%s" % (ro[1])
                        
                
                        
                                
                        
                        

def alterar():
        num = int(raw_input("1-alterar dados do ANIMAL/2-alterar dados do USUARIO"))
        if num==1:
                nome = raw_input("Nome Atual:")
                noma = raw_input("Novo Nome:")
                sexo = raw_input("Sexo(F)/(M):")
                raca= raw_input("Raça:")
                sql = "update animal set nome=?, sexo=?, raca=? where nome=?"
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                control.execute(sql,[noma,sexo,raca,nome])
                conn.commit()
                print("Sucesso!")
        if num==2:
                nome = raw_input("Nome Atual:")
                noma = raw_input("Novo Nome:")
                endereco = raw_input("Endereço:")
                bairro = raw_input("Bairro:")
                cep = raw_input("CEP:")
                cidade = raw_input("Cidade:")
                telefone_res = raw_input("Telefone:")
                telefone_cel = raw_input("Celular:")
                email = raw_input("Email:")
                sql = "update  pessoa set nome=?,endereco=?,bairro=?,cep=?,cidade=?,telefone_res=?,telefone_cel=?,email=? where nome=?"
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                control.execute(sql,[noma,endereco,bairro,cep,cidade,telefone_res,telefone_cel,email,nome])
                conn.commit()
                print("Sucesso!")

def apagar():
        num = int(raw_input("1-Deletar ANIMAL/2-Deletar USUARIO"))
        if num==1:
                noma = raw_input("Nome do animal:")
                sql = "delete from animal where nome=?"
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                control.execute(sql,[noma])
                conn.commit()
                print("Sucesso!")
        if num==2:
                nome = raw_input("Nome do usuario:")
                sql = "delete from animal where pessoa=?"
                dois="delete from pessoa where nome=?"
                conn = sqlite3.connect("petshop.db")
                control = conn.cursor()
                control.execute(sql,[nome])
                control.execute(dois,[nome])
                conn.commit()
                print("Sucesso!")

def novo_animal():
        nome = raw_input("Usuario Dono:")
        noma = raw_input("Nome do bichinho:")
        sexo = raw_input("Sexo(F)/(M):")
        raca= raw_input("Raça:")
        sq="select id_raca from raca where descricao=?"
        conn = sqlite3.connect("petshop.db")
        control = conn.cursor()
        control.execute(sq,[raca])
        while (1):
                row = control.fetchone()
                if row == None:
                        break
                                
                      
                print "Raça Encontrada"
                a=row[0]
                print int(a)
                sql= "insert into animal(nome,sexo,raca,pessoa) values (?,?,?,?)"
                control.execute(sql,[noma,sexo,a,nome])
                conn.commit()
                print("Bichinho cadastrado com sucesso!")
                break
#Aqui o programa principal
menu()
op=1
while(op!=0):
	op = int(raw_input("Digite a opção:"))
	if op==1:
		i_petshop()
	if op==2:
		buscar()
	if op==3:
		alterar()
	if op==4:
		apagar()
	if op==5:listar_tudo()
	if op==6:
		novo_animal()
	if op==7:
		raca()
	if op==8:
		cad_raca()



