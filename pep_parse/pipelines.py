import csv
import datetime
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class PepParsePipeline:
    def open_spider(self, spider):
        self.pep_count = Counter()

    def process_item(self, item, spider):
        self.pep_count.update((item['status'],))
        return item

    def close_spider(self, spider):
        now = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        path = BASE_DIR / 'results' / f'status_summary_{now}.csv'
        with open(path, 'w', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, dialect='unix')
            writer.writerow(('Статус', 'Количество'))
            writer.writerows(self.pep_count.items())
            writer.writerow(('Total', sum(self.pep_count.values())))
