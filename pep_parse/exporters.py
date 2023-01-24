from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class MyCsvItemExporter(CsvItemExporter):
    HEADER_MAP = {
        'number': 'Номер',
        'name': 'Название',
        'status': 'Статус',
    }

    def _write_headers_and_set_fields_to_export(self, item):
        if self.include_headers_line:
            if not self.fields_to_export:
                self.fields_to_export = ItemAdapter(item).field_names()
            row = [
                self.HEADER_MAP.get(header, header)
                for header in self._build_row(self.fields_to_export)
            ]
            self.csv_writer.writerow(row)
