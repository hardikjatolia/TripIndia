import MainRepo


class Repo(MainRepo.Repo):
    def createCityTable(self):
        try:
            query = """CREATE TABLE IF NOT EXISTS "Cities" (
                "index" SERIAL UNIQUE,
                "name" TEXT UNIQUE PRIMARY KEY,
                "knownas" TEXT,
                "state" TEXT
            );"""
            self.cur.execute(query)
        except Exception as e:
            print(e)
            return False
        return True

    def addCity(self, name, knownas, state):
        try:
            query = """INSERT INTO "Cities" ( "name" ,"knownas", "state") VALUES ('{}','{}','{}');""".format(
                name, knownas, state)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def getCityByName(self, name):
        try:
            query = """ SELECT * from "Cities" WHERE "name" = '{}';""".format(
                name)
            self.cur.execute(query)
            data = self.cur.fetchall()
            city = {"index": data[0][0], "name": data[0][1],
                    "knownas": data[0][2], "state": data[0][3]}
        except Exception as e:
            print(e)
            return [False, None]
        return [True, city]

    def getCityByIndex(self, index):
        try:
            query = """ SELECT * from "cITIES" WHERE "index" = '{}';""".format(
                index)
            self.cur.execute(query)
            data = self.cur.fetchall()
            city = {"index": data[0][0], "name": data[0][1],
                    "knownas": data[0][2], "state": data[0][3]}
        except Exception as e:
            print(e)
            return [False, None]
        return [True, city]

    def getAllCities(self):
        try:
            query = """ SELECT * from "Cities"; """
            self.cur.execute(query)
            table = self.cur.fetchall()
        except Exception as e:
            print(e)
            return [False, None]
        cities = []
        for data in table:
            city = {"index": data[0][0], "name": data[0][1],
                    "knownas": data[0][2], "state": data[0][3]}
            cities.append(city)
        return [True, cities]

    def getCitiesByState(self, state):
        try:
            query = """ SELECT * from "Cities"
                        WHERE "state" = '{}'; """.format(state)
            self.cur.execute(query)
            table = self.cur.fetchall()
        except Exception as e:
            print(e)
            return [False, None]
        cities = []
        for data in table:
            city = {"index": data[0][0], "name": data[0][1],
                    "knownas": data[0][2], "state": data[0][3]}
            cities.append(city)
        return [True, cities]

    def deleteCityByIndex(self, index):
        try:
            query = """DELETE from "Cities" WHERE "index" = '{}';""".format(
                index)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def deleteCityByName(self, name):
        try:
            query = """DELETE from "Cities" WHERE "name" = '{}';""".format(
                name)
            self.cur.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            return False
        return True

    def delteCitiesTable(self):
        try:
            query = """ DROP TABLE IF EXISTS "Cities"; """
            self.cur.execute(query)
        except Exception as e:
            print(e)
            return False
        return True
