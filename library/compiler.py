from json import load


class Compiler:
    def __init__(self):
        super().__init__()
        json = self.get_json("../test.json")
        self.children = json.get("childWidgets")
        self.children_len = len(json.get("childWidgets"))+1
        self.sout_that_u_deserve(json)

    @staticmethod
    def get_json(file_name):
        with open(file_name, 'r') as j_file:
            json = load(j_file)
        return json

    def sout_that_u_deserve(self, json):
        print(json.get("type")+'{')
        for key, value in json.items():
            if key == "type":
                continue
            if key == "childWidgets":
                for i in value:
                    print("layout.add_by_id("+str(i.get('id'))+")")
            else:
                print(str(key) + ' = ' + str(value))
        print('}')

        self.children_len = self.children_len - 1
        if self.children_len != 0:
            self.sout_that_u_deserve(self.children[self.children_len-1])


if __name__ == '__main__':
    Compiler()
