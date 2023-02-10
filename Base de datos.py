from flask import Flask, render_template, request
import mysql.connector


def cargaralimentos():
    mydb=mysql.connector.connect(host='localhost',user='root', password='123456',
                            database='dietas')
    mycursor=mydb.cursor()
    mycursor.execute("select * from alimentos")
    lista_alimentos=mycursor.fetchall()
    mydb.close()
    return lista_alimentos



def busqueda():
    
    mydb=mysql.connector.connect(host='localhost',user='root', password='123456',
                            database='dietas')
    mycursor=mydb.cursor()
    alimento_usado=request.form['alimento_usado']  #alimento_usado y gramos era por poner
    gramos=request.form['gramos']                  # algún nombre en html
    mycursor.execute("select (`Energía Total (kcal)`*%s/100),(`Grasa Total (g)`*%s/100),(`Proteína Total (g)`*%s/100),(`Carbohidratos (g)`*%s/100) from alimentos where Nombre=%s",(gramos,gramos,gramos,gramos,alimento_usado))
    macros=mycursor.fetchall()
    kcal, grasas, proteinas, hc =macros[0][0:4]
    lista_alimentos=cargaralimentos()
  
    return  alimento_usado, gramos, kcal ,grasas, proteinas, hc