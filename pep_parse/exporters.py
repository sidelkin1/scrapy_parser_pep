from itemadapter import ItemAdapter
from scrapy.exporters import CsvItemExporter


class CustomCsvItemExporter(CsvItemExporter):
    def _write_headers_and_set_fields_to_export(self, item):
        if self.include_headers_line:
            if not self.fields_to_export:
                self.fields_to_export = ItemAdapter(item).field_names()
            row = list(self._build_row(self.fields_to_export))
            if hasattr(item, 'header_map'):
                row = [item.header_map.get(header, header) for header in row]
            self.csv_writer.writerow(row)
