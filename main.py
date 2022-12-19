from googleapiclient.discovery import build
import httplib2
from oauth2client.service_account import ServiceAccountCredentials


def accessing_the_api(url: str) -> dict:
    """Возвращает словарь с журналом действий через get запрос к API amoCRM"""
    pass


def getting_an_access_copy(credentials_file: str):
    """Возвращает экземпляр доступа к google sheets API"""
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        credentials_file,
        ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive'])
    httpAuth = credentials.authorize(httplib2.Http())

    return build('sheets', 'v4', http=httpAuth)


def update_values(spreadsheet_id: str, cell: str, data: str) -> None:
    """Записывает данные в определенную ячейку"""
    service.spreadsheets().values().batchUpdate(
        spreadsheetId=spreadsheet_id,
        body={
            "valueInputOption": "USER_ENTERED",
            "data": [
                {"range": cell,
                 "values": [[data]]
                 }
            ]
        }
    ).execute()


if __name__ == "__main__":
    CREDENTIALS_FILE = "credentials.json"
    spreadsheet_id = "spreadsheet_id"
    service = getting_an_access_copy("credentials.json")
    data = accessing_the_api(url="")

    # Преобразуем в читабильную строку
    data = ';\n '.join(
        [f'{key.capitalize()}: {value}' for key, value in data.items()])

    update_values(spreadsheet_id, cell="A1", data=data)
