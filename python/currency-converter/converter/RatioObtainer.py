import json, datetime, urllib.request

RATIOS_FILENAME = 'ratios.json'
API_URL = 'https://api.exchangeratesapi.io'

class RatioObtainerException(Exception):
    pass

class RatioObtainer:
    base = None
    target = None
    cached_ratios = []

    def __init__(self, base, target):
        self.base = base
        self.target = target
        self.load_cached_ratios_from_file()

    def load_cached_ratios_from_file(self):
        try:
            with open(RATIOS_FILENAME) as ratios_file:
                content = ratios_file.read()
                self.cached_ratios = json.loads(content)
        except:
            self.cached_ratios = []
            print('[WARNING]', 'Ratios cache file loading error. Using API instead')

    def flush_cached_ratios_to_file(self):
        try:
            with open(RATIOS_FILENAME, 'w') as ratios_file:
                content = json.dumps(self.cached_ratios)
                ratios_file.write(content)
        except:
            print('[WARNING]', 'Ratios cache file saving error')

    def was_ratio_saved_today(self):
        return bool(self.get_matched_ratio_value())

    def fetch_ratio(self):
        with urllib.request.urlopen(API_URL + '/latest?base=' + self.base) as request:
            content = request.read()
            data = json.loads(content)
            ratio = data['rates'][self.target]
            if ratio and not self.was_ratio_saved_today():
                self.save_ratio(ratio)
            return ratio

    def save_ratio(self, ratio):
        ratio_dict = {
            'base_currency': self.base,
            'target_currency': self.target,
            'date_fetched': self.today_date(),
            'ratio': ratio
        }

        self.cached_ratios.append(ratio_dict)
        self.flush_cached_ratios_to_file()

    def get_matched_ratio_value(self):
        for currency in self.cached_ratios:
            if (currency['base_currency'] == self.base and
                currency['target_currency'] == self.target and
                currency['date_fetched'] == self.today_date()):
                return currency['ratio']

    def today_date(self):
        return str(datetime.date.today())

