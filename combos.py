class Combos:
    def __init__(self):
        self.success = 0
        self.failed = 0
        self.remaining = 0

        self.combo_list = None

    def parse_combos(self, path):
        f = open(path, 'r', encoding='utf-8')
        content = f.read()

        combo_list = content.strip().split('\n')
        self.combo_list = combo_list

        self.remaining = len(self.combo_list)

    def update_success(self):
        self.success += 1
        self.remaining -= 1

        print(f'Successful: {self.success} | Failed: {self.failed}    ', end='\r')

    def update_failed(self):
        self.failed += 1
        self.remaining -= 1

        print(f'Successful: {self.success} | Failed: {self.failed}    ', end='\r')
