import schedule
from tradingview_ta import TA_Handler, Interval
import FileManager

RAW_ASSETS_LIST = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'XRPUSDT', 'ADAUSDT', 'SOLUSDT',
                  'MATICUSDT', 'CHZUSDT', 'ATOMUSDT', 'AVAXUSDT', 'DOTUSDT', 'ALGOUSDT',
                  'AAVEUSDT', 'MANAUSDT', 'SANDUSDT', 'FTMUSDT', 'UNIUSDT',
                  'TRXUSDT', 'NEARUSDT', 'XLMUSDT', 'ZILUSDT', 'XTZUSDT', 'LTCUSDT']

ASSETS_LIST_HOURLY = []
ASSETS_LIST_DAILY = []
ASSETS_LIST_WEEKLY = []

def create_asset_lists():
    for item in RAW_ASSETS_LIST:
        ASSETS_LIST_HOURLY.append(TA_Handler(symbol=item, screener='Crypto', exchange='Binance', interval=Interval.INTERVAL_1_HOUR))
        ASSETS_LIST_DAILY.append(TA_Handler(symbol=item, screener='Crypto', exchange='Binance', interval=Interval.INTERVAL_1_DAY))
        ASSETS_LIST_WEEKLY.append(TA_Handler(symbol=item, screener='Crypto', exchange='Binance', interval=Interval.INTERVAL_1_WEEK))


def generate_data_indicators_all(asset_list):
    print('Generating CSV Files...')
    indicator_asset_list = []
    for item in asset_list:
        print(f'CSV FOR: {item.symbol}')
        indicator_asset_list.append(item.get_analysis().indicators)
    return indicator_asset_list

def collect_hourly_data():
    path = 'Data\\indicators_file_HOURLY.csv'
    indicator_Data = generate_data_indicators_all(ASSETS_LIST_HOURLY)
    FileManager.convert_indicators_to_CSV(path, RAW_ASSETS_LIST, indicator_Data, 'HOURLY')

def collect_daily_data():
    path = 'Data\\indicators_file_DAILY.csv'
    indicator_Data = generate_data_indicators_all(ASSETS_LIST_DAILY)
    FileManager.convert_indicators_to_CSV(path, RAW_ASSETS_LIST, indicator_Data, 'DAILY')

def collect_weekly_data():
    path = 'Data\\indicators_file_WEEKLY.csv'
    indicator_Data = generate_data_indicators_all(ASSETS_LIST_WEEKLY)
    FileManager.convert_indicators_to_CSV(path, RAW_ASSETS_LIST, indicator_Data, 'WEEKLY')


schedule.every().hour.at(":00").do(collect_hourly_data)
schedule.every().hour.at(":01").do(collect_daily_data)
schedule.every().hour.at(":02").do(collect_weekly_data)

create_asset_lists()

while True:
    schedule.run_pending()