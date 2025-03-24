import mysql.connector

def hae_tyontekijat():
    try:
        yhteys = mysql.connector.connect(
            host="localhost",
            user="root",  # Укажите вашего пользователя
            password="",  # Укажите ваш пароль
            database="yritys"
        )
        
        kursori = yhteys.cursor()
        kursori.execute("SELECT etunimi, sukunimi, osasto, palkka FROM tyontekijat")
        tulokset = kursori.fetchall()
        
        for etunimi, sukunimi, osasto, palkka in tulokset:
            print(f"{etunimi} {sukunimi} | Osasto: {osasto} | Palkka: {palkka:.2f} €")
        
        kursori.close()
        yhteys.close()
        
    except mysql.connector.Error as err:
        print(f"Virhe tietokantayhteydessä: {err.errno} ({err.sqlstate}): {err.msg}")

if __name__ == "__main__":
    hae_tyontekijat()
