import psycopg2
import pandas as pd


def Populate(connectionSTR):

    conn = psycopg2.connect(connectionSTR)  # GLobal host
    cur = conn.cursor()

    Location = "./exchange-code-mic-mapping.csv"

    table = Location[2:-4]
    print(table)

    cur.execute("CREATE TABLE IF NOT EXISTS \"" + table + "\" ();")
    try:
        cur.execute(f"ALTER TABLE \"{table}\" ADD COLUMN \"EQUITY EXCH NAME\" text;")
        conn.commit()
        cur.execute(f"ALTER TABLE \"{table}\" ADD COLUMN \"EQUITY EXCH CODE\" text;")
        conn.commit()
    except:
        print("The table already exists!")
        return

    df = pd.read_csv(Location)

    exchName = df["EQUITY EXCH NAME"]
    exchCode = df["EQUITY EXCH CODE"]



    for i in range(len(df)):
        if str(exchName[i]) != "No Exchange " and str(exchName[i]) != "nan":
            insert = f"INSERT INTO \"{table}\" VALUES ('{exchName[i]}', '{exchCode[i]}');"
            cur.execute(insert)
            conn.commit()

def main():
    password = input("Please Enter the Password for the Postgres Database: ")

    connectionSTR = "dbname='postgres' user='postgres' host='dev-datafactory-postgresql.csodrrohkuas.us-east-1.rds.amazonaws.com' password=" + password;
    Populate(connectionSTR)

if __name__ == '__main__':
     main()
