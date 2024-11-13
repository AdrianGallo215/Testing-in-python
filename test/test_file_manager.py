import unittest
from unittest.mock import MagicMock, patch, mock_open
from src.utils.file_manager import FileManager

class TestFileManager(unittest.TestCase):

    @patch ('builtins.open', new_callable=mock_open, read_data="Nombre,Apellido\nAdrian,Gallo")
    @patch('csv.reader')
    def test_read_csv(self, mock_csv_reader, mock_open):
        mock_csv_reader.return_value = [["Nombre", "Apellido"], ["Adrian", "Gallo"]]

        resultado = FileManager.read_csv("test.csv")

        mock_open.assert_called_once_with("test.csv",mode="r")
        mock_csv_reader.assert_called_once()
        assert resultado == mock_csv_reader.return_value

    @patch('builtins.open', new_callable=mock_open)
    @patch('csv.writer')
    def test_export_csv(self, mock_csv_writer, mock_open):
        csv_writer_instance = MagicMock()
        mock_csv_writer.return_value = csv_writer_instance
        data = [["Nombre", "Apeliido"], ["Adrian", "Gallo"]]

        FileManager.export_csv(data,"test.csv")

        mock_open.assert_called_once_with("test.csv",mode="w", newline=" ")
        csv_writer_instance.writerow.assert_called_with(["Adrian", "Gallo"])

    @patch('builtins.open', new_callable=mock_open, read_data='[{"Nombre": "Adrian"}, {"Nombre": "Marcelo"}]')
    @patch('json.load')
    def test_read_json(self, mock_json_read, mock_open):
        mock_json_read.return_value = [{"Nombre": "Adrian"}, {"Nombre": "Marcelo"}]

        resultado = FileManager.read_json("test.json")

        mock_open.assert_called_once_with("test.json", mode="r")
        mock_json_read.assert_called_once()
        assert resultado == mock_json_read.return_value

    @patch('builtins.open', new_callable=mock_open)
    @patch('json.dump')
    def test_export_json(self, mock_json_dump, mock_open):
        data = [{"Nombre": "Adrian"}, {"Nombre": "Marcelo"}]

        FileManager.export_json(data, 'test.json')

        mock_open.assert_called_once_with('test.json', mode="w")
        mock_json_dump.assert_called_once_with(data, mock_open(), indent=4)

if __name__ == '__main__':
    unittest.main()
